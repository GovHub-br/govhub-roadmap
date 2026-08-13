# Fork MinC

O fork MinC é a adaptação do pipeline GovHub para dados do Ministério da Cultura.

## O contexto

Políticas culturais dependem de dados de fomento, patrimônio, espaços, agentes e projetos culturais. O fork MinC concentra esse recorte em um repositório próprio, sem perder a arquitetura e as práticas compartilhadas do GovHub.

## Como funciona

O repositório `data-application-minc` parte do `data-application-gov-hub` e adapta o pipeline para fontes ligadas à cultura. A proposta documentada no site original cita fontes como SALIC, MapaCultural, SNIIC, IBGE MUNIC Cultura, IPHAN e Funarte.

O desenho segue a arquitetura Medallion:

| Camada | Papel |
| --- | --- |
| Bronze | dados brutos das fontes culturais |
| Silver | entidades qualificadas, como projetos, espaços culturais, indicadores e patrimônio |
| Gold | fatos e dimensões para análise de fomento, patrimônio e distribuição territorial |

Os dashboards previstos apoiam gestão do MinC, sociedade civil, IPHAN e equipes de acompanhamento de investimento cultural.

## Por que essa escolha

O fork separa o domínio cultural sem criar um projeto completamente novo. Assim, o MinC herda práticas de ingestão, dbt, testes, documentação e operação do GovHub, enquanto mantém fontes e dashboards próprios.

## Limites e quando não se aplica

Padrões reutilizáveis não devem ficar presos ao fork. Skills gerais, helpers, protocolos e melhorias de engenharia devem voltar para os repositórios centrais quando servirem a mais de um domínio. O fork deve guardar apenas o que for específico do contexto MinC.

## Ver também

- [Como Contribuir (fork → branch → PR)](#doc/com-01-como-contribuir)
- [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr)
- [Revisão de PRs](#doc/com-03-revisao-de-prs)

## Origem

Espelho de `docs/documentacao/forks/minc.md` em `GovHub-br/gov-hub`, sincronizado localmente em 2026-08-12.
