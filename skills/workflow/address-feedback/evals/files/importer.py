"""Imports archived order files. Archives from before 2019 use day/month/year."""

from dates import parse_date


def import_row(row: dict) -> dict:
    return {"order_id": row["id"], "placed_on": parse_date(row["placed"])}
