# Retrospective: what this bylaw would have done for 2024-2027

This is an **illustrative** calculation, not a prediction or a commitment. It shows what would have happened to council remuneration if this bylaw had been in force at the start of the current 2024-2027 multi-year budget.

> **Note on starting baseline.** This retrospective uses the *pre-raise* councillor base pay of **$67,420** as the starting point, because that is the pay that was actually in force during 2024-2027. The new base of {{ policy.base_pay.councillor_cad | currency }} only takes effect with the council term beginning November 17, 2026. A retrospective applied to the pre-raise pay shows what the pre-raise pay would have done under this bylaw; a forward-looking simulation starting from the new $94,222 base would be a separate exercise.

## Inputs

- Starting baseline (councillor, 2024): **$67,420**
- Pay-cut ratio: {{ policy.asymmetry.pay_cut_per_levy_rise_percent }} percent per 1 percent levy increase (1:1)
- Floor (50% of the pre-raise base, hypothetically): $33,710

## Levy increases (operating property-tax levy)

| Year | Approved levy increase |
|---|---|
| 2024 | 8.7% |
| 2025 | ~7.1% |
| 2026 (proposed) | 4.3% |
| 2027 (proposed) | 5.3% |

## Calculation

Each year's pay change is applied to the prior year's baseline, and the new baseline is locked in (the ratchet provision in clause 3(a)).

| Year | Levy change | Pay change | New baseline (councillor) |
|---|---|---|---|
| Start (2024) | — | — | $67,420 |
| End of 2024 | +8.7% | -8.7% | $61,557 |
| End of 2025 | +7.1% | -7.1% | $57,185 |
| End of 2026 | +4.3% | -4.3% | $54,726 |
| End of 2027 | +5.3% | -5.3% | $51,826 |

**Cumulative pay reduction over the term: approximately 23%.**

A councillor who had taken office in November 2022 under this bylaw, assuming the levy trajectory above, would have ended the 2024-2027 term earning roughly $51,800 against a starting baseline of $67,420.

The hypothetical floor at 50 percent of the pre-raise base ($33,710) was not reached.

## What this implies going forward

The new councillor base pay of {{ policy.base_pay.councillor_cad | currency }} takes effect with the term beginning November 17, 2026. Under this bylaw, that becomes the new baseline. Future retrospectives (or forecasts) would use {{ policy.base_pay.councillor_cad | currency }} as their starting point and {{ (policy.base_pay.councillor_cad * policy.floor_percent_of_base / 100) | currency }} as their floor.

## A note on illustration vs prediction

The levy figures above are what the City of London actually approved (2024, 2025) or has proposed (2026, 2027) under the current 2024-2027 multi-year budget. Future levy trajectories will differ. The point of this retrospective is to make the formula concrete, not to predict any future councillor's pay.
