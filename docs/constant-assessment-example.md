# Worked example: the constant-assessment meter (3.0-draft)

One page on what section 4.5 measures and how the numbers move. The operative text in [`bylaw/01-amending-bylaw.md`](../bylaw/01-amending-bylaw.md) governs; this page is illustration.

## What the meter is

A residential property tax bill is assessment × (municipal rate + education rate), plus fees such as water and wastewater that are not property tax at all. Council sets only the municipal rate, in the annual rating by-law. MPAC sets the assessment. The Province sets the education rate.

Section 4.5 reads Council's decision and nothing else. It takes this year's residential municipal tax rate, corrects it for any MPAC reassessment so that a home is compared to itself, and asks: **what happened to the municipal tax on a home whose assessment did not change?** That percentage is the *constant-assessment municipal tax change percentage*.

- `R_t` = this year's residential municipal tax rate (from this year's rating by-law)
- `R_t-1` = last year's residential municipal tax rate
- `F_t` = reassessment adjustment factor: 1 in a year with no MPAC reassessment or phase-in; otherwise the ratio of this year's total residential assessment to last year's, on the same set of properties

```
constant-assessment change (%) = ((R_t × F_t) / R_t-1  −  1) × 100
```

In a year with no reassessment, `F_t = 1` and this is simply the percentage change in the rate, which is exactly the percentage change in the municipal portion of every unchanged-assessment residential bill in the city.

## What counts against pay

Only the part of that change above inflation:

- `CPI` = annual change in the Statistics Canada All-items CPI for Ontario, not seasonally adjusted (the same series Policy s. 4.1 already uses; Statistics Canada does not publish a CPI series specific to London)
- `CPI allowance` = CPI, or zero if CPI is negative

```
applicable change = change                         if change ≤ 0   (a cut erodes the decrement in full)
applicable change = max(0, change − CPI allowance)  if change > 0   (only the excess over inflation adds)

accumulated decrement = max(0, last year's decrement + applicable change)
final pay = pay otherwise payable under Policy ss. 4.2, 4.3, 4.4  ×  (1 − decrement / 100)
```

## The numbers

All rows use a hypothetical CPI of 2.1% unless stated. The 3.4% figure is the City's published 2026 tax increase; because the 2025→2026 assessment phase-in was 0.00%, it is also the change in the residential municipal rate, and so the change in the municipal portion of every unchanged-assessment residential bill.

| Scenario | `R_t` vs `R_t-1` | `F_t` | Constant-assessment change | CPI | Applicable change | Effect on decrement |
|---|---|---|---|---|---|---|
| 2026-style year, no reassessment | +3.40% | 1.0000 | +3.40 | 2.1 | +1.30 | adds 1.30 points |
| Rate rises with inflation | +2.00% | 1.0000 | +2.00 | 2.1 | 0 | none |
| Rate rises exactly at CPI | +2.10% | 1.0000 | +2.10 | 2.1 | 0 | none |
| Rate frozen | 0.00% | 1.0000 | 0.00 | 2.1 | 0 | none |
| Rate cut | −1.00% | 1.0000 | −1.00 | 2.1 | −1.00 | erodes 1.00 point (floor at zero) |
| Deflation year, rate rises | +3.40% | 1.0000 | +3.40 | −0.5 | +3.40 | adds 3.40 (allowance floors at zero, deflation never adds more) |
| Reassessment year, levy flat | −16.67% | 1.2000 | 0.00 | 2.1 | 0 | none (rate fell only because the roll grew 20%) |
| Reassessment year, real 3.4% increase | −13.84% | 1.2000 | +3.40 | 2.1 | +1.30 | adds 1.30, same as a frozen year |

The last two rows are why `F_t` exists. Without it, a raw rate ratio in a reassessment year reads a mechanical rate drop as a tax cut and hands council a decrement erosion for something MPAC did.

## What this means for the historical record

London's published tax increases for 2024, 2025 and 2026 were 8.7%, 7.3% and 3.4%. Under 3.0-draft each of those would have counted against pay only to the extent it exceeded that year's Ontario CPI. The campaign's public figures should therefore be stated as "above inflation" increases; the exact decrement those three years would have produced depends on the Statistics Canada annual-average Ontario CPI for each year and should be computed from the published series, not estimated here.

## The public line

If your house didn't change and your city tax still went up faster than inflation, council pay goes down. Keep up with inflation and pay is whole. Only the extra comes off.
