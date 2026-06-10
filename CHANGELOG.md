# Changelog

All notable changes to the Pay Accountable to City Taxpayers (PACT) Bylaw are recorded here. Each entry corresponds to a version line in `rendered/BYLAW.md`. Version-bump rules are documented in `VERSIONING.md`.

## 2.3-draft — 2026-06-10 — Levy measure anchored to the statutory levy definition, net of assessment growth; single-tier citation fix

**MINOR bump (2.2-draft → 2.3-draft).** Per `VERSIONING.md`, adjusting the reduction formula's input and adding an operationally-referenced definition are MINOR-bump changes. Pledges pinned to 2.2-draft are flagged on the public scoreboard as "pledged against an earlier version"; candidates can re-pledge through the OTP flow.

**Why the change.** The City of London publishes two levy-increase figures every budget cycle: the total tax levy increase, and the "Tax Levy % Increase from Rates," which the City's own budget tables footnote as "adjusts for change in total levy due to assessment growth." The from-rates line is the number everyone quotes (8.7% for 2024, 7.3% for 2025); the total line was 10.4% and 8.5% in the same years, because growth in the assessment roll (chiefly new construction) adds levy dollars without raising anyone's tax bill. As drafted in 2.2, the levy change percentage measured the total line while every public explanation of PACT used the from-rates line, and the exclusion intended to remove assessment-value effects operated only "to the extent separately identified in the annual rating by-law," which London's rating by-law does not do (it publishes tax rates by property class, not dollar amounts). Net effect: the decrement would have accrued roughly 1.2 to 1.7 percentage points per year faster than the published examples implied, and council would have been docked pay for new homes joining the tax roll. That contradicts the design intent. PACT responds to the tax increase existing taxpayers actually bear.

**Operative changes a pledger would notice side-by-side:**

- 4.3(a)(ii) "total municipal tax levy" is re-anchored to the statutory defined term: the *general local municipality levy* under *Municipal Act, 2001* s. 312(1) ("the amount the local municipality decided to raise in its budget for the year under section 290 on all rateable property"). Education amounts and special local municipality levies sit outside that term by definition; the Treasurer-determination fallback is retained.
- New 4.3(a)(vii) defines "assessment growth amount": the portion of the year-over-year levy change attributable to changes in the assessment roll (new construction, additions, improvements, expansions, supplementary assessments) as determined by the City Treasurer and published in the City's annual budget documents; deemed zero if no determination is published.
- 4.3(a)(iii) "levy change percentage" is now computed net of the assessment growth amount and is intended to correspond to the City's published "tax levy increase from rates." A levy increase wholly attributable to assessment growth produces a levy change percentage of zero.
- 4.3(e)(i) and 4.3(e)(iii): the Treasurer also calculates and publishes the assessment growth amount used.
- 4.3(f) cross-references the 4.3(a)(iii) definition instead of restating the formula without the netting.
- Preamble citation corrected from subsection 11(2) (the lower-tier and upper-tier grant) to subsection 10(2) (the single-tier grant; London is a single-tier municipality), now citing paragraphs 1, 2 and 3 so each recited matter maps to a cited paragraph. The matter lists of the two subsections are identical; the authority is unchanged. On its own this would have been an editorial/patch change; it ships with the MINOR bump.

**Sources for the levy figures:** City of London 2025 Annual Budget Update ("Tax Levy % Increase" vs "Tax Levy % Increase from Rates," Note 1); City of London 2025 Tax Rates schedule (rates by property class only). Statutory text verified against the e-Laws consolidated *Municipal Act, 2001* (ss. 10(2), 11(2), 283, 285, 290, 312).

## 2.2-draft — 2026-05-23 — Architectural pivot: parallel persistent ledger applied multiplicatively (v13 series)

**MAJOR bump (1.0-draft → 2.2-draft).** Per `VERSIONING.md`, this is a MAJOR bump because v13 *removes and replaces the persistence-of-reduction rule* by changing the fundamental mechanism from a section 4.2 modifier (v12) to a parallel persistent ledger (v13). All pledges to the 1.0-draft version are automatically flagged on the public scoreboard as "pledged against an earlier version" and candidates can re-pledge through the OTP flow.

