import sqlite3
from contextlib import closing
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def reconcile(database):
    query = (ROOT / "conciliacao.sql").read_text(encoding="utf-8")
    return database.execute(query).fetchall()


def main():
    with closing(sqlite3.connect(":memory:")) as database:
        database.executescript((ROOT / "exemplo.sql").read_text(encoding="utf-8"))
        print("pedido | esperado | pago | situação")
        for row in reconcile(database):
            print(" | ".join(map(str, row)))


if __name__ == "__main__":
    main()
