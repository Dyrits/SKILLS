# Discount codes

Status: approved. Project: Tidewater Shop (invented), module `shop/discount.py`.

## Agreed behavior

- A cart may carry one discount code. Applying a second code replaces the first; codes never stack.
- Code kinds: `PERCENT10` takes 10 percent off the subtotal; `FIVEOFF` takes 500 cents off; `FREESHIP` makes shipping cost 0.
- A discount never takes more than 50 percent off the subtotal.
- An unknown code is rejected with a `ValueError`.

## Acceptance

- Subtotal 2000 with `PERCENT10` gives a total of 1800 before shipping.
- Subtotal 800 with `FIVEOFF` gives 400 (capped at 50 percent), not 300.
- `apply_code(cart, "BOGUS")` raises `ValueError`.
- Applying `FIVEOFF` then `PERCENT10` leaves only `PERCENT10` active.

## Exclusions

- Per-customer limits and expiry dates are out of scope.
