# Changelog

## CHG-0006 · 2026-09-10 · Invoice export scope agreed

Type: Documentation
Event: Agreement
Scope: Invoice export

Summary: The invoice export ships as a CSV download first.
Reason: A CSV covers the finance team's monthly import and is the smallest useful increment.
References: documentation/capabilities/invoice-export/specifications.md
Validation: Approved by the user on 2026-09-10.
Evidence: None beyond the approval.

## CHG-0007 · 2026-09-24 · CSV writer delivered

Type: Code
Event: Delivery
Scope: Invoice export

Summary: The CSV writer and its download endpoint are merged.
Reason: Unblocks the finance import.
References: documentation/capabilities/invoice-export/tasks/01-csv-writer.md
Validation: Unit and integration tests pass; accepted by Marta (product) on 2026-09-24.
Evidence: CI run for the merge commit.
