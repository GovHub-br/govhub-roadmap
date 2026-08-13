# Como Contribuir (fork → branch → PR)

Guia para transformar uma issue do GovHub em um Pull Request revisável, com contexto, validação e rastreabilidade suficientes.

## Quando usar isto

- ao corrigir documentação, código, pipeline, infraestrutura ou automação em um repositório do GovHub;
- ao trabalhar em uma issue já combinada com a equipe;
- ao preparar uma contribuição externa ou de disciplina;
- ao abrir uma melhoria pequena para validação técnica.

## Pré-requisitos

- conta no GitHub;
- acesso ao repositório ou fork do repositório;
- ambiente local configurado quando a mudança exigir teste local;
- issue com contexto, escopo e critérios de aceitação;
- padrão de commit e branch consultado em [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr).

## Passos

1. Abra ou escolha uma issue.
2. Confira se a issue tem título claro, descrição, contexto e critérios de aceitação.
3. Faça fork do repositório quando não tiver push direto no repositório principal.
4. Crie uma branch com o prefixo correto.
5. Faça a alteração mantendo o escopo combinado na issue.
6. Rode as validações aplicáveis: `make lint`, `make test`, testes de DAG, testes dbt ou revisão de documentação.
7. Faça commits no padrão Conventional Commits.
8. Suba a branch para o GitHub.
9. Abra o PR para a `main` do repositório principal.
10. Preencha o template do PR com descrição, issue relacionada, domínio de revisão, validação e evidências.
11. Responda aos comentários de revisão até o PR estar pronto para merge.

## Verificar se deu certo

- o PR aparece aberto no GitHub;
- a issue relacionada está referenciada;
- os checks aplicáveis foram executados ou a ausência foi justificada;
- a descrição permite que uma pessoa revisora entenda o que mudou e como validar;
- o domínio de revisão foi informado no PR ou por label `team:*`, quando o repositório usar esse fluxo.

## Problemas comuns

| Sintoma | Causa provável | O que fazer |
| --- | --- | --- |
| PR sem contexto suficiente | descrição copiada do commit ou muito curta | explique motivação, arquivos principais, validação e issue |
| PR grande demais | escopo da issue ficou amplo | divida em PRs menores ou combine o recorte com a equipe |
| Conflito com `main` | branch ficou desatualizada | atualize a branch com a `main` antes de pedir nova revisão |
| Revisão não foi solicitada | domínio não foi informado | aplique a label `team:*` correta ou solicite revisão manual |
| Testes ausentes | validação não foi registrada | rode o teste aplicável ou registre no PR que não há teste aplicável |

## Ver também

- [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr)
- [Revisão de PRs](#doc/com-03-revisao-de-prs)
- [Criar Fork Temático](#doc/com-04-criar-fork-tematico)

## Origem

Espelho de `docs/documentacao/CONTRIBUTING.md` em `GovHub-br/gov-hub`, sincronizado localmente em 2026-08-12.
