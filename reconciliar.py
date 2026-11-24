import argparse
import json
import sqlite3
from contextlib import closing
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def reconcile(database):
    query = (ROOT / "conciliacao.sql").read_text(encoding="utf-8")
    return database.execute(query).fetchall()


def demo_report() -> list[tuple]:
    with closing(sqlite3.connect(":memory:")) as database:
        with database:
            database.executescript("BEGIN;\n" + (ROOT / "exemplo.sql").read_text(encoding="utf-8"))
            return reconcile(database)


def main():
    parser = argparse.ArgumentParser(description="Reconcile the bundled fictional orders.")
    parser.add_argument("--json", action="store_true", help="Return a structured report.")
    args = parser.parse_args()
    rows = demo_report()
    if args.json:
        keys = ("pedido", "esperado_centavos", "pago_centavos", "situacao")
        print(json.dumps([dict(zip(keys, row)) for row in rows], indent=2))
        return
    print("pedido | esperado | pago | situação")
    for row in rows:
        print(" | ".join(map(str, row)))


if __name__ == "__main__":
    main()
