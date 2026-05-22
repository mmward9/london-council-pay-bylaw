#!/usr/bin/env python3
"""
Render the bylaw from source materials.

Reads:
  parameters.yaml          policy parameters
  bylaw/*.md               prose sections (Jinja templates) in filename order

Writes:
  rendered/BYLAW.md        canonical rendered bylaw

Usage:
  python build/render.py            # renders to rendered/
  python build/render.py --check    # exits non-zero if rendered/ is stale
"""
from pathlib import Path
import sys
import yaml
from jinja2 import Environment, BaseLoader, StrictUndefined


def currency(amount):
    """$94,222"""
    if amount is None:
        return "$0"
    return "${:,.0f}".format(amount)


def percent(value):
    """1.0%"""
    if value is None:
        return "0%"
    return "{:g}%".format(value)


def render_bylaw(repo_root: Path) -> str:
    params_path = repo_root / "parameters.yaml"
    bylaw_dir = repo_root / "bylaw"

    if not params_path.exists():
        raise SystemExit(f"Missing {params_path}")
    if not bylaw_dir.exists():
        raise SystemExit(f"Missing {bylaw_dir}")

    with params_path.open() as f:
        params = yaml.safe_load(f)

    section_files = sorted(bylaw_dir.glob("*.md"))
    if not section_files:
        raise SystemExit(f"No section files in {bylaw_dir}")

    env = Environment(
        loader=BaseLoader(),
        undefined=StrictUndefined,
        trim_blocks=False,
        lstrip_blocks=False,
        keep_trailing_newline=True,
    )
    env.filters["currency"] = currency
    env.filters["percent"] = percent

    pieces = []
    for f in section_files:
        text = f.read_text()
        template = env.from_string(text)
        rendered = template.render(**params)
        pieces.append(rendered)

    return "\n\n".join(pieces).rstrip() + "\n"


def render_examples(repo_root: Path) -> dict:
    """Render any Jinja templates in examples/ to the same path with extension preserved."""
    examples_dir = repo_root / "examples"
    if not examples_dir.exists():
        return {}
    with (repo_root / "parameters.yaml").open() as f:
        params = yaml.safe_load(f)
    env = Environment(
        loader=BaseLoader(),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
    )
    env.filters["currency"] = currency
    env.filters["percent"] = percent
    out = {}
    for f in sorted(examples_dir.glob("*.md")):
        out[f.name] = env.from_string(f.read_text()).render(**params)
    return out


def main():
    repo_root = Path(__file__).resolve().parent.parent
    rendered_dir = repo_root / "rendered"
    rendered_dir.mkdir(exist_ok=True)

    bylaw_md = render_bylaw(repo_root)
    examples = render_examples(repo_root)

    check_mode = "--check" in sys.argv

    bylaw_out = rendered_dir / "BYLAW.md"
    if check_mode:
        existing = bylaw_out.read_text() if bylaw_out.exists() else ""
        if existing != bylaw_md:
            print(f"STALE: {bylaw_out}", file=sys.stderr)
            sys.exit(1)
        for name, body in examples.items():
            ex_out = rendered_dir / "examples" / name
            ex_existing = ex_out.read_text() if ex_out.exists() else ""
            if ex_existing != body:
                print(f"STALE: {ex_out}", file=sys.stderr)
                sys.exit(1)
        print("rendered/ is in sync with sources.")
        return

    bylaw_out.write_text(bylaw_md)
    print(f"Wrote {bylaw_out}")

    (rendered_dir / "examples").mkdir(exist_ok=True)
    for name, body in examples.items():
        out = rendered_dir / "examples" / name
        out.write_text(body)
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()
