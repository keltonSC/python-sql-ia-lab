import sqlite3
import unittest
from contextlib import closing
from reconciliar import ROOT, reconcile


class ReconciliationTests(unittest.TestCase):
    def test_totals_and_all_statuses(self):
        with closing(sqlite3.connect(":memory:")) as database:
            database.executescript((ROOT / "exemplo.sql").read_text(encoding="utf-8"))
            self.assertEqual(reconcile(database), [
                ("A01", 10000, 10000, "pago"),
                ("A02", 8000, 1000, "parcial"),
                ("A03", 6000, 0, "sem pagamento"),
                ("A04", 5000, 5500, "excesso"),
                ("A05", 0, 3500, "pagamento sem pedido"),
            ])
