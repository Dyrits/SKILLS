# Invoice export: specifications

An account owner downloads their invoices as a CSV file.

## Columns

`id`, `issued_on`, `total`, `legacy_ref`.

`legacy_ref` is required: the finance team's monthly import reads it, and an export without it breaks that import.

## Pagination

Accounts with more than 5,000 invoices are served in pages of 5,000, linked by a `Link` response header carrying the next cursor.

## Acceptance

A 12,000-invoice account downloads as three pages that concatenate into one valid file.
