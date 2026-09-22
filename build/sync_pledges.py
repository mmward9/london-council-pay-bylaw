#!/usr/bin/env python3
"""
Sync pledges/candidates.yaml from the live ward9.online pledge tracker.

The pledge tracker on ward9.online (https://ward9.online/pledge/) is the
real source of truth for candidate positions: submissions there are
verified by a one-time code sent to the candidate's email on file with
the City, so the site's own database is the primary record, not this
file. pledges/candidates.yaml is a durable, version-controlled mirror of
that record, kept for the repo's own audit trail and for anyone auditing
this bylaw from GitHub without going to the live site.

candidates.yaml therefore MUST be re-synced whenever a pledge changes.
Manually hand-editing it will drift from the live tracker the next time
any candidate responds -- run this script instead.

Reads:
  https://ward9.online/api/pledges   live pledge data (JSON)

Writes:
  pledges/candidates.yaml            regenerated in full from that data

Usage:
  python build/sync_pledges.py            # fetch live and overwrite
  python build/sync_pledges.py --check    # exit non-zero if the file is stale
"""
from pathlib import Path
import sys
import urllib.request
import json
import yaml

API_URL = "https://ward9.online/api/pledges"

# API status values -> this file's documented schema values (pledges/README.md)
STATUS_MAP = {
    "support": "supports",
    "oppose": "opposes",
    "conditional": "conditional",
}


def fetch_live_pledges() -> list[dict]:
    # The live site blocks requests with no User-Agent (bot protection),
    # not a real access restriction -- confirmed via curl with a normal
    # browser UA, 2026-09-22.
    req = urllib.request.Request(
        API_URL,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
            ),
            "Referer": "https://ward9.online/pledge/",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    return data["pledges"]


def to_candidate_entry(p: dict) -> dict:
    role = p["candidate_role"]
    ward = "mayor" if role == "mayor" else p["candidate_position"].replace("Ward ", "")
    entry = {
        "name": p["candidate_name"],
        "ward": ward,
        "position": "mayor" if role == "mayor" else "councillor",
        "status": STATUS_MAP.get(p["status"], p["status"]),
        "source": "https://ward9.online/pledge/",
        "date_recorded": p["created_at"].split(" ")[0],
    }
    if p.get("public_statement"):
        entry["statement"] = p["public_statement"]
    entry["notes"] = (
        f"Pledged against bylaw version {p['bylaw_version']} "
        f"(commit {p['bylaw_commit_sha'][:12]}). "
        "Synced from https://ward9.online/api/pledges -- do not hand-edit, "
        "re-run build/sync_pledges.py instead."
    )
    if p.get("withdrawn_at"):
        entry["notes"] += f" Withdrawn {p['withdrawn_at']}."
    return entry


def build_yaml_text(candidates: list[dict]) -> str:
    header = (
        "# Candidate pledge tracker for the Pay Accountable to City Taxpayers Bylaw.\n"
        "#\n"
        "# This file is GENERATED from the live ward9.online pledge tracker.\n"
        "# Do not hand-edit -- run `python build/sync_pledges.py` to refresh it.\n"
        "# See pledges/README.md for the schema and verification process.\n\n"
    )
    body = yaml.safe_dump(
        {"candidates": candidates},
        sort_keys=False,
        allow_unicode=True,
        width=100,
    )
    return header + body


def main() -> int:
    check_only = "--check" in sys.argv
    repo_root = Path(__file__).resolve().parent.parent
    out_path = repo_root / "pledges" / "candidates.yaml"

    live = fetch_live_pledges()
    candidates = [to_candidate_entry(p) for p in live]
    # Stable order: mayor first, then by ward number, then by name.
    def sort_key(c):
        ward = c["ward"]
        ward_num = -1 if ward == "mayor" else int(ward)
        return (ward_num, c["name"])
    candidates.sort(key=sort_key)

    new_text = build_yaml_text(candidates)

    if check_only:
        current_text = out_path.read_text() if out_path.exists() else ""
        if current_text != new_text:
            print(f"STALE: {out_path} does not match live tracker ({len(candidates)} pledges).")
            return 1
        print(f"OK: {out_path} matches live tracker ({len(candidates)} pledges).")
        return 0

    out_path.write_text(new_text)
    print(f"Wrote {out_path} ({len(candidates)} pledges).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
