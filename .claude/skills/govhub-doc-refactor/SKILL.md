---
name: govhub-doc-refactor
description: Use quando um documento específico do govhub-roadmap precisar ser refatorado, reescrito, atualizado, dividido ou fundido — inclusive quando a atualização vier de um espelho de outro repositório da organização GovHub-br, quando o documento misturar tipos Diátaxis, ou quando o tipo declarado no box não corresponder ao conteúdo.
---

# Refatorar um documento do GovHub

Escrever do zero é a skill **govhub-doc-writer**. Esta aqui é para quando o
documento **já existe** e está errado: mistura tipos, envelheceu em relação à
fonte, duplica outro, ou o box declara um tipo que o conteúdo não sustenta.

## A regra que não se negocia

**Não invente conteúdo técnico, e não descarte conteúdo sem destino.**

Refatorar não é reescrever de memória. Todo parágrafo do documento antigo ou
sobrevive, ou vai para outro documento, ou é removido por uma razão que você diz
em voz alta. Conteúdo que some no meio de uma refatoração é a forma mais fácil
de destruir documentação — ninguém percebe até precisar dele.

| Racionalização | Realidade |
|---|---|
| "Essa seção estava confusa, tirei" | Confusa ≠ errada. Mova, não apague. |
| "Reescrevi mais claro do zero" | Sem a fonte na frente, "mais claro" vira "inventado". |
| "O conteúdo antigo estava desatualizado" | Então diga o que substituiu, e por qual fonte. |
| "Dá pra recuperar no git" | Ninguém vai no git procurar o que não sabe que existiu. |
| "É só reorganizar, não muda nada" | Reorganizar muda o que o leitor acha. Verifique os links. |

## Fluxo

### 1. Identificar o arquivo

Aceite qualquer referência do usuário — slug, caminho, id do box ou o título:

```bash
python3 .claude/skills/govhub-doc-refactor/scripts/diagnosticar.py <slug|caminho|id>
```

Resolve sozinho e já diagnostica. Se a referência for ambígua, o script lista os
candidatos. Se o usuário não souber qual arquivo, varra tudo:

```bash
python3 .claude/skills/govhub-doc-refactor/scripts/diagnosticar.py --todos
```

### 2. Ler o diagnóstico junto com o documento

O script aponta sinais (passos numerados, tabela de parâmetros, justificativa) e
sinaliza combinações que denunciam mistura de tipos. **Ele é uma heurística.**
Leia o arquivo antes de aceitar o veredito — e antes de descartá-lo.

Confira também:

- o **tipo declarado** no box bate com o conteúdo?
- há **tag de estado** (`lacuna`, `dup`, `rascunho`) dizendo o que já se sabia?
- existe seção **Origem**? Se não, a procedência vai ser estabelecida agora.

### 3. Perguntar a origem da atualização

Pergunte antes de escrever qualquer coisa. Use AskUserQuestion com as opções que
se aplicarem:

| Origem | O que fazer |
|---|---|
| **Espelho de outro repo da organização** | Passo 4 |
| Página atual do gov-hub.io | É o repo `gov-hub`; use o passo 4 também |
| Código do repo da aplicação | Leia o código; cite arquivo e linha |
| O usuário vai ditar | Escreva o que ele disser, nada além |
| Não tem fonte | O conteúdo novo fica `*a escrever*` |

Nunca assuma a origem. Um documento que parece desatualizado pode estar certo e
o site é que está velho.

### 4. Se for espelho: buscar, comparar, registrar

```bash
python3 .claude/skills/govhub-doc-refactor/scripts/espelho.py <slug>
python3 .claude/skills/govhub-doc-refactor/scripts/espelho.py <slug> --diff
python3 .claude/skills/govhub-doc-refactor/scripts/espelho.py <slug> --repo data-application-gov-hub --path README.md
```

Sem `--repo`, ele resolve pela URL do gov-hub.io declarada no documento e busca
em `GovHub-br/gov-hub`. Repositórios e o que cada um alimenta estão em
`references/repos-da-organizacao.md`.

