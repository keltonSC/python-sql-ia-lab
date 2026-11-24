import json

EXAMPLE = (
    {"id": "ISP-A", "regiao": "Norte fictício", "acessos": 1200, "origem": "Cadastro demo"},
    {"id": "ISP-B", "regiao": "Sul fictício", "acessos": 4800, "origem": "Cadastro demo"},
    {"id": "ISP-A", "regiao": "Norte fictício", "acessos": 1250, "origem": "Pesquisa demo"},
    {"id": "ISP-C", "regiao": "Norte fictício", "acessos": 0, "origem": "Pesquisa demo"},
)


def build_report(records):
    companies = {}
    for row in records:
        company = companies.setdefault(row["id"], {"regiao": row["regiao"], "medicoes": []})
        company["medicoes"].append({"origem": row["origem"], "acessos": row["acessos"]})
    regions = {}
    for company in companies.values():
        total = regions.setdefault(company["regiao"], {"empresas": 0})
        total["empresas"] += 1
    return {"empresas": companies, "por_regiao": regions}


if __name__ == "__main__":
    print(json.dumps(build_report(EXAMPLE), ensure_ascii=False, indent=2))
