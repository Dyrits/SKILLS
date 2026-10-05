"""Date parsing for the Fernwick importer (invented example)."""

from datetime import date, datetime


def parse_date(text: str) -> date:
    """Parse an ISO date; fall back to the legacy day/month/year format."""
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        return datetime.strptime(text, "%d/%m/%Y").date()
