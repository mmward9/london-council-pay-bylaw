# Changelog

All notable changes to the Pay Accountable to City Taxpayers (PACT) Bylaw are recorded here. Each entry corresponds to a version line in `rendered/BYLAW.md`. Version-bump rules are documented in `VERSIONING.md`.

## 1.0-draft — 2026-05-22 — Architectural pivot: standalone bylaw to amending by-law

**MAJOR bump.** The PACT Bylaw was previously designed as a standalone bylaw that re-invented the entire council remuneration framework: base pay, annual indexing formula, a 50% floor, a no-exception clause, an inflation reference, and an annual reporting obligation. Twelve audit iterations and two Perplexity Pro Deep Research passes, together with direct retrieval of the actual City of London remuneration framework documents from london.ca and the consolidated Municipal Act from ontario.ca, established that the City already has a complete remuneration framework in By-law CPOL.-70(b)-220 (Remuneration for Elected Officials and Appointed Citizen Members Policy) plus the resolution 2025-C06 base reset adopted on November 4, 2025. The new design replaces the standalone bylaw with a single-clause amending by-law that adds the one piece the City framework lacks: the levy link.

**Operative changes from the perspective of a candidate or pledger reading the new bylaw vs. the prior one:**

- The bylaw no longer sets base pay. Council base pay is set by resolution 2025-C06 at the 70th percentile of 2020 median full-time employment income for Londoners per the 2021 Census (approximately $94,222 for councillors; the Mayor base is maintained at $168,908). The PACT Bylaw does not change those figures and does not change Councils authority to reset them at the next quadrennial Council Resourcing Review.
- The bylaw no longer establishes its own annual indexing formula. Section 4.2 of CPOL.-70(b)-220 continues to indexed elected official remuneration by the average annual variation in median full-time employment income from census data, with a zero floor in 4.2(a) and a wage-freeze pause in 4.2(b).
- The bylaw no longer establishes its own pay floor. PACT modifies the section 4.2 annual adjustment in years with a positive levy increase percentage, by the same number of percentage points as the levy increase. In all other years, section 4.2 applies unchanged.
- The bylaw no longer specifies "no exceptions." Council retains all its existing tools for handling extraordinary circumstances; PACT only constrains the formula-driven annual adjustment.
- The bylaw no longer requires its own annual report. The City Treasurers existing section 284 annual remuneration statement continues to cover the public-reporting obligation.

**What PACT does add:** a single new section 4.3 to CPOL.-70(b)-220 that links the section 4.2 annual adjustment to the levy decision Council itself makes each year. If the levy increases, the section 4.2 adjustment is reduced by the same number of percentage points as the levy increase. The reduction can produce a negative adjustment (the section 4.2 zero floor and wage-freeze pause are expressly overridden). The mechanism does not claw back already-paid remuneration; it modifies the future annual adjustment component.

**Statutory authority verified from primary sources:** Municipal Act, 2001 sections 5(3), 8(1), 8(2), and 11(2) paragraphs 1 (governance structure) and 3 (financial management). The earlier draft cited section 283 as the authority, but section 283 governs local board remuneration and the Mississauga / Markham transitional provisions; the council remuneration authority since the 2006 Municipal Statute Law Amendment Act rests on the broad permissive grant in sections 5, 8, and 11. The earlier section 283 citation has been corrected.

**Strong-mayor framework:** The PACT amending by-law is not a budget by-law under sections 289 or 290 of the Municipal Act and is not within the O. Reg. 530/22 section 5(1) carve-out from the head-of-council veto. Veto exposure applies. The two-thirds council override threshold under section 284.11(9) is 10 of 15 council members. Per O. Reg. 580/22 the prescribed provincial priorities are limited to housing-unit construction and housing-supporting infrastructure; no plausible provincial-priority ground for a veto of a remuneration by-law of this kind is apparent.

**Conflict of interest:** Section 4(i) of the Municipal Conflict of Interest Act expressly exempts a members pecuniary interest in remuneration "by reason of being a member" from the disclosure / disqualification rules in MCIA sections 5, 5.2, and 5.3. All fifteen members of Council (Mayor plus 14 Councillors) may vote on introduction, debate, and passage of the amending by-law.

**Pre-introduction prerequisites still open** (per the City Solicitor / Treasurer handoff memo in `docs/solicitor-handoff.md`): counsel opinion on the override and downward-adjustment authority, Treasurer mapping of the "total municipal tax levy" definition to Londons actual annual rating by-law line items, and three belt-and-suspenders confirmations on Mayor coverage and MCIA s. 4(i).

**Architecture changes in the repository** for this version:
- Operative bylaw text now at `bylaw/01-amending-bylaw.md` (replaces `bylaw/00-title.md` through `bylaw/08-inflation.md`).
- `parameters.yaml` is now metadata + verified primary-source references only (no more reinvented compensation parameters).
- `build/render.py` is the updated single-file renderer.
- The eight earlier section files, the old `parameters.yaml`, the old `render.py`, and the old `examples/retrospective-2024-2027.md` are preserved at `legacy/` for the audit trail.
- New `docs/` directory contains the full audit trail: v12 proposal, Deep Research audit (209 sources), November 4 2025 vote record, and the Solicitor / Treasurer handoff memo.

## Unreleased

- **2026-05-13: Brand rename.** The bylaw was previously referred to in campaign materials as the "Council Pay Accountability Bylaw." It is now branded the *Pay Accountable to City Taxpayers (PACT) Bylaw*. The formal long title in `rendered/BYLAW.md` ("A bylaw to tie the remuneration of the Council of the City of London to the annual operating property-tax levy") is unchanged. A "Short title" clause has been added to `bylaw/00-title.md` per standard municipal bylaw style. No operative effect. No version bump per `VERSIONING.md` (rename is editorial).
