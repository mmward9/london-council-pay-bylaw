# Retrospective: what this bylaw would have done for 2024-2027

This is an **illustrative** calculation, not a prediction or a commitment. It shows what would have happened to council remuneration under this bylaw if it had been in force at the start of the current 2024-2027 multi-year budget.

## Inputs

- Starting baseline (councillor): {{ policy.base_pay.councillor_cad | currency }}
- Pay-cut ratio: {{ policy.asymmetry.pay_cut_per_levy_rise_percent }} percent per 1 percent levy increase
- Floor: {{ policy.floor_percent_of_base }} percent of base

## Levy increases (operating property-tax levy)

| Year | Approved levy increase |
|---|---|
| 2024 | 8.7% |
| 2025 | ~7.1% |
| 2026 (proposed) | 4.3% |
| 2027 (proposed) | 5.3% |

## Calculation

| Year | Levy change | Pay change | New baseline (councillor) |
|---|---|---|---|
| Start | — | — | {{ policy.base_pay.councillor_cad | currency }} |
| End of 2024 | +8.7% | -8.7% | $86,025 |
| End of 2025 | +7.1% | -7.1% | $79,917 |
| End of 2026 | +4.3% | -4.3% | $76,481 |
| End of 2027 | +5.3% | -5.3% | $72,427 |

**Cumulative pay reduction over the term: approximately 23%.**

A councillor who had taken office in November 2022 under this bylaw would have ended the term earning roughly $72,400 against a starting baseline of {{ policy.base_pay.councillor_cad | currency }}.

The floor at {{ policy.floor_percent_of_base }} percent of base ({{ (policy.base_pay.councillor_cad * policy.floor_percent_of_base / 100) | currency }}) was not reached.

This illustration uses the levy figures publicly available at the time of this writing and the current bylaw parameters. If parameters change, the numbers in this table change with them.
