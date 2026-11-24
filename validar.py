import argparse
import csv
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path


def validate(path: Path) -> dict:
    with path.open(encoding="utf-8-sig", newline="") as source:
        return validate_rows(source)


def validate_rows(source) -> dict:
    report = {"rows": 0, "valid_rows": 0, "errors": []}
    seen = set()
    rows = csv.DictReader(source, strict=True)
    if rows.fieldnames != ["id", "valor"]:
        report["errors"].append({"line": 1, "issue": "expected id,valor header"})
        return report
    for row in rows:
        report["rows"] += 1
        issues = []
        if None in row or None in row.values():
            issues.append("wrong number of columns")
        else:
            identifier = row["id"].strip()
            if not identifier:
                issues.append("missing id")
            elif identifier in seen:
                issues.append("duplicate id")
            if identifier:
                seen.add(identifier)
            try:
                amount = Decimal(row["valor"].strip())
                if not amount.is_finite() or amount < 0:
                    raise InvalidOperation
            except InvalidOperation:
                issues.append("invalid amount")
        if issues:
            report["errors"].extend({"line": rows.line_num, "issue": issue} for issue in issues)
        else:
            report["valid_rows"] += 1
    return report


def main():
    parser = argparse.ArgumentParser(description="Validate a CSV file with id and valor.")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        report = validate(args.path)
    except (OSError, UnicodeError, csv.Error) as error:
        report = {"rows": 0, "valid_rows": 0, "errors": [{"issue": type(error).__name__}]}
    print(json.dumps(report, indent=2))
    return int(bool(report["errors"]))


if __name__ == "__main__":
    raise SystemExit(main())
