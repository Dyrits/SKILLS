# Invoice export: specifications

An account owner downloads their invoices as a CSV file.

## Behavior

- The file has the columns `id`, `issued_on`, `total`.
- Dates are written as `YYYY-MM-DD`.
- Totals use a dot as the decimal separator.
