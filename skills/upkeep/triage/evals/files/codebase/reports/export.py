import csv


def export_csv(report, path):
    """Write a report's rows to a CSV file with a header row."""
    with open(path, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(report.rows[0].keys()))
        writer.writeheader()
        writer.writerows(report.rows)
