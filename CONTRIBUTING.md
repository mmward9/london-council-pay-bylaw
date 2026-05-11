# Contributing to the London Council Pay Accountability Bylaw

Most people should use the **"Suggest a change"** button on
[ward9.online/bylaw](https://ward9.online/bylaw). It does not require a
GitHub account. It creates a public issue in this repo on your behalf and
your suggestion shows up in the same place as the technical contributions.

This document is for people who want to participate directly via GitHub.

## Repository layout

```
parameters.yaml              ← almost all substantive changes live here
bylaw/                       ← prose sections (Jinja templates)
  01-preamble.md
  02-definitions.md
  ...
rendered/BYLAW.md            ← auto-generated; do not edit by hand
dissent/                     ← steel-man opposing arguments
pledges/candidates.yaml      ← candidate pledge tracker
examples/                    ← illustrative calculations
build/render.py              ← the renderer
```

## What to edit, depending on what you're proposing

| Type of change | Edit |
|---|---|
| Change a policy parameter (e.g., the cut ratio) | `parameters.yaml` only |
| Change the wording of a clause | the relevant file in `bylaw/` |
| Add a new opposing argument | a new file in `dissent/` |
| Add or update a candidate pledge | `pledges/candidates.yaml` |
| Add an illustrative example | a new file in `examples/` |
| Change the renderer | `build/render.py` |

Do **not** edit `rendered/BYLAW.md` directly. It is rebuilt from the source
on every push.

## How to open a pull request

1. Fork this repo.
2. Make your change on a branch.
3. Open a pull request against `main`.

For substantive policy changes, please also open an issue first or use the
website form so the discussion can be public before code review. Pull
requests that propose substantive policy changes without prior discussion
will be converted into issues.

## What gets accepted

- Substantive, good-faith arguments that improve the bylaw.
- Wording improvements that don't change the policy.
- Bug fixes to the renderer or CI workflows.
- New dissent files that meaningfully steel-man an opposing view.
- Verified candidate pledges (see `pledges/README.md` for verification).

## What gets closed

- Personal attacks, harassment, or content targeting individuals rather
  than policy.
- Spam, off-topic, or content that has nothing to do with the bylaw.
- Duplicate suggestions (the existing thread will be linked).
- Suggestions that violate the [Code of Conduct](CODE_OF_CONDUCT.md).

## Moderation

The repo maintainer (currently Matt Millar) is the final decision-maker on
what gets merged. Every rejected suggestion is rejected publicly with a
reason. The discussion record is part of the policy record.

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Civil engagement is required.
