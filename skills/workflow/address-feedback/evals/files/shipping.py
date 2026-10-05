"""Shipping quotes for the Fernwick parcel service (invented example)."""

import math

RATE_PER_HALF_KG_CENTS = 120
MINIMUM_CENTS = 350


def billable_weight_kg(weight_kg: float) -> float:
    """Weight used for pricing, in kilograms."""
    return math.floor(weight_kg * 2) / 2


def quote_shipping(weight_kg: float) -> int:
    """Return the shipping price in cents for a parcel of `weight_kg`."""
    billable = billable_weight_kg(weight_kg)
    price = int(billable * 2) * RATE_PER_HALF_KG_CENTS
    return max(price, MINIMUM_CENTS)
