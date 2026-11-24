# Kelton Silva • Python, SQL e integração de sistemas

Projetos demonstrativos para vagas remotas em back-end, automação e dados. O fio condutor é o mesmo do meu trabalho profissional: validar dados de entrada, integrar sistemas e tornar o resultado fácil de conferir.

## Projetos executáveis

| Projeto | O que demonstra | Comando |
| --- | --- | --- |
| Validação de CSV | Entrada UTF-8, campos obrigatórios, duplicidade, valores inválidos e saída JSON | `python validar.py exemplo.csv` |
| Conciliação de pedidos | SQLite, CTE, agregação de pagamentos e reconciliação de registros sem vínculo | `python reconciliar.py` |
| Painel de campanha | Métricas por origem, investimento, leads e CPL. Reconstrução demonstrativa do padrão do painel Casa Boris | `python demonstracoes.py campanha` |
| Catálogo de lançamentos | Filtros de catálogo e apresentação acessível. Duas variantes fictícias inspiradas em Lancamentos-LCI e Lancamentos-LC | `python demonstracoes.py catalogo --colecao litoral` |
| Folheto imprimível | Geração de HTML para exportar como PDF pelo navegador. Reconstrução leve do fluxo do Gerador-de-PDF | `python demonstracoes.py folheto` |
| Briefing verificável para IA | Contexto local, referências por ID, contrato de resposta JSON e rejeição de referências desconhecidas | `python briefing_ia.py gerar` |

## Como rodar

Python 3.10+ e biblioteca padrão. Execute os comandos na raiz deste repositório. O CSV de exemplo contém erros propositais e deve retornar código 1. Para o catálogo alternativo, use `--colecao urbano`. Os exemplos HTML saem em `saidas/`. Abra `folheto.html` e use **Imprimir → Salvar como PDF**.

```sh
python -m unittest discover -v
python briefing_ia.py validar resposta_exemplo.json
```

Todos os registros desta vitrine são fictícios. Os exemplos HTML abrem offline. O briefing de IA usa uma resposta local de exemplo e fica pronto para copiar em um assistente quando fizer sentido. O validador confere as referências declaradas. A revisão humana confere a interpretação de cada fonte.

## Como trabalho

- **Python e SQL.** Validar, deduplicar, reconciliar e documentar um fluxo antes de automatizá-lo.
- **APIs e integrações.** Isolar autenticação, validar payloads, definir timeout e idempotência e manter logs sem segredos.
- **IA aplicada.** Organizar contexto antes do pedido, pedir saída estruturada, conferir fontes e reservar a aprovação de ações externas para uma pessoa. Uso MCP para conectar ferramentas e consultar fontes quando o fluxo exige.
- **Atualização técnica.** Comparar alternativas em documentação e changelogs, prototipar em um exemplo pequeno, medir o resultado e registrar os limites.

[LinkedIn de Kelton Silva](https://www.linkedin.com/in/kelton-silva-cardoso/)
