import unittest
from carteira_isp import EXAMPLE, build_report
from duelo_modular import Robot, duel


class HistoricalDemosTests(unittest.TestCase):
    def test_aggregation_keeps_all_source_records(self):
        report = build_report(EXAMPLE)
        self.assertEqual(report["por_regiao"]["Norte fictício"]["empresas"], 2)
        self.assertEqual(len(report["empresas"]["ISP-A"]["medicoes"]), 2)

    def test_duel_terminates_and_reports_winner(self):
        a = Robot("A", 3, 3, 1)
        b = Robot("B", 4, 1, 1)
        winner, moves = duel(a, b)
        self.assertEqual(winner, "A")
        self.assertEqual(moves[-1][-1], 0)

    def test_duel_rejects_invalid_hull(self):
        with self.assertRaises(ValueError):
            duel(Robot("A", 0, 3, 1), Robot("B", 4, 1, 1))

    def test_conflicting_regions_require_review(self):
        conflicting = dict(EXAMPLE[0], regiao="Outra região")
        with self.assertRaisesRegex(ValueError, "ISP-A"):
            build_report([EXAMPLE[0], conflicting])

    def test_robot_rejects_non_integer_statistics(self):
        with self.assertRaises(ValueError):
            Robot("A", 3, 1.5, 0)
