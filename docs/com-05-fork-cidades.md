# Fork Cidades

O fork Cidades é a adaptação do pipeline GovHub para integração, qualificação e visualização de dados municipais.

## O contexto

Municípios precisam cruzar informações de fontes diferentes, como indicadores socioeconômicos, convênios, educação, saúde e emprego. O fork Cidades organiza esse trabalho em um repositório próprio, mantendo a base técnica do GovHub e adaptando fontes, modelos e dashboards ao contexto municipal.

## Como funciona

O repositório `data-application-cidades` parte do `data-application-gov-hub` e concentra pipelines voltados a cidades brasileiras. A proposta documentada no site original inclui fontes como IBGE Cidades, SICONV/TransfereGov, FNDE, DataSUS, RAIS/CAGED e MUNIC.

O desenho segue a arquitetura Medallion:

| Camada | Papel |
| --- | --- |
| Bronze | dados brutos de cada fonte municipal |
| Silver | tabelas qualificadas por domínio, como indicadores, transferências, educação e saúde |
| Gold | fatos e dimensões prontos para análise e dashboards |

Os dashboards previstos atendem públicos como prefeituras, secretarias e equipes de gestão de convênios.

## Por que essa escolha

O fork permite reaproveitar padrões do GovHub sem misturar diretamente dados e decisões específicas de municípios com o pipeline federal principal. Isso preserva a estrutura comum, mas dá espaço para cronogramas, fontes e visualizações próprias.

## Limites e quando não se aplica

Nem todo recorte municipal precisa virar fork. Para experimentos pequenos, documentação ou modelos que servem a todos os domínios, é melhor contribuir no repositório base. Se houver exigência forte de isolamento, volume ou SLA, o fork pode não ser suficiente e a equipe deve avaliar infraestrutura separada.

## Ver também

- [Como Contribuir (fork → branch → PR)](#doc/com-01-como-contribuir)
- [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr)
- [Revisão de PRs](#doc/com-03-revisao-de-prs)

## Origem

Espelho de `docs/documentacao/forks/cidades.md` em `GovHub-br/gov-hub`, sincronizado localmente em 2026-08-12.
