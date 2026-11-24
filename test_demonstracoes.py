import unittest

from briefing_ia import load_data, validate
from demonstracoes import campaign, table


class DemonstrationTests(unittest.TestCase):
    def test_campaign_groups_channels_and_keeps_undefined_cpl(self):
        rows = campaign(load_data("dados_ficticios.json")["campanhas"])
        self.assertEqual(rows[0], ("Busca", 52500, 25, 21))
        self.assertEqual(rows[1], ("Portal", 10000, 0, None))

    def test_table_escapes_text(self):
        self.assertIn("&lt;teste&gt;", table(["Coluna"], [("<teste>",)]))
        self.assertNotIn("<teste>", table(["Coluna"], [("<teste>",)]))

    def test_sample_brief_has_valid_sources(self):
        validate(load_data("resposta_exemplo.json"), load_data("fontes_exemplo.json"))

    def test_unknown_source_is_rejected(self):
        with self.assertRaises(ValueError):
            validate({"resumo": "Teste", "fontes": ["F99"]}, load_data("fontes_exemplo.json"))
