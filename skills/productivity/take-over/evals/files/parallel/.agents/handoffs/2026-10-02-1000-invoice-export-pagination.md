# Handoff: invoice export, pagination in flight

Supersedes: none
Workspace: invoice-service, branch `invoice-export-pagination`

## Goal

Paginate the invoice export so large accounts no longer get the whole file in one response.

## State

- The cursor type and the first page query exist; the next-page query does not (verified: test run).

## Decisions

- Cursor pagination rather than page numbers, because invoices are inserted while an export runs.

## Next

1. Implement the next-page query and its test.

## Open questions

None.

## Sources

None.
