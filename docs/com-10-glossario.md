# Glossário do GovHub

Referência rápida dos termos usados nos documentos de comunidade, contribuição e operação do GovHub.

## Termos

| Termo | Significado |
| --- | --- |
| GovHub | Iniciativa para transformar dados governamentais em ativos estratégicos para gestão pública. |
| Contribuidor | Pessoa que propõe mudanças em código, documentação, dados, infraestrutura, pesquisa ou governança. |
| Issue | Registro rastreável de problema, melhoria ou tarefa a ser realizada. |
| Pull Request ou PR | Proposta de mudança submetida para revisão antes de entrar na branch principal. |
| Branch | Linha de trabalho usada para desenvolver uma mudança sem alterar diretamente a `main`. |
| Conventional Commits | Padrão de mensagens de commit no formato `tipo(escopo): descrição`. |
| Code Owners | Pessoas ou times responsáveis por revisar mudanças em áreas específicas, quando o repositório usa esse recurso. |
| Ruleset | Regra de proteção configurada no GitHub para exigir PR, aprovação, checks ou restrições na branch principal. |
| Revisão por domínio | Fluxo em que uma label `team:*` ou regra do repositório direciona revisão para o time responsável. |
| Fork temático | Adaptação do pipeline GovHub para um contexto específico, como Cidades ou MinC. |
| Pipeline | Fluxo de ingestão, transformação e disponibilização de dados. |
| DAG | Grafo de tarefas do Airflow usado para orquestrar uma rotina de dados. |
| dbt | Ferramenta usada para transformar e testar modelos analíticos. |
| Medallion | Arquitetura em camadas Bronze, Silver e Gold. |
| Bronze | Camada de dados brutos ou próximos da origem. |
| Silver | Camada de dados limpos, normalizados e qualificados. |
| Gold | Camada de dados agregados, fatos e dimensões prontos para consumo. |
| Superset | Ferramenta de BI usada para dashboards. |
| JupyterHub | Ambiente de notebooks para análise interativa e pesquisa. |
| OpenMetadata | Ferramenta de catálogo, linhagem e governança de dados. |
| Trino + Ranger | Caminho governado para consulta a dados sensíveis, quando habilitado. |
| OSS | Contribuições externas e governança open source do projeto. |

## Ver também

- [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr)
- [Mapa dos repositórios](#doc/com-11-mapa-dos-repositorios)
- [Arquitetura Medallion](#doc/arch-03-arquitetura-medallion)

## Origem

Consolidado a partir dos documentos já migrados neste roadmap e de `docs/documentacao/CONTRIBUTING.md` em `GovHub-br/gov-hub`, sincronizado localmente em 2026-08-12.
