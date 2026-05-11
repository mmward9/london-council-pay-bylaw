# Dissent

This directory tracks the strongest opposing arguments to the bylaw. Each file is one argument and the response to it. The goal is to publicly demonstrate engagement with the steel-manned version of every serious objection.

## Why this exists

A common criticism of any political proposal is "you only listen to people who agree with you." This directory is the answer. Every substantive opposing argument that has been raised, in good faith, is recorded here with its strongest possible formulation and a written response.

If your suggestion was a substantive disagreement and got rejected, it lives here.

## File format

```markdown
---
argument: "Short title of the opposing argument"
raised_by: "Source (issue number, person, publication) — optional"
status: open | incorporated | rejected
date: YYYY-MM-DD
---

## The argument

A clear, strong, fair-minded summary of the opposing view. Steel-man it.

## Our response

The bylaw's response to this argument. Why the bylaw is structured as it
is despite this consideration. Or, if the argument has been incorporated,
a link to the PR that did so.
```

## Adding a new dissent file

1. Use the "Suggest a change" form on ward9.online if you want to be sure your argument is captured.
2. Or open a PR with a new file at `dissent/NNN-short-slug.md` using the next sequential number.