**Why the change.** A load-bearing question on v12: would a future base re-peg (such as the recurring re-peg directed by Council resolution 2025-C06 Part (d) in 2028, and similar future cycles) erase accumulated PACT decreases? Answer: yes, because v12 modified the annual adjustment under section 4.2 but left Council's base-setting authority untouched, and any re-peg would wipe the accumulated drift. The drafting directive was clear: PACT is useless without a permanent bite. v13 closes the gap by introducing a parallel persistent ledger that survives every base-setting event.

**Operative changes a candidate or pledger would notice on side-by-side comparison:**

- The mechanism is no longer a modifier to the section 4.2 annual adjustment. v13 introduces a **separate state variable** called the *accumulated decrement* (non-negative percentage, persistent across all fiscal years).
- The decrement is updated each fiscal year by the levy change percentage, floored at zero. Levy increases add to the decrement; levy decreases erode it. There is no upper cap on the decrement; the political-optics tradeoff was confirmed legally sustainable in the v13 audit.
- The decrement is applied **multiplicatively** to the result of section 4.2 (and any base re-peg). Section 4.2 operates on its own pre-decrement trajectory and is unaffected by the decrement; the decrement is applied only at the final-payable step.
- The decrement **persists across all base-setting events** by explicit text in 4.3(d) and 4.3(g). A re-peg modifies the input to the multiplication; the decrement still applies on top.
- A new s. 4.3(a)(vi) defines "fiscal year" by cross-reference to *Municipal Act* s. 285 (calendar year January 1 to December 31).
- New s. 4.3(e)(iv) handles the interim period between January 1 and adoption of the annual rating by-law (uses prior-year decrement for interim calculations, reconciles upon adoption).
- New s. 4.3(e)(v) is a Treasurer-compliance backstop: any late calculation must be performed "as soon as practicable and in any event no later than 60 days after the end of the relevant fiscal year," with retroactive application and reconciliation in the next payment period.
- The enacting clauses now use "add-and-supersede" language with the conflict-resolution scope narrowed to "annual adjustment, base compensation, or levy-linkage" (mirrors the s. 4.3(h) internal-priority scope so the carrying by-law cannot accidentally override unrelated provisions of section 4).

**Audit cycle on v13 series.** Three Perplexity reviews completed in the same Perplexity thread on 2026-05-23:

1. **v13 Deep Research audit:** CONDITIONAL PASS with two required drafting fixes (fiscal-year definition; interim-calculation timing) and three optional improvements (compounding clarification; Treasurer non-compliance reconciliation; explicit enacting clause). Decrement cap (optional improvement 3) was rejected per the standing campaign-design directive.
2. **v13.1 delta-review:** UNCONDITIONAL PASS subject to three one-line precision edits (event-anchored lateness trigger; "without limiting subsection (iv)" sequencing priority; optional 60-day enforceability backstop) and a presentation-only Appendix A cleanup.
3. **v13.2 confirmation review:** UNCONDITIONAL PASS. "v13.2 is legally sound, internally coherent, and drafting-complete. The document is ready for introduction."

All three reviews are in [`docs/`](docs/) (`v13-deep-research-audit.md`, `v13.1-delta-review.md`, `v13.2-confirmation-review.md`).

**Statutory authority verified from primary sources** (carries through from v12 with one addition): Municipal Act, 2001 sections 5(3), 8(1), 8(2), 11(2) paragraphs 1 (governance structure) and 3 (accountability and transparency), 283 (remuneration), 285 (fiscal year), and 312(2) (annual rating by-law).

**Repository changes for this version:**

- Operative bylaw text rewritten in `bylaw/01-amending-bylaw.md`. New Section 4.3 has nine subsections (a-i); prior v12 had seven (a-g). Added definitions: "accumulated decrement", "fiscal year". Restructured Treasurer duties under (e) from three sub-duties to five.
- `parameters.yaml` metadata: `version` bumped from `1.0-draft` to `2.2-draft`; `last_substantive_review` to `2026-05-23`.
- `docs/`: existing v12 audit working papers preserved under explicit v12-prefixed names; v13 series added; `solicitor-handoff.md` moved to `docs/post-election/` per the locked decision that the bylaw stays in this repo and on ward9.online pre-election (no external counsel review in this cycle).
- `README.md` and `docs/README.md` updated to reflect the v13 architecture and the new docs structure.

**What stays unchanged:** `dissent/`, `pledges/`, `pilot-commitment.md`, `VERSIONING.md`, `LICENSE`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`. The v12 architecture rationale and the v12 audit findings are preserved in `legacy/` and in `docs/v12-proposal.md` and `docs/v12-deep-research-audit.md`.

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
