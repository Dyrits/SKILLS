# Coupons (Brightcart, invented example)

## Agreed behavior (approved)

- `apply_coupon(cart, code)` returns the cart total in cents after the coupon.
- Coupon `SAVE10` takes 10 percent off the cart total, with the discount rounded down to whole cents.
- An expired coupon is rejected with `CouponExpiredError`.

## Unresolved proposals (not agreed)

- Coupons might stack with loyalty points.
- A coupon might apply only to selected categories.
