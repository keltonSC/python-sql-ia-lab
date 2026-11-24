import argparse
import json
from decimal import Decimal
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def campaign(rows):
    totals = {}
    for row in rows:
        combined = totals.setdefault(row["canal"], [0, 0])
        combined[0] += row["centavos"]
        combined[1] += row["leads"]
    return [(name, cents, leads, Decimal(cents) / 100 / leads if leads else None)
            for name, (cents, leads) in sorted(totals.items())]


def currency(cents):
    return f"R$ {Decimal(cents) / 100:.2f}"


def table(headers, rows):
    headings = "".join(f'<th scope="col">{escape(str(value))}</th>' for value in headers)
    body = "".join("<tr>" + "".join(f"<td>{escape(str(value))}</td>" for value in row)
                   + "</tr>" for row in rows)
    return f"<table><thead><tr>{headings}</tr></thead><tbody>{body}</tbody></table>"


def render_page(title, markup):
    return f'''<!doctype html>
<html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title><style>
body {{max-width: 48rem; margin: 3rem auto; padding: 0 1rem; font: 1rem/1.55 system-ui; color: #132c36}}
th, td {{text-align: left; padding: .65rem; border-bottom: 1px solid #cedbdc}}
table {{border-collapse: collapse; width: 100%}}
@media print {{body {{margin: 1rem auto}}}}
</style><main><h1>{escape(title)}</h1><p>Dados fictícios para demonstração.</p>{markup}</main></html>'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("demo", choices=["campanha", "catalogo", "folheto"])
    parser.add_argument("--colecao", choices=["litoral", "urbano"], default="litoral")
    parser.add_argument("--saida", type=Path, default=ROOT / "saidas")
    args = parser.parse_args()
    fixtures = json.loads((ROOT / "dados_ficticios.json").read_text(encoding="utf-8"))
    if args.demo == "campanha":
        header = ["Canal", "Investimento", "Leads", "CPL"]
        rows = [(channel, currency(cents), leads, f"R$ {cpl:.2f}" if cpl is not None else "—")
                for channel, cents, leads, cpl in campaign(fixtures["campanhas"])]
        title = "Painel de campanha"
    else:
        listings = fixtures["catalogo"][args.colecao]
        rows = [(x["nome"], x["regiao"], f"{x['area_m2']} m²") for x in listings]
        if args.demo == "folheto":
            rows = rows[:1]
        title = "Folheto de imóvel" if args.demo == "folheto" else "Catálogo de lançamentos"
        header = ["Empreendimento", "Região", "Área"]
    args.saida.mkdir(parents=True, exist_ok=True)
    path = args.saida / f"{args.demo}.html"
    path.write_text(render_page(title, table(header, rows)), encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()
