# GovHub — Roadmap de Documentação

Roadmap visual da documentação do GovHub, no estilo do [roadmap.sh](https://roadmap.sh): uma espinha vertical com as 7 seções, e cada box pendurado nelas é um documento tipado pelo framework [Diátaxis](https://diataxis.fr).

São 47 documentos em `docs/`. Sem build e sem dependências de pacote: `index.html` mais arquivos `.md`, servidos como estão pelo GitHub Pages.

## Como funciona

Três views, roteadas pelo hash da URL:

| View | Hash | O que é |
| --- | --- | --- |
| Roadmap | *(nenhum)* | A espinha completa: 7 seções, 47 boxes, progresso salvo no navegador |
| Instalação | `#instalacao` | Roadmap detalhado de uma página só, etapa por etapa |
| Doc | `#doc/<slug>` | Renderiza um `.md` de `docs/` com a identidade visual do GovHub |

Clicar num box abre o documento. Clicar no quadradinho à esquerda marca como lido.

## Os tipos (Diátaxis)

Cada documento serve a **uma** necessidade. Misturar os quatro numa página só é o erro mais comum, e é o que o selo colorido existe pra evitar.

| Tipo | Serve para | Quantos |
| --- | --- | --- |
| **tutorial** (verde) | Aprender fazendo. Caminho único, resultado garantido. | 4 |
| **guia** (azul) | Resolver um problema específico de quem já sabe o básico. | 10 |
| **referência** (roxo) | Consultar. Tabelas, parâmetros, listas. | 20 |
| **explicação** (marrom) | Entender o porquê, o contexto e as alternativas. | 13 |

As tags tracejadas marcam o que ainda precisa de decisão: `lacuna` (tipo a confirmar), `gap` (não existe em lugar nenhum), `dup` (a fundir), `rascunho` (proposta a validar).

## Escrever um documento

Todos os 47 arquivos já existem em `docs/`, com esqueleto adequado ao seu tipo e um bloco `> [!TODO]` no topo dizendo o que falta. Muitos apontam para a página correspondente no `gov-hub.io`, que é o conteúdo a migrar e revisar.

Convenções:

- **Markdown puro**, sem HTML embutido — o estilo mora no `index.html`.
- Respeite o tipo do box. Se ao escrever ficar claro que o tipo está errado, mude o `data-type` no `index.html` em vez de misturar.
- Links internos usam `#doc/<slug>`.
- `> [!TODO] …` no topo vira o destaque laranja de "a escrever".

Sintaxe suportada pelo renderizador: títulos `#`–`####`, listas, tabelas, blocos de código cercados, blockquote, `---`, links, imagens, **negrito**, *itálico* e `código`.

Para adicionar um documento novo: crie `docs/<slug>.md` e um box no `index.html` com `data-md="<slug>"`, `data-type` e `data-parent` apontando para a seção.

## Rodar localmente

A view de doc usa `fetch()` para ler os `.md`, e o navegador bloqueia isso em `file://`. Abrir o `index.html` com duplo clique faz o roadmap e a Instalação funcionarem, mas não a view de doc. Para ver tudo:

```bash
python3 -m http.server 8000
```

E acesse `http://localhost:8000`. No GitHub Pages funciona sem nada disso.

## Publicar

```bash
git add index.html docs/ .nojekyll README.md
git commit -m "docs: roadmap único com os 47 documentos"
git push
```

Depois, em **Settings → Pages**: Source `Deploy from a branch`, Branch `main` / `(root)`. Em 1–2 minutos o site sobe em `https://SEU-USUARIO.github.io/govhub-roadmap/`.

Para colocar dentro de um repo GovHub-br existente, copie `index.html`, `docs/` e `.nojekyll` para uma pasta `docs/` do repo e escolha Branch `main` / `/docs` nas configurações do Pages.

## Identidade visual

Segue o guia oficial do GovHub: roxo `#7A34F3` como cor-assinatura, laranja `#F97316` só como acento pontual, fundos claros neutros e fonte Inter. Os tokens estão no `:root` do `index.html`.

## Arquivos

- `index.html` — as três views, o desenho das arestas e o renderizador de Markdown
- `docs/*.md` — os 47 documentos
- `.nojekyll` — impede o GitHub de processar o repositório com Jekyll
