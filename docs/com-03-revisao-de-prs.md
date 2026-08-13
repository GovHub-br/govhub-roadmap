# Revisão de PRs

Guia para revisar Pull Requests do GovHub com critérios claros de qualidade, segurança e rastreabilidade.

## Quando usar isto

- ao revisar PRs de código, dados, documentação, infraestrutura ou automação;
- ao validar se um PR pode ser integrado na `main`;
- ao conferir se o domínio correto foi chamado para revisão;
- ao lidar com mudanças sensíveis, urgentes ou com impacto em produção.

## Pré-requisitos

- PR aberto e com descrição preenchida;
- issue relacionada, quando houver;
- checks, testes ou justificativas visíveis no PR;
- domínio de revisão identificado;
- regras do repositório consultadas em [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr).

## Passos

1. Leia a issue relacionada e a descrição do PR.
2. Confira se a mudança está dentro do escopo combinado.
3. Verifique se a branch está sem conflito com a `main`.
4. Confira os checks obrigatórios e os testes informados.
5. Revise o código, a documentação ou a configuração alterada.
6. Procure exposição de segredos, dados pessoais, credenciais ou exemplos sensíveis.
7. Verifique se DAGs, modelos dbt, documentação e infraestrutura seguem os padrões do projeto.
8. Use comentários objetivos para pedir correções.
9. Use sugestão quando for preferência de estilo e request changes quando houver bloqueio real.
10. Aprove apenas quando os problemas bloqueantes estiverem resolvidos.

## Verificar se deu certo

- o PR tem pelo menos uma aprovação exigida pela ruleset;
- os comentários bloqueantes foram resolvidos;
- os checks obrigatórios estão verdes ou justificados;
- não há request changes pendente;
- o domínio correto revisou ou justificou a não necessidade.

## Problemas comuns

| Sintoma | Causa provável | O que fazer |
| --- | --- | --- |
| Review pedido ao time errado | label ou domínio incorreto | ajuste a label `team:*` ou solicite revisão manual do time correto |
| PR aprovado sem teste | validação não foi exigida | peça execução ou justificativa explícita |
| Discussão se perde fora do PR | decisões feitas em chat externo | registre no PR o resumo da decisão |
| Mudança urgente sem contexto | pressão por merge rápido | peça motivo da urgência e evidência mínima de validação |
| Segredo aparece no diff | credencial commitada | bloqueie o merge e acione rotação ou revogação do segredo |

## Ver também

- [Como Contribuir (fork → branch → PR)](#doc/com-01-como-contribuir)
- [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr)
- [Criar Fork Temático](#doc/com-04-criar-fork-tematico)

## Origem

Espelho de `docs/documentacao/pipeline/protocolo-mr.md` em `GovHub-br/gov-hub`, sincronizado localmente em 2026-08-12.
