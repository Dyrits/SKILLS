# Handoff: invoice export, CSV writer done

Supersedes: `2026-09-12-0900-invoice-export-kickoff.md`
Workspace: invoice-service, branch `main`

## Goal

Build the invoice export agreed with the team.

## State

- The CSV writer is merged and covered by tests in `src/export/csv.test.ts` (verified: test run).
- The endpoint returns the whole file in one response (verified: read `src/export/handler.ts`).

## Decisions

None.

## Next

1. Pagination for large accounts.

## Open questions

None.

## Sources

- `documentation/capabilities/invoice-export/specifications.md`
