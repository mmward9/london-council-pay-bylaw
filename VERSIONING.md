# Versioning policy

The Council Pay Accountability Bylaw is a public document under active drafting. Candidates who pledge to support it on [ward9.online/pledge/](https://ward9.online/pledge/) pin their pledge to a specific version. This file is the editorial rulebook for what causes the version number to change.

The version line appears at the top of [`rendered/BYLAW.md`](rendered/BYLAW.md) in the form:

```
**Status:** <status> | Version: <version> | Last substantive review: <date>
```

## Format

Versions follow a relaxed [SemVer](https://semver.org/) scheme with an optional pre-release suffix:

```
MAJOR.MINOR.PATCH[-suffix]
```

While the bylaw is in pre-1.0 drafting (the entire current period), the format is `0.<minor>[-suffix]`, e.g. `0.1-draft`, `0.2`, `0.3.1`. Once the bylaw reaches its first "ready-to-submit" state it will move to `1.0.0` and the rest of this document applies in full.

## What bumps the version

A version bump means existing pledges to earlier versions are flagged as "needs reaffirming" on the public scoreboard. Use it deliberately. A version bump fires when the operative effect of the bylaw changes — not when the wording changes. The bar is: would a reasonable candidate who has already pledged want a chance to re-read the bylaw before remaining on the record as a supporter?

### MAJOR bump (1.0.0 -> 2.0.0)
Reserved for fundamental restructuring of the bylaw. Examples:

- A change to which offices are subject to the bylaw (mayor, councillor, deputy mayor, budget chair).
- A change to the underlying mechanism that ties remuneration to the levy. Switching from "percentage of levy increase" to "absolute dollar tie," for example.
- Removing or replacing the persistence-of-reduction rule. A bylaw that lets remuneration snap back is a different policy from one that doesn't.

### MINOR bump (0.1 -> 0.2, 1.0 -> 1.1)
Substantive but bounded changes. Examples:

- Adjusting the threshold above which a remuneration reduction kicks in.
- Adjusting the reduction formula. Going from 1-to-1 down to 0.5-to-1, or the reverse.
- Adding a new clause that creates a new obligation or constraint on council. Quorum rules for re-establishing baselines, mandatory annual reporting, anything that adds a duty.
- Adding or removing a definition that is referenced operationally. Adding an "exemption" definition is a minor bump even if nothing currently fits.
- A change to whether the bylaw applies retroactively to in-term raises.

### PATCH bump (0.2 -> 0.2.1, 1.1 -> 1.1.1)
Clarifying changes that do not alter operative effect but resolve real ambiguity. Examples:

- Replacing an undefined term with a defined one. Going from "the levy" to "the annual operating property-tax levy as defined in clause 1(b)."
- Splitting a single clause into two for readability, with no operational change.
- Adding or correcting a clear cross-reference. "see clause 4" becomes "see clause 4(b)."
- Reordering clauses where the substantive obligations are identical.

## What does NOT bump the version

Editorial fixes that change zero operative effect. These get committed without touching the version line:

- Spelling, grammar, punctuation, capitalization.
- Whitespace, indentation, markdown formatting.
- Adding or correcting hyperlinks to external sources (Municipal Act citations, City pages).
- Adding or correcting source attributions in the bylaw's footnote area.
- README, AUTHORS, LICENSE, the changelog itself, this file.
- Build tooling, CI configuration, repository hygiene.

If a change looks editorial but you find yourself wondering whether it qualifies, ask: would a candidate reading their pledged version side-by-side with the new version notice an operational difference? If yes, it is at least a patch bump. If no, it is editorial.

## How to bump

1. Edit `rendered/BYLAW.md` to update the version line. Increment the appropriate digit, set everything to the right of it back to zero, and update the `Last substantive review:` date.
2. Append a dated entry to `CHANGELOG.md` describing the change in candidate-facing language. "What changed and why," not "diff of clause 3(b)."
3. Commit and push.
4. The ward9.online site rebuilds on the next cron tick. Pledges to the prior version automatically appear as "needs reaffirming." A proactive reaffirmation email goes out to pledged candidates once the campaign is approved to send mail.

## Examples

| Change                                                              | Bump                |
| ------------------------------------------------------------------- | ------------------- |
| Fix "councilor" to "councillor"                                     | None (editorial)    |
| Add a markdown header                                               | None (editorial)    |
| Define "affected office" for the first time                         | Patch               |
| Reword clause 3 for clarity, same effect                            | Patch               |
| Change the threshold from 0% to 2% levy growth before reduction     | Minor               |
| Add a clause requiring an annual report from the City Clerk         | Minor               |
| Add the Deputy Mayor to the list of affected offices                | Minor               |
| Switch from "percentage tied to levy" to "dollar tied to levy"      | Major               |
| Remove the persistence-of-reduction rule                            | Major               |

## Why this exists

A pledge that means "I support whatever this document says, present and future" is a pledge to nothing. Pinning each pledge to a specific version protects candidates from being bound to language they did not agree to, and protects voters from a bylaw whose meaning shifts after the pledges are collected. This file is the contract between the bylaw's drafters and the candidates who put their name on it.
