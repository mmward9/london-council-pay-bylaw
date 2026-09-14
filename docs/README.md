# Audit Trail for the PACT Bylaw

This directory contains the working documents that produced the current operative bylaw text. Each file is a primary-source artefact of the design, audit, or political record. They are kept here for transparency: every reader of this repository can trace why the bylaw reads the way it reads.

## 3.0-draft (current)

3.0-draft keeps the v13 decrement ledger and replaces its trigger. The by-law no longer measures the property tax levy; it measures the residential municipal tax rate Council sets in the annual rating by-law, adjusted for MPAC reassessment, on a home whose assessment did not change, with a CPI allowance from the first year. The change and its rationale are recorded in [`../CHANGELOG.md`](../CHANGELOG.md).

| File | What it is |
|---|---|
| [constant-assessment-example.md](constant-assessment-example.md) | One-page worked example of the 3.0-draft meter: the formula, the CPI allowance, a table of scenarios including a reassessment year, and the public line. |

## v13 series (decrement ledger — architecture retained; levy trigger superseded by 3.0-draft)

The v13 series introduced the current architecture: a parallel persistent ledger applied multiplicatively on top of section 4.2 and any future base re-pegs, persisting across all base-setting events including the recurring re-pegs directed by resolution 2025-C06 Part (d). These documents describe the ledger with its original levy trigger; the ledger is unchanged in 3.0-draft, the trigger is not. Three Perplexity reviews completed in the same thread on 2026-05-23: a comprehensive Deep Research audit on v13, a delta-review on v13.1, and a confirmation review on v13.2.

| File | What it is |
|---|---|
| [v13-proposal.md](v13-proposal.md) | The full v13.2 proposal: rationale, mechanism, worked example, operative text, Appendix A enacting language, implementation cascade, refinements log, and the deferred post-election handoff items list. |
| [v13-deep-research-audit.md](v13-deep-research-audit.md) | Perplexity Pro Deep Research audit on v13. Comprehensive legal, drafting, and political audit across 18 sections. Verdict: CONDITIONAL PASS with two required drafting fixes plus optional improvements. |
| [v13.1-delta-review.md](v13.1-delta-review.md) | Perplexity delta-review confirming v13.1 (the version that incorporated the v13 audit fixes). Verdict: UNCONDITIONAL PASS subject to three precision edits. |
| [v13.2-confirmation-review.md](v13.2-confirmation-review.md) | Perplexity confirmation review on v13.2 (the version that incorporated all v13.1 precision edits plus the 60-day enforceability backstop and Appendix A presentation cleanup). Verdict: UNCONDITIONAL PASS. The audit cycle on v13.2 is closed. |

## v12 series (superseded — kept for transparency)

| File | What it is |
|---|---|
| [v12-proposal.md](v12-proposal.md) | The v12 proposal. The single-clause amending by-law structure that modified section 4.2's annual adjustment in years with a positive levy change. Superseded by v13 because v12 did not survive base-setting re-pegs (each re-peg would have wiped the accumulated effect). |
| [v12-deep-research-audit.md](v12-deep-research-audit.md) | Perplexity Pro Deep Research audit on v12 (2026-05-22, 209 sources). Confirmed v12 was structurally sound but flagged the re-peg gap that v13 closes. |

## Political record

| File | What it is |
|---|---|
| [2025-c06-vote-record.md](2025-c06-vote-record.md) | Full verbatim per-vote tally of the November 4, 2025 London Council vote on resolution 2025-C06 (the 70th-percentile pay reset for the 2026-2030 term). Sourced directly from the official Council Minutes (eSCRIBE DocumentId 120361). Designed as a source document for campaign communications. |

## Post-election materials

| File | What it is |
|---|---|
| [post-election/](post-election/) | Materials that would be used in a post-election Solicitor / Treasurer review cycle. Per locked campaign decision, the PACT bylaw stays in this repo and on ward9.online pre-election; the items in `post-election/` are not pursued in the current cycle. |

## Why these documents are in the repository

The bylaw text in [`rendered/BYLAW.md`](../rendered/BYLAW.md) is the operative instrument. Everything in this directory is the supporting record. Readers who want to argue with the bylaw can argue with it on the verifiable record. Readers who want to suggest a change can do so knowing exactly what work has already been done.
