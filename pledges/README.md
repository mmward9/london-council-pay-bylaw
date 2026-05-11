# Pledges

This directory tracks which candidates in the 2026 City of London municipal election have publicly pledged to support this bylaw, who has declined, and who has not yet responded.

## Why this exists

The pay accountability bylaw is the central plank of one Ward 9 candidate's campaign. Every other candidate for council and mayor has been invited to take a public position. This directory records those positions.

## Statuses

- **`supports`** — The candidate has publicly committed to vote for this bylaw if elected.
- **`opposes`** — The candidate has publicly stated they will not support this bylaw.
- **`conditional`** — The candidate has expressed conditional support, with specific changes they would require.
- **`invited`** — The candidate has been invited to respond and has not yet done so.

Every entry includes a source link to the candidate's public statement (their own social media, their own website, a news interview, a public response to a written invitation, or a recorded council vote).

## Schema

See [`candidates.yaml`](candidates.yaml) for the live file. Each entry has:

```yaml
- name: "Full Name"
  ward: "9"             # or "mayor" for mayoral candidates
  position: "councillor" # or "mayor"
  status: "supports" | "opposes" | "conditional" | "invited"
  source: "https://..."  # link to public statement
  statement: "Optional verbatim quote"
  date_recorded: "YYYY-MM-DD"
  notes: "Optional notes"
```

## Verification

Pledges are verified by direct contact (email or phone) with the candidate before they are recorded as `supports` or `opposes`. The verification record is kept by the repo maintainer.

## Right of reply

Any candidate listed here may, at any time, request that their entry be updated to reflect a change in their position. Updates are made promptly and the prior status is preserved in git history.
