# Handoff: billing import migration

Supersedes: none
Workspace: billing, branch `main`

## Goal

Migrate the billing importer to the new CSV layout.

## State

- The importer reads the old CSV format; the new format parser is not started (verified: read `src/import/`).

## Decisions

None.

## Next

1. Write the new format parser.

## Open questions

None.

## Sources

- `documentation/specifications/billing-import.md`
