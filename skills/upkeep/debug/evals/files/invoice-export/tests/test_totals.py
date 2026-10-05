from src.totals import display_total, export_total


def test_totals_match_without_discount():
    lines = [{"price_cents": 500, "quantity": 2, "discount_percent": 0}]
    assert display_total(lines) == export_total(lines) == 1000


def test_totals_match_for_whole_cent_discount():
    lines = [{"price_cents": 1000, "quantity": 1, "discount_percent": 10}]
    assert display_total(lines) == export_total(lines) == 900
