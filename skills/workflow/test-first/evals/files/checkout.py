"""Brightcart checkout (invented example)."""

from datetime import date

COUPONS = {"SAVE10": {"percent": 10, "expires": date(2026, 1, 31)}}


class CouponExpiredError(Exception):
    pass


def apply_coupon(cart_total_cents: int, code: str, today: date) -> int:
    coupon = COUPONS[code]
    return cart_total_cents - cart_total_cents * coupon["percent"] // 100
