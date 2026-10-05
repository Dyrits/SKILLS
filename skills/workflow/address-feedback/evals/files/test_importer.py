from importer import import_row


def test_archived_row_with_legacy_date_is_imported():
    row = {"id": "A-17", "placed": "03/04/2018"}
    assert import_row(row)["placed_on"].isoformat() == "2018-04-03"
