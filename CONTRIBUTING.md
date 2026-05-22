# Contributing to the Pay Accountable to City Taxpayers (PACT) Bylaw

Most people should use the **"Suggest a change"** button on [ward9.online/bylaw](https://ward9.online/bylaw). It does not require a GitHub account. It creates a public issue in this repository on your behalf and your suggestion shows up in the same place as the technical contributions.

This document is for people who want to participate directly via GitHub.

## Repository layout (post v12 refactor)

```
bylaw/
  01-amending-bylaw.md       ← operative text (the only source file)
parameters.yaml              ← metadata + verified primary-source references
rendered/BYLAW.md            ← auto-generated; do not edit by hand
docs/                        ← audit trail (v12 proposal, Deep Research,
                                vote record, solicitor handoff)
legacy/                      ← pre-v12 standalone-bylaw archive
                                (kept for transparency; not operative)
dissent/                     ← steel-man opposing arguments
pledges/candidates.yaml      ← candidate pledge tracker
build/render.py              ← the renderer
```

## What to edit, depending on what you're proposing

| Type of change | Edit |
|---|---|
| Change the wording of the operative bylaw | `bylaw/01-amending-bylaw.md` |
| Correct a primary-source reference (URL, citation, version number) | `parameters.yaml` |
| Update the candidate-facing metadata (status, version, review date) | `parameters.yaml` (under `metadata:`) |
| Add a new opposing argument | a new file in `dissent/` |
| Add or update a candidate pledge | `pledges/candidates.yaml` |
| Change the renderer | `build/render.py` |

Do **not** edit `rendered/BYLAW.md` directly. It is rebuilt from the source on every push.

## Why the structure is so spare

Under the v12 amending-by-law approach, PACT adds only ONE new section to the City's existing remuneration policy. All the other compensation parameters — base pay, the recurring 70th-percentile base reset, the annual indexing formula by median full-time employment income variation, the zero floor, the wage-freeze pause — are set by existing City instruments (CPOL.-70(b)-220 and resolution 2025-C06). The PACT repository does not re-state any of those parameters. The pre-v12 design did re-state them in the old `parameters.yaml`, which is preserved at `legacy/parameters.yaml` for reference.

## How to open a pull request

1. Fork this repo.
2. Make your change on a branch.
3. Open a pull request against `main`.

For substantive policy changes, please also open an issue first or use the website form so the discussion can be public before code review. Pull requests that propose substantive policy changes without prior discussion will be converted into issues.

## Version-bump discipline

See [`VERSIONING.md`](VERSIONING.md). Any change to operative effect bumps the version and re-flags existing pledges as "needs reaffirming." Wording-only improvements that preserve operative effect do not bump.

## What gets accepted

- Substantive, good-faith arguments that improve the bylaw.
- Wording improvements that don't change the operative effect.
- Corrections to citations, URLs, or primary-source references.
- Bug fixes to the renderer or CI workflows.
- New dissent files that meaningfully steel-man an opposing view.
- Verified candidate pledges (see [`pledges/README.md`](pledges/README.md) for verification).

## What gets closed

- Personal attacks, harassment, or content targeting individuals rather than policy.
- Spam, off-topic, or content that has nothing to do with the bylaw.
- Duplicate suggestions (the existing thread will be linked).
- Proposals that re-introduce the pre-v12 standalone-bylaw approach (the architectural pivot is documented in `CHANGELOG.md` and `docs/v12-proposal.md`; the duplication of City framework that the standalone approach required is the reason it was retired).
- Suggestions that violate the [Code of Conduct](CODE_OF_CONDUCT.md).

## Moderation

The repo maintainer (currently Matt Millar) is the final decision-maker on what gets merged. Every rejected suggestion is rejected publicly with a reason. The discussion record is part of the policy record.

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Civil engagement is required.
