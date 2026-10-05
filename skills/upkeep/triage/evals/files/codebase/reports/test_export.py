import tempfile
import unittest
from types import SimpleNamespace

from export import export_csv


class ExportTests(unittest.TestCase):
    def test_writes_header_and_rows(self):
        report = SimpleNamespace(rows=[{"id": 1, "total": 5}])
        with tempfile.NamedTemporaryFile("r", suffix=".csv") as handle:
            export_csv(report, handle.name)
            self.assertEqual(handle.read().splitlines(), ["id,total", "1,5"])


if __name__ == "__main__":
    unittest.main()
