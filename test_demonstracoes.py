import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from briefing_ia import MAX_RESPONSE_BYTES, load_data, parse_response, validate
from demonstracoes import campaign, listing_rows, table


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

    def test_catalogue_region_filter(self):
        listings = load_data("dados_ficticios.json")["catalogo"]["litoral"]
        self.assertEqual(len(listing_rows(listings, "PRAIA")), 1)
        self.assertEqual(listing_rows(listings, "inexistente"), [])

    def test_large_and_ambiguous_ai_responses_are_rejected(self):
        with TemporaryDirectory() as directory:
            response = Path(directory) / "response.json"
            for payload in (b" " * (MAX_RESPONSE_BYTES + 1), b'{"resumo": 1, "resumo": 2}'):
                with self.subTest(size=len(payload)):
                    response.write_bytes(payload)
                    with self.assertRaises(ValueError):
                        parse_response(response)
