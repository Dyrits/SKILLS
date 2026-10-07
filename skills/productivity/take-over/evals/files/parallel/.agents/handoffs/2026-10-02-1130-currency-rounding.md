# Handoff: currency rounding in totals

Supersedes: none (forked from `2026-10-02-1000-invoice-export-pagination.md`)
Workspace: invoice-service, branch `currency-rounding`

## Goal

Find why exported totals differ by one cent from the ledger for some currencies, found while testing pagination.

## State

- Reproduced for JPY and KWD only (verified: ran the export against the fixture account).

## Decisions

None.

## Next

1. Compare the rounding mode in `src/export/totals.ts` with the ledger's.

## Open questions

None.

## Sources

None.
