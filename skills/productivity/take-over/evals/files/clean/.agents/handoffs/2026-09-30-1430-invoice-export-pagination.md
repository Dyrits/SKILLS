# Handoff: invoice export, pagination in flight

Supersedes: `2026-09-24-1615-invoice-export-csv.md`
Workspace: invoice-service, branch `invoice-export-pagination`

## Goal

Paginate the invoice export so large accounts no longer get the whole file in one response.

## State

- Pagination is half built on branch `invoice-export-pagination`: the cursor type and the first page query exist, the next-page query does not.
- Tests for the first page pass (verified: test run).
- Because the `legacy_ref` column is unused, the export drops it, and the writer in `src/export/csv.ts` no longer emits it.

## Decisions

- Cursor pagination rather than page numbers, because invoices are inserted while an export runs.

## Next

1. Implement the next-page query and its test.
2. Add the `Link` response header.

## Open questions

None.

## Sources

- `documentation/capabilities/invoice-export/specifications.md`
