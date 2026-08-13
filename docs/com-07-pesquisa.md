# Pesquisa

Pesquisa, no GovHub, é o espaço para explorar soluções ainda experimentais antes de incorporá-las ao pipeline principal.

## O contexto

Algumas ideias precisam ser testadas antes de virarem DAG, modelo dbt, dashboard ou automação oficial. O repositório `govhub-research` existe para esse trabalho exploratório, especialmente em engenharia de dados, IA aplicada, OCR, parsers e integração de bases.

## Como funciona

Uma pesquisa começa como hipótese ou prova de conceito. O resultado pode ser um notebook, script, parser, experimento ou documentação técnica. Quando a abordagem fica madura, ela pode ser proposta para integração no pipeline principal por issue e PR.

| Área | Uso |
| --- | --- |
| IA aplicada | classificação, extração e apoio à análise |
| OCR | leitura de documentos digitalizados |
| Parsers | extração de dados de PDFs, documentos e formatos públicos |
| Integração de bases | cruzamento de dados entre sistemas |

## Por que essa escolha

Separar pesquisa do pipeline principal protege a operação. Experimentos podem falhar, mudar de hipótese e usar amostras antes de virar código produtivo. O que amadurece volta para o GovHub com documentação, validação e revisão.

## Limites e quando não se aplica

Pesquisa não substitui o fluxo de produção. Código que já afeta ingestão, transformação, dashboards ou operação deve seguir os padrões de PR, teste e revisão do repositório correspondente. Dados sensíveis também exigem cuidado desde a fase exploratória.

## Ver também

- [Como Contribuir (fork → branch → PR)](#doc/com-01-como-contribuir)
- [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr)
- [Revisão de PRs](#doc/com-03-revisao-de-prs)

## Origem

Espelho de `docs/documentacao/comunidade/pesquisa.md` em `GovHub-br/gov-hub`, sincronizado localmente em 2026-08-12.