**Toda refatoração vinda de espelho registra a procedência** no rodapé do `.md`:

```markdown
## Origem

Espelho de [`docs/documentacao/adocao/requisitos.md`](https://github.com/GovHub-br/gov-hub/blob/main/docs/documentacao/adocao/requisitos.md)
em `GovHub-br/gov-hub`, sincronizado em 2026-07-28 (commit `a1b2c3d`).
```

Sem isso a próxima pessoa não sabe de onde re-sincronizar, e o documento vira
uma cópia órfã que diverge em silêncio. O `espelho.py` imprime esse bloco pronto.

### 5. Decidir o plano, e dizer o plano

Antes de editar, diga em uma frase o que vai acontecer com o documento. Os casos:

| Situação | Plano |
|---|---|
| Mistura tipos | Divide: o principal fica, o resto vira documento novo por tipo |
| Tipo declarado errado | Corrige `data-type` no box e ajusta a forma do texto |
| Desatualizado | Reescreve no lugar, a partir da fonte, e registra a Origem |
| Duplica outro (`dup`) | Funde no que fica; o que sai vira redirecionamento ou some do roadmap |
| Grande demais | Divide por assunto, mantendo o tipo |

Ao dividir, o documento principal fica com o slug e o box originais. Os extraídos
ganham slug novo na mesma seção, com o próximo número livre.

### 6. Reescrever

Siga o modelo do tipo alvo em
`.claude/skills/govhub-doc-writer/references/modelos-diataxis.md` — teoria,
forma, tom e template de cada um dos quatro. Não duplique aquilo aqui.

Regras de forma do repositório (Markdown puro, links `#doc/<slug>`, `[!TODO]`
enquanto restar pendência) estão em
`.claude/skills/govhub-doc-writer/references/estrutura-do-repo.md`.

Ao extrair conteúdo, deixe no documento de origem um link para onde ele foi.

### 7. Atualizar o roadmap

Toda alteração estrutural reflete no `index.html`:

- documento novo extraído → **box novo** na mesma seção
- tipo corrigido → `data-type` **e** a classe e o rótulo do selo, os três juntos
- pendência resolvida → remova ou troque a `data-tag`
- documento fundido → remova o box do que sumiu

O markup exato do box está em `estrutura-do-repo.md`. Os três atributos do selo
precisam concordar entre si — `verificar.py` reprova se divergirem.

### 8. Verificar

```bash
python3 .claude/skills/govhub-doc-writer/scripts/verificar.py
python3 .claude/skills/govhub-doc-refactor/scripts/diagnosticar.py <slug>
```

O primeiro confere a integridade do repositório; o segundo confirma que a mistura
que motivou a refatoração sumiu. **Rode os dois antes de dizer que terminou.**

## Erros comuns

| Erro | Consequência | Correção |
|---|---|---|
| Reescrever sem ler o original inteiro | Conteúdo bom desaparece | Passo 2 antes do 6 |
| Dividir sem criar os boxes | Documentos invisíveis no roadmap | Passo 7 |
| Extrair sem deixar link no original | O leitor perde o rastro | Link no lugar de onde saiu |
| Espelhar sem registrar a Origem | Cópia órfã que diverge em silêncio | Bloco do passo 4 |
| Trocar só o `data-type` e esquecer o selo | Filtro do topo quebra | Os três atributos juntos |
| Confiar no diagnóstico sem ler | Heurística tem falso positivo | Ela sugere, você decide |

## Referências

- `references/repos-da-organizacao.md` — os repositórios da GovHub-br e o que cada um alimenta
- `scripts/diagnosticar.py` — sinais de mistura de tipos num documento
- `scripts/espelho.py` — busca e compara com a fonte em outro repositório

Para escrever do zero, use **govhub-doc-writer**; a teoria dos quatro tipos e os
modelos ficam nas referências dela.
