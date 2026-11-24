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
| Carteira de ISPs fictícia | Deduplicação por ID, preservação das fontes e total por região. Demonstração independente de prospecção | `python carteira_isp.py` |
| Duelo de robôs modulares | Modelagem, regras de turno e testes. Demonstração independente inspirada na proposta do Meta Botis | `python duelo_modular.py` |

## Como rodar

Python 3.11 a 3.15 como faixa-alvo (3.12 validado localmente) e biblioteca padrão. Execute os comandos na raiz deste repositório. O CSV de exemplo contém erros propositais e deve retornar código 1. Para o catálogo alternativo, use `--colecao urbano`. Os exemplos HTML saem em `saidas/`. Abra `folheto.html` e use **Imprimir → Salvar como PDF**.

```sh
python -m unittest discover -v
python briefing_ia.py validar resposta_exemplo.json
```

Todos os registros desta vitrine são fictícios. Os exemplos HTML abrem offline. O briefing de IA usa uma resposta local de exemplo e fica pronto para copiar em um assistente quando fizer sentido. O validador confere as referências declaradas. A revisão humana confere a interpretação de cada fonte.

## Organização e decisões técnicas

| Fluxo | Regra de negócio | Entrada e saída |
| --- | --- | --- |
| CSV | Campos obrigatórios, identificadores únicos e valores decimais finitos | Adaptador UTF-8 com BOM opcional, relatório JSON e código de saída |
| Conciliação | SQL agrega em centavos, preserva pagamentos órfãos e distingue cinco estados | SQLite em memória com carga transacional, índice e opção JSON |
| Campanha | Soma antes de calcular CPL, com custo indefinido para zero leads | JSON e tabela HTML |
| Catálogo | Seleciona coleção e filtra região sem distinção de maiúsculas | HTML offline com dados escapados |
| Folheto | Reaproveita a seleção e limita a saída ao primeiro imóvel encontrado | Estilos de impressão e mensagem para filtro sem resultado |
| Briefing de IA | Confere formato, IDs conhecidos e unicidade das referências | Resposta de até 16 KiB e rejeição de chaves JSON duplicadas |
| Carteira de ISPs | Consolida por ID, preserva medições e sinaliza regiões conflitantes | Entrada sintética e totais por região |
| Duelo | Valida atributos na criação, com regras e turnos determinísticos | Simulação separada da exibição, com histórico de turnos |

Experimente `python reconciliar.py --json` e `python demonstracoes.py catalogo --colecao litoral --regiao Praia`.

Referências de manutenção [versões do Python](https://devguide.python.org/versions/), [unittest](https://docs.python.org/3/library/unittest.html) e [planejamento de consultas no SQLite](https://www.sqlite.org/queryplanner.html).

## English overview

Eight runnable demos cover CSV validation, SQLite reconciliation, campaign KPIs, catalogue filtering, printable HTML, structured AI output checks, multi-source ISP data and a deterministic game simulation. All records are synthetic. Run `python -m unittest discover -v`.

## Como trabalho

- **Python e SQL.** Validar, deduplicar, reconciliar e documentar um fluxo antes de automatizá-lo.
- **APIs e integrações.** Isolar autenticação, validar payloads, definir timeout e idempotência e manter logs sem segredos.
- **IA aplicada.** Organizar contexto antes do pedido, pedir saída estruturada, conferir fontes e reservar a aprovação de ações externas para uma pessoa. Uso MCP para conectar ferramentas e consultar fontes quando o fluxo exige.
- **Atualização técnica.** Comparar alternativas em documentação e changelogs, prototipar em um exemplo pequeno, medir o resultado e registrar os limites.

[LinkedIn de Kelton Silva](https://www.linkedin.com/in/kelton-silva-cardoso/)
