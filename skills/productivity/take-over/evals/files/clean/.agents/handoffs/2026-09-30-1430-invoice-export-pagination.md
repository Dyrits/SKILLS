# Handoff: invoice export, pagination in flight

Supersedes: `2026-09-24-1615-invoice-export-csv.md`.

## State

Pagination is half built on branch `invoice-export-pagination`: the cursor type and the first page query exist, the next-page query does not. Tests for the first page pass.

Because the `legacy_ref` column is unused, the export drops it, and the writer in `src/export/csv.ts` no longer emits it.

The agreed behaviour and columns are in `documentation/capabilities/invoice-export/specifications.md`.

## What is next

Implement the next-page query and its test, then the `Link` response header.

## Suggested skills

`test-first` for the next-page query, `implement` for the header.
