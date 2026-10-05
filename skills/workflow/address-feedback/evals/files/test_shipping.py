from shipping import quote_shipping


def test_minimum_price_applies_to_light_parcels():
    assert quote_shipping(0.5) == 350


def test_price_grows_with_each_half_kilogram():
    assert quote_shipping(2.0) == 480
