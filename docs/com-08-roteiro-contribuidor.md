# Roteiro do Contribuidor

O roteiro do contribuidor organiza a chegada de uma pessoa nova ao GovHub: primeiro ambiente e contexto, depois uma contribuição pequena e revisada.

## O contexto

O GovHub combina engenharia de dados, documentação, infraestrutura, visualização e governança. Sem um roteiro, quem chega tende a pular direto para uma tarefa grande, sem conhecer arquitetura, padrões de contribuição e fluxo de revisão.

## Como funciona

O roteiro original separa a entrada em dois momentos:

| Momento | Foco |
| --- | --- |
| Primeiro dia | ler o README, configurar ambiente, conhecer repositórios, entender a arquitetura geral e escolher a primeira atividade com o time |
| Primeira semana | estudar arquitetura Medallion, consultar tutoriais da área, configurar Git, ler padrões de engenharia e abrir um PR pequeno |

As trilhas ajudam a orientar o caminho conforme o papel da pessoa:

| Trilha | Foco |
| --- | --- |
| Pipeline | Airflow e dbt |
| Visualização | Superset |
| Infra | Kubernetes e Argo CD |
| Pesquisa | IA, OCR e parsers |

## Por que essa escolha

O primeiro PR deve ensinar o fluxo completo de colaboração, não resolver o problema mais difícil do projeto. Separar onboarding por trilhas evita sobrecarregar quem chega e deixa claro onde buscar a documentação certa.

## Limites e quando não se aplica

O roteiro não substitui acompanhamento humano. A primeira atividade ainda precisa ser combinada com a equipe, principalmente quando envolve credenciais, dados sensíveis, produção ou decisões de arquitetura.

## Ver também

- [Como Contribuir (fork → branch → PR)](#doc/com-01-como-contribuir)
- [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr)
- [Revisão de PRs](#doc/com-03-revisao-de-prs)

## Origem

Espelho de `docs/documentacao/onboarding/roteiro.md` em `GovHub-br/gov-hub`, sincronizado localmente em 2026-08-12.
