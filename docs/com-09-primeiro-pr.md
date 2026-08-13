# Primeiro PR, passo a passo

Ao final deste tutorial você vai ter uma contribuição pequena aberta como Pull Request no GovHub.

Público: pessoa contribuindo pela primeira vez no GovHub. Este é um **tutorial**: siga o caminho em ordem. Para consulta rápida de regras, veja [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr).

## Antes de começar

- Conta no GitHub.
- Git configurado na máquina.
- Issue escolhida ou combinada com a equipe.
- Repositório alvo definido.
- Ambiente local configurado quando a mudança exigir teste local.

## 1. Escolha uma tarefa pequena

Escolha uma issue com escopo claro. Para o primeiro PR, prefira documentação, ajuste pequeno, teste faltante ou correção simples.

Confira se a issue tem:

- título claro;
- descrição do problema ou melhoria;
- critérios de aceitação;
- repositório correto.

## 2. Faça o fork e clone

No GitHub, abra o repositório alvo e clique em **Fork**.

Depois clone o seu fork:

```bash
git clone git@github.com:<seu-usuario>/<repositorio>.git
cd <repositorio>
```

Adicione o repositório principal como `upstream`:

```bash
git remote add upstream git@github.com:GovHub-br/<repositorio>.git
git fetch upstream
```

## 3. Crie a branch

Atualize sua branch local a partir da `main` do repositório principal:

```bash
git checkout main
git pull upstream main
```

Crie uma branch seguindo o padrão do projeto:

```bash
git checkout -b docs/minha-primeira-contribuicao
```

Use `docs/`, `feat/`, `fix/` ou `refactor/` conforme o tipo da mudança.

## 4. Faça a mudança

Edite apenas o necessário para cumprir a issue. Evite aproveitar o PR para refatorações ou ajustes fora do escopo.

Depois confira o diff:

```bash
git diff
```

## 5. Valide

Rode as validações aplicáveis ao repositório.

Para documentação, confira links, formatação e navegação. Para repositórios com Makefile, use os comandos indicados no próprio projeto, como:

```bash
make lint
make test
```

Se um teste não se aplicar, anote a justificativa no PR.

## 6. Faça o commit

Adicione os arquivos alterados:

```bash
git add <arquivos>
```

Crie o commit no padrão Conventional Commits:

```bash
git commit -m "docs: ajusta primeira contribuicao"
```

Se a ruleset do repositório exigir assinatura, configure GPG antes de commitar.

## 7. Envie a branch

```bash
git push --set-upstream origin docs/minha-primeira-contribuicao
```

## 8. Abra o Pull Request

No GitHub, abra o PR do seu fork para a `main` do repositório principal.

Preencha o template com:

- descrição do que mudou;
- issue relacionada;
- tipo de mudança;
- como validar;
- evidências, quando houver;
- domínio de revisão ou label `team:*`, quando o repositório usar revisão por domínio.

## 9. Responda à revisão

Leia os comentários com calma. Quando precisar alterar algo:

```bash
git add <arquivos>
git commit -m "fix: ajusta revisao do pr"
git push
```

O PR será atualizado automaticamente.

## 10. Depois do merge

Depois que o PR for mergeado, sincronize seu fork:

```bash
git checkout main
git pull upstream main
git push origin main
```

Apague a branch se ela não for mais usada.

## Verificar que funcionou

Você terminou este tutorial quando:

- o PR está aberto ou foi mergeado;
- a issue está referenciada;
- o template do PR está preenchido;
- os testes aplicáveis foram registrados;
- a revisão foi respondida no próprio PR.

## O que você aprendeu

Você atravessou o fluxo básico de contribuição do GovHub: issue, fork, branch, mudança pequena, validação, commit, PR e revisão.

## Próximos passos

- [Como Contribuir (fork → branch → PR)](#doc/com-01-como-contribuir)
- [Revisão de PRs](#doc/com-03-revisao-de-prs)
- [Padrões de commit / branch / PR / testes](#doc/com-02-padroes-commit-pr)

## Origem

Consolidado a partir de `docs/documentacao/CONTRIBUTING.md` e `docs/documentacao/onboarding/git-workflow.md` em `GovHub-br/gov-hub`, sincronizado localmente em 2026-08-12.
