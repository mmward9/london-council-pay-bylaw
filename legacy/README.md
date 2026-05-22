# Legacy archive — pre-v12 standalone-bylaw design

This directory contains the original source files for the PACT Bylaw from before the v12 architectural pivot. They are kept here for historical reference and for transparency about how the current bylaw evolved.

## What was here before

The original design (versions 0.1-draft through to the version archived here) treated PACT as a standalone bylaw that re-invented the entire council remuneration framework from scratch: base pay parameters, annual indexing rules, a 50% floor, "no exception" clauses, inflation reference, and a recurring publish-and-report mechanism. The source materials produced a multi-section assembled output by Jinja-templating from `parameters.yaml` into eight markdown files in `legacy/bylaw/`.

That design was sound on its own terms but, on closer review of the actual City of London remuneration framework (CPOL.-70(b)-220 plus resolution 2025-C06 of November 4, 2025), turned out to duplicate machinery the City already has. The v12 refactor replaced the standalone approach with a single-clause amending by-law that adds the one piece the City's framework lacks: the levy link.

## What's in this directory

| Path | Original purpose |
|---|---|
| `bylaw/00-title.md` through `bylaw/08-inflation.md` | The eight prose sections that produced the standalone bylaw |
| `parameters.yaml` | Policy parameter file with base pay figures, asymmetric multipliers, floor, inflation reference |
| `examples/retrospective-2024-2027.md` | Worked example illustrating what would have happened to council pay under the old formula in the 2024-2027 budget cycle |
| `build/render.py` | The original multi-section Jinja renderer |
| `rendered/examples/` | The rendered retrospective example |

## Why we kept it

1. **Audit trail.** Pledges, suggestions, and public communications referenced the earlier text. Keeping it visible lets readers see exactly what changed and verify the architectural pivot was deliberate, not silent.
2. **Reusable framework.** The original parameter-driven design pattern (`parameters.yaml` + Jinja sections + render.py) is a working open-source-bylaw template. Other municipalities or future drafters might adapt this design for problems that genuinely need a standalone bylaw.
3. **Honesty about iteration.** Twelve iterations and two Deep Research audit passes produced v12. Pretending the earlier work didn't exist would be dishonest about how the bylaw was actually drafted.

## Authoritative current operative text

The current PACT Bylaw is at [`bylaw/01-amending-bylaw.md`](../bylaw/01-amending-bylaw.md) in the repository root. The rendered version is at [`rendered/BYLAW.md`](../rendered/BYLAW.md). Full design rationale is in [`docs/`](../docs/).
