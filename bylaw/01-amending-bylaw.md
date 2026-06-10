# {{ metadata.campaign_brand }}

**Status:** {{ metadata.status }} | Version: {{ metadata.version }} | Last substantive review: {{ metadata.last_substantive_review }}

---

> **Note to readers.** This bylaw is a single-section amendment to existing City of London By-law No. CPOL.-70(b)-220 (Remuneration for Elected Officials and Appointed Citizen Members Policy). It adds one new section — section 4.3 — to that existing instrument. It does NOT re-enact base pay, annual indexing under existing section 4.2, the zero floor and wage-freeze pause in section 4.2, the recurring 70th-percentile base reset established by Council in resolution 2025-C06 (November 4, 2025), or any other component already in the City framework. Those provisions continue to operate untouched.
>
> The v13 series is a fundamental architectural change from the v12 single-clause modifier of section 4.2. v13 introduces a **parallel persistent ledger** called the *accumulated decrement*, applied multiplicatively on top of whatever section 4.2 indexing and any future base re-pegs produce. The decrement persists across all base-setting events including the recurring re-pegs directed by resolution 2025-C06 Part (d). Levy decreases erode the decrement (floored at zero; no pay increase ever generated). There is no upper cap on the decrement.
>
> The 2.3-draft revision anchors the levy measure to the statutory defined term for the City's levy (the *general local municipality levy*, *Municipal Act, 2001* subsection 312(1)) net of Treasurer-published assessment growth, so the change PACT measures corresponds to the "tax levy increase from rates" the City already publishes in its annual budget documents. Details in [`CHANGELOG.md`](https://github.com/mmward9/london-council-pay-bylaw/blob/main/CHANGELOG.md).
>
> Full audit trail, including the Perplexity Pro Deep Research audit on v13, the v13.1 delta-review, and the v13.2 confirmation review (all completed 2026-05-23 in the same Perplexity thread), is in [`docs/`](https://github.com/mmward9/london-council-pay-bylaw/tree/main/docs).

---

## Preamble

**WHEREAS** the Council of The Corporation of the City of London is authorized under section 5(3), section 8(1), section 8(2), and paragraphs 1, 2 and 3 of subsection 10(2) of the *Municipal Act, 2001*, S.O. 2001, c. 25, to pass by-laws respecting the governance structure, the accountability and transparency, and the financial management of the municipality, including the remuneration of its elected officials;

**AND WHEREAS** By-law No. CPOL.-70(b)-220 (Remuneration for Elected Officials and Appointed Citizen Members Policy) governs the remuneration of elected officials of the City of London;

**AND WHEREAS** the property tax levy adopted by Council in each fiscal year reflects Council's exercise of its fiscal authority and represents the most direct decision through which Council determines the financial burden borne by City of London property taxpayers;

**AND WHEREAS** the Council of The Corporation of the City of London considers it appropriate, in the interests of fiscal accountability, alignment between elected official remuneration and the fiscal capacity decisions taken by Council, and the continued public confidence in the integrity of municipal compensation, to maintain a persistent record of the cumulative effect of Council's property tax levy decisions on the remuneration of elected officials, applied multiplicatively on top of remuneration otherwise payable under this Policy;

**AND WHEREAS** this section does not affect the base compensation set or maintained by Council in any other resolution or by-law and does not affect Council's authority to set the property tax levy or to set or update base compensation in any year;

**THE MUNICIPAL COUNCIL OF THE CORPORATION OF THE CITY OF LONDON ENACTS as follows:**

## Enacting clauses

1. The provisions of City of London Policy CPOL.-70(b)-220 (Remuneration for Elected Officials and Appointed Citizen Members Policy) are amended by adding a new section 4.3 in the form set out in clause 2 of this by-law. To the extent that any prior provision of section 4 of the Policy relating to annual adjustment, base compensation, or levy-linkage is inconsistent with the new section 4.3, the new section 4.3 prevails.

2. The new section 4.3 of City of London Policy CPOL.-70(b)-220 is:

## Section 4.3 — Permanent Decrement Tied to Property Tax Levy

**4.3(a) Definitions.** For the purpose of this section:

**(i) "Annual rating by-law"** means the by-law passed by Council in each fiscal year under subsection 312(2) of the *Municipal Act, 2001* that sets the rates of taxation upon the assessment of the lands and premises in the City of London for the purpose of raising the general local municipality levy for that year.

**(ii) "Total municipal tax levy"** for a fiscal year means the general local municipality levy of the City of London for that fiscal year within the meaning of subsection 312(1) of the *Municipal Act, 2001*, being the amount the City of London decided to raise in its budget for that year under section 290 of the *Municipal Act, 2001* on all rateable property in the City of London, as that amount stands when the annual rating by-law for that fiscal year is adopted. For greater certainty, the total municipal tax levy does not include amounts levied for education purposes under the *Education Act*, amounts raised by any special local municipality levy within the meaning of subsection 312(1) of the *Municipal Act, 2001*, or revenue from fees and charges. The total municipal tax levy is not adjusted for later supplementary estimates, supplementary assessments, or mid-year true-ups unless the budget for that fiscal year is formally amended before the annual rating by-law is adopted. Where the total municipal tax levy for a fiscal year cannot be determined under this clause, the determination shall be made by the City Treasurer and documented in the records of the office of the City Clerk.

**(iii) "Levy change percentage"** for a fiscal year means the percentage change in the total municipal tax levy for that fiscal year, net of the assessment growth amount for that fiscal year, compared to the total municipal tax levy for the immediately preceding fiscal year, calculated as (((current-year total municipal tax levy minus the assessment growth amount for the current fiscal year) minus previous-year total municipal tax levy) divided by previous-year total municipal tax levy) multiplied by 100, with the result rounded to two decimal places. The value may be positive (the levy increased by more than assessment growth), zero, or negative (the levy decreased, or increased by less than assessment growth). For greater certainty, an increase in the total municipal tax levy that is wholly attributable to the assessment growth amount produces a levy change percentage of zero, and the levy change percentage is intended to correspond to the tax levy increase from rates as published in the City's annual budget documents. Where the total municipal tax levy for the immediately preceding fiscal year is zero or cannot be determined, the levy change percentage for that fiscal year shall be deemed to be zero.

**(iv) "Accumulated decrement"** means a non-negative percentage value, initially zero when this section first comes into force, that is updated each fiscal year as set out in subsection (b) of this section. The accumulated decrement is a persistent state variable maintained by the City Treasurer and is not reset by any resolution, by-law, or amendment of this Policy other than one that expressly repeals or amends this section 4.3.

**(v) "Remuneration"** as used in this section means the base compensation of an elected official as set under this Policy, and any additional stipend or allowance paid to an elected official under this Policy as it may be amended from time to time, including without limitation any stipend paid to the Deputy Mayor or Budget Chair.

**(vi) "Fiscal year"** for the purposes of this section means the calendar year January 1 to December 31, being the City of London's fiscal year within the meaning of section 285 of the *Municipal Act, 2001*.

**(vii) "Assessment growth amount"** for a fiscal year means the portion of the change in the total municipal tax levy for that fiscal year, relative to the immediately preceding fiscal year, that is attributable to changes in the assessment roll, including new construction, additions, improvements, expansions, and supplementary assessments, rather than to changes in tax rates, as that portion is determined by the City Treasurer and published in the City's annual budget documents. Where the City Treasurer publishes that determination as a percentage rather than a dollar amount, the assessment growth amount is that percentage applied to the total municipal tax levy for the immediately preceding fiscal year. Where no such determination is made or published for a fiscal year, the assessment growth amount for that fiscal year is deemed to be zero.

**4.3(b) Annual update of the accumulated decrement.** For each fiscal year in which this section is in force, the accumulated decrement shall be updated as follows:

Updated accumulated decrement (in percentage points) = the greater of:

(i) zero, and

(ii) the previous fiscal year's accumulated decrement plus the levy change percentage for the current fiscal year.

The accumulated decrement shall not be less than zero in any fiscal year. There is no upper bound on the accumulated decrement.

**4.3(c) Application to remuneration.** For each fiscal year in which this section is in force, the remuneration payable to each City of London elected official shall be calculated as follows:

(i) first, compute the remuneration that would otherwise be payable under section 4.2 of this Policy and under any resolution, by-law, or amendment governing base compensation, applying all annual adjustments under section 4.2 and any re-peg or reset of base compensation in force for that fiscal year, all without reference to the accumulated decrement and without including any reduction attributable to the accumulated decrement from prior or current fiscal years; and

(ii) then, multiply the result of step (i) by (1 minus the current accumulated decrement expressed as a decimal fraction).

The resulting amount is the final remuneration payable for that fiscal year. For greater certainty, the operation of section 4.2 in any fiscal year is unaffected by the accumulated decrement under this section; section 4.2 produces its result independently, and the accumulated decrement is applied only at the point of computing the final remuneration payable. Where the accumulated decrement equals or exceeds 100, the final remuneration payable for that fiscal year is zero.

**4.3(d) Persistence across re-peg events.** The accumulated decrement persists across, and continues to be applied after, any resolution, by-law, or amendment that establishes, resets, updates, or otherwise modifies the base compensation of City of London elected officials, including without limitation the update directed by Council resolution 2025-C06 clause (d) and any subsequent periodic re-peg under similar resolutions. Any such re-peg modifies the input to step (i) of subsection (c) of this section for the affected fiscal year and subsequent fiscal years; the accumulated decrement continues to be applied in step (ii) on each such re-pegged value.

**4.3(e) Calculation and publication by Treasurer.** The City Treasurer shall:

(i) calculate the levy change percentage, the assessment growth amount, and the accumulated decrement for each fiscal year in which this section is in force,

(ii) maintain a record of these values in the records of the office of the City Clerk,

(iii) include the current fiscal year's levy change percentage, the assessment growth amount used in that calculation, the accumulated decrement, and the final remuneration payable for the Mayor and Councillors in the City's published annual budget documents and in any annual remuneration disclosure required by law,

(iv) where the annual rating by-law for a fiscal year has not been adopted before the first remuneration payment date in that fiscal year, use the previous fiscal year's accumulated decrement for interim remuneration calculations and reconcile any difference in the first remuneration payment following adoption of the annual rating by-law, and

(v) without limiting subsection (iv), where any calculation under subsection (i), maintenance of records under subsection (ii), or publication under subsection (iii) has not been completed before the date on which the relevant annual rating by-law is adopted, perform the calculation, recording, or publication as soon as practicable and in any event no later than 60 days after the end of the relevant fiscal year, and apply the resulting accumulated decrement retroactively to the remuneration for the relevant fiscal year, with any over- or under-payment reconciled in the next remuneration payment period following the calculation.

**4.3(f) First year of application.** This section first applies to the remuneration payable for the first fiscal year that begins on or after the date this by-law comes into force. The levy change percentage for that fiscal year is determined under clause (a)(iii) of this section, comparing that fiscal year to the immediately preceding fiscal year. The previous fiscal year's accumulated decrement for the purpose of subsection (b) is zero in the first fiscal year of application.

**4.3(g) For Greater Certainty.** This section does not alter the base compensation of any elected official as set or maintained by Council under any other resolution or by-law, does not restrict or alter Council's authority to set the property tax levy in any year, and does not restrict or alter Council's authority to set or update the base compensation. This section operates by maintaining and applying a separate accumulated decrement to the remuneration otherwise payable, and that decrement applies regardless of the value of any base compensation set by Council. Council's authority to amend or repeal this section is not restricted, but any such amendment or repeal must be done through a properly-passed by-law and is subject to the same public process as any amendment to this Policy.

**4.3(h) Internal Priority.** If there is any conflict between this section and any other provision of this Policy, this section prevails to the extent of the conflict. For greater certainty, this subsection applies only to interpretation conflicts within section 4 of this Policy relating to annual adjustment, base compensation, and levy-linkage.

**4.3(i) Rounding.** All percentage and percentage-point calculations under this section shall be rounded to two decimal places at each computational step.

## Coming Into Force

3. This by-law shall come into force and effect on the day of its passage.
