"""Invoice totals. All amounts are integer cents."""


def line_total(price_cents, quantity, discount_percent):
    """Total for one line, discount applied."""
    return round(price_cents * quantity * (1 - discount_percent / 100))


def display_total(lines):
    """The total shown on screen: discount every line, then round once."""
    exact = sum(
        line["price_cents"] * line["quantity"] * (1 - line["discount_percent"] / 100)
        for line in lines
    )
    return round(exact)


def export_total(lines):
    """The total written to the CSV export: sum of rounded line totals."""
    return sum(
        line_total(line["price_cents"], line["quantity"], line["discount_percent"])
        for line in lines
    )
