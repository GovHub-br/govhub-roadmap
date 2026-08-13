# Padrões de commit / branch / PR / testes

Referência de consulta rápida das convenções de contribuição do GovHub. Para o passo a passo de uma primeira contribuição, veja [Primeiro PR, passo a passo](#doc/com-09-primeiro-pr).

## Commits

O GovHub adota **Conventional Commits**:

```text
tipo(escopo opcional): descrição
```

| Tipo | Descrição | Uso |
| --- | --- | --- |
| `feat` | funcionalidade nova | adicionar DAG, modelo, integração ou pipeline |
| `fix` | correção | corrigir bug, falha de execução ou inconsistência de dados |
| `docs` | documentação | criar ou atualizar documentação |
| `refactor` | refatoração | reorganizar código sem alterar comportamento esperado |
| `perf` | desempenho | melhorar desempenho sem mudar a regra de negócio |
| `test` | testes | adicionar, corrigir ou reorganizar testes |
| `build` | build | alterar dependências, empacotamento ou configuração de build |
| `ci` | integração contínua | alterar workflows, automações de CI/CD ou validações automatizadas |
| `chore` | manutenção | fazer ajustes operacionais que não alteram código-fonte nem testes |
| `style` | formatação | alterar formatação sem impacto na lógica |

| Regra | Padrão |
| --- | --- |
| Descrição | curta, clara, em minúsculas e sem ponto final |
| Escopo | opcional, entre parênteses: `feat(dbt): ...` |
| Corpo | opcional, separado do título por uma linha em branco |
| Issue | use `Closes #NUMERO` ou `Closes: #NUMERO` quando o commit ou PR fechar uma issue |

Exemplos:

```text
feat(dbt): adiciona modelo gold de execução orçamentária
fix(dag): corrige timeout na ingestão do SIAPE
docs: atualiza guia de variáveis do Airflow
ci: ajusta workflow de revisão por domínio
```

Commits assinados devem ser configurados no ambiente local quando a ruleset do repositório exigir assinatura.

## Branches

| Padrão | Descrição | Uso |
| --- | --- | --- |
| `tipo/descricao-curta` | branch por categoria | formato padrão para mudanças sem issue vinculada no nome |
| `numero-da-issue-tipo-descricao-curta` | branch vinculada a issue | formato recomendado quando a issue deve ficar visível já no nome da branch |

Exemplos:

| Branch | Quando usar |
| --- | --- |
| `feat/integracao-siafi-despesas` | nova funcionalidade ou pipeline |
| `fix/corrigir-modelo-silver-servidores` | correção de bug ou inconsistência |
| `docs/atualizar-dicionario-siape` | mudança apenas documental |
| `149-feat-ingestao-sisbolsas` | branch vinculada à issue 149 |

## Pull requests

| Item | Descrição | Padrão |
| --- | --- | --- |
| Título | identificação do PR | curto, descritivo e no mesmo padrão dos commits |
| Issue | vínculo com demanda | referenciar a issue relacionada, preferencialmente com `Closes #NUMERO` |
| Descrição | resumo e contexto | explicar o que foi feito e qual domínio foi impactado |
| Validação | conferência da mudança | registrar comandos executados, evidências ou justificativa quando não houver teste aplicável |
| Revisão | aprovação antes do merge | solicitar revisão pelo fluxo do repositório |
| Branch base | atualização da contribuição | manter a branch atualizada com `main` antes de concluir o PR |

O template de PR deve ser preenchido com:

| Seção | O que informar |
| --- | --- |
| Descrição | resumo objetivo da mudança e contexto |
| Tipo de mudança | categoria principal: funcionalidade, bug, documentação, infraestrutura ou outro |
| Issues relacionadas | número da issue fechada ou relacionada |
| Domínio de revisão | time ou domínio afetado pela mudança |
| Como testar / validar | comandos, passos ou justificativa |
| Evidências | prints, logs, resultados de consulta ou links úteis |
| Checklist | confirmação dos itens obrigatórios antes da revisão |

PRs devem passar por pelo menos **1 aprovação** antes do merge. Mudanças críticas, sensíveis ou com impacto em produção podem exigir **2 aprovações**, conforme protocolo do repositório.

Quando o repositório usar revisão automática por domínio, aplique a label `team:*` correspondente ao PR:

| Label | Time | Descrição |
| --- | --- | --- |
| `team:ipea` | IPEA | revisão de mudanças do domínio IPEA |
| `team:mir` | MIR | revisão de mudanças do domínio MIR |
| `team:mcid` | MCid | revisão de mudanças do domínio MCid |
| `team:minc` | MinC | revisão de mudanças do domínio MinC |
| `team:gces` | OSS | triagem de contribuições da disciplina GCES |
| `team:oss` | OSS | contribuições externas, governança e colaboração open source |

## Testes

| Tipo | Descrição | Validação esperada |
| --- | --- | --- |
| Código Python | helpers, plugins ou lógica compartilhada | `make lint` e `make test` |
| DAG Airflow | orquestração ou ingestão | `airflow dags test NOME_DA_DAG DATA_EXECUCAO` |
| Modelo dbt | transformação, teste ou documentação dbt | `dbt run --select MODELO` e `dbt test --select MODELO` dentro do projeto dbt |
| Documentação | páginas, guias, referências ou README | revisão de links, formatação, navegação e ortografia |
| CI/CD ou infraestrutura | workflows, deploy, containers ou ambiente | validação do workflow, plano, diff ou ambiente afetado |

Quando um teste não se aplicar, registre a justificativa no PR. A ausência de teste deve ser explícita, não implícita.

## Checklist rápido

| Antes do PR | Conferir |
| --- | --- |
| Branch | criada a partir da `main` atualizada |
| Commits | seguem Conventional Commits |
| Segurança | nenhum segredo, token, `.env` real ou credencial foi commitado |
| Testes | comandos aplicáveis foram executados ou justificados |
| Documentação | atualizada quando a mudança altera uso, operação ou arquitetura |
| Revisão | domínio correto indicado no PR ou por label `team:*` |

## Ver também

- [Primeiro PR, passo a passo](#doc/com-09-primeiro-pr)
- [Como Contribuir (fork → branch → PR)](#doc/com-01-como-contribuir)
- [Revisão de PRs](#doc/com-03-revisao-de-prs)
- Protocolo de PR — `gov-hub.io/documentacao/pipeline/protocolo-mr/`
- Git Workflow — `gov-hub.io/documentacao/onboarding/git-workflow/`

## Origem

Consolidado a partir de:

- `docs/documentacao/CONTRIBUTING.md` em `GovHub-br/gov-hub`
- `docs/documentacao/onboarding/git-workflow.md` em `GovHub-br/gov-hub`
- `docs/documentacao/pipeline/protocolo-mr.md` em `GovHub-br/gov-hub`
- `.github/MERGE_REQUEST_PROTOCOL.md` em `GovHub-br/data-application-gov-hub`
- `.github/PULL_REQUEST_TEMPLATE.md` em `GovHub-br/data-application-gov-hub`
