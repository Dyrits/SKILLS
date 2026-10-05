# ORD-88: Store order totals in whole cents

Invoices for the Hollis Mill shop show totals that are off by a cent on some orders (for example 0.1 + 0.2 shows 0.30000000000000004 in the export). The cause is the `total` column, which stores a floating point number.

Goal: store the order total as an integer number of cents, convert existing rows once, and stop using the float column.

Out of scope: currency conversion, changing the invoice layout.
