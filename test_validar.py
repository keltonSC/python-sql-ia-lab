import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from validar import validate


class CsvValidationTests(unittest.TestCase):
    def check_text(self, source):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "file.csv"
            path.write_text(source, encoding="utf-8-sig")
            return validate(path)

    def test_valid_bom_file(self):
        self.assertEqual(self.check_text("id,valor\nA,0\n")["valid_rows"], 1)

    def test_invalid_header(self):
        self.assertEqual(self.check_text("name,valor\n")["errors"][0]["line"], 1)

    def test_duplicate_invalid_and_extra_fields(self):
        result = self.check_text("id,valor\nA,1\nA,-2\nB,NaN\nC,5,extra\n")
        self.assertEqual(result["valid_rows"], 1)
        self.assertEqual([item["line"] for item in result["errors"]], [3, 3, 4, 5])
