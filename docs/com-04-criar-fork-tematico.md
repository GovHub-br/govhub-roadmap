# Criar Fork Temático

Guia para criar uma nova instância temática do pipeline GovHub a partir do projeto base.

## Quando usar isto

- quando um novo domínio de dados precisa de fontes, dashboards ou equipe próprios;
- quando um ministério, órgão, estado ou município precisa de recorte específico;
- quando a prova de conceito deve evoluir isolada antes de voltar ao pipeline base;
- quando requisitos de compliance, volume ou SLA exigirem isolamento maior.

## Pré-requisitos

- entendimento da arquitetura Medallion do GovHub;
- repositório base identificado;
- decisão sobre isolamento de dados e infraestrutura;
- fontes de dados e responsáveis mapeados;
- permissão para criar repositório ou fork na organização.

## Passos

1. Confirme se o caso realmente exige fork temático.
2. Crie o fork a partir de `data-application-gov-hub`.
3. Nomeie o repositório no formato `data-application-<contexto>`.
4. Clone o novo repositório.
5. Adicione o repositório base como `upstream`.
6. Defina schemas, buckets ou prefixos próprios para o contexto.
7. Crie DAGs de ingestão em caminhos coerentes com a fonte.
8. Crie modelos dbt nas camadas Bronze, Silver e Gold.
9. Adicione testes dbt nas tabelas Silver e Gold.
10. Crie ou exporte dashboards no local versionado pelo fork.
11. Documente fontes, execução local, dashboards e decisões específicas do fork.
12. Mantenha a sincronização periódica com o pipeline base.

## Verificar se deu certo

- o fork existe e aponta para o repositório base por `upstream`;
- o ambiente local sobe sem erro;
- DAGs e modelos dbt rodam no contexto do fork;
- os dados ficam isolados por schema, bucket ou prefixo definido;
- o README do fork explica contexto, fontes, execução e dashboards;
- melhorias genéricas podem voltar ao repositório base por PR.

## Problemas comuns

| Sintoma | Causa provável | O que fazer |
| --- | --- | --- |
| Fork diverge rápido do base | sincronização não foi combinada | mantenha rotina de merge do `upstream/main` |
| Dados misturados entre contextos | schemas ou buckets compartilhados sem separação | defina prefixos e schemas próprios |
| Código genérico fica preso no fork | melhoria não voltou ao base | abra PR upstream para padrões reutilizáveis |
| Dashboard não é reprodutível | export não foi versionado | salve dashboards no local definido pelo fork |
| Testes dbt ausentes | camada foi criada sem contrato mínimo | adicione testes em Silver e Gold |

## Ver também

- [Como Contribuir (fork → branch → PR)](#doc/com-01-como-contribuir)
- [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr)
- [Revisão de PRs](#doc/com-03-revisao-de-prs)

## Origem

Espelho de `docs/documentacao/forks/guia-criar-fork.md` em `GovHub-br/gov-hub`, sincronizado localmente em 2026-08-12.
