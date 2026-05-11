# The London Council Pay Accountability Bylaw

A proposed bylaw for the City of London, Ontario, drafted in public.

If passed, this bylaw would tie the remuneration of London City Councillors,
the Deputy Mayor, Budget Chair, and Mayor to the City's annual operating
property tax levy. Raise property taxes, council pay drops by the same
percentage. Hold the line, pay matches inflation. Cut taxes, pay rises
modestly above inflation.

The text of the bylaw, the underlying parameters, and the discussion around
each clause are all open for public input. The bylaw is the policy. The
process is the point.

This is a pilot. If the candidate proposing this bylaw is elected, the same
process will be used for every motion brought forward as councillor. Direct
democracy doesn't replace council. It makes sure your councillor knows where
you stand on every issue, not just at election time.

## The current rendered bylaw

See [`rendered/BYLAW.md`](rendered/BYLAW.md). That file is auto-generated
from the source materials in this repo, and is always in sync with the
parameters and prose at HEAD.

## How to suggest a change

**Easy path (recommended for everyone):** visit
[ward9.online/bylaw](https://ward9.online/bylaw) and use the **"Suggest a
change"** button next to any section of the bylaw. You don't need a GitHub
account. Your suggestion becomes a public issue in this repo and will get
a public response.

**Direct path (for the technically inclined):** open a pull request against
this repo. See [CONTRIBUTING.md](CONTRIBUTING.md) for the layout, the
templating conventions, and what gets reviewed.

## What's in this repo

| Path | Purpose |
|---|---|
| [`parameters.yaml`](parameters.yaml) | The policy parameters. Almost all substantive proposed changes live here. |
| [`bylaw/`](bylaw/) | The prose of the bylaw, broken into sections. Variables from `parameters.yaml` are interpolated at render time. |
| [`rendered/BYLAW.md`](rendered/BYLAW.md) | The current canonical bylaw, auto-generated. |
| [`examples/`](examples/) | Illustrative calculations (e.g., what would have happened under this bylaw for the 2024-2027 budget). |
| [`dissent/`](dissent/) | Steel-man opposing arguments. Each file is one argument and its response. Public commitment to engaging with the strongest possible counter-arguments. |
| [`pledges/`](pledges/) | List of candidates and their stance on this bylaw. |
| [`build/`](build/) | The renderer. Reads `parameters.yaml` and the section files and produces `rendered/BYLAW.md`. |

## Who's behind this

Matt Millar, candidate for Ward 9 in the 2026 City of London municipal
election. Authorized by Matt Millar.

## License

Dedicated to the public domain via [CC0 1.0](LICENSE). Adopt, adapt, fork,
reuse for any city, any province, any country. No permission required.
