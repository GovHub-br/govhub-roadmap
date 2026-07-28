# GovHub — Roadmap de Documentação

**→ [govhub-br.github.io/govhub-roadmap](https://govhub-br.github.io/govhub-roadmap/)**

Mapa visual da documentação do GovHub, no estilo do [roadmap.sh](https://roadmap.sh):
uma espinha vertical com as 7 seções, e cada box pendurado nelas é um documento
tipado pelo framework [Diátaxis](https://diataxis.fr).

Serve a duas coisas ao mesmo tempo: mostrar **onde a documentação está furada** e
hospedar o texto que preenche esses furos.

Sem build e sem dependências de pacote — `index.html` mais arquivos `.md`,
servidos como estão pelo GitHub Pages.

## Estado atual

47 documentos mapeados. **Nenhum está pronto.** É esse o trabalho.

| | |
|---|---|
| Esqueleto (mais de 6 pendências) | 16 |
| Parcial | 31 |
| Escrito | 0 |
| Marcadores `*a escrever*` no total | 328 |

Por tipo: 20 referências, 13 explicações, 10 guias e **4 tutoriais**. O
desequilíbrio é o achado mais útil do mapa — a documentação é forte em consultar
e entender, e fraca em **aprender fazendo**.

Tags de decisão pendente, em 17 dos 47 boxes:

| Tag | Quantos | Significa |
|---|---|---|
| `rascunho` | 9 | proposta a validar com quem opera |
| `lacuna` | 6 | existe, mas o tipo Diátaxis está em dúvida |
| `gap` | 1 | não existe em lugar nenhum — "Primeiro PR, passo a passo" |
| `dup` | 1 | duplica outro documento, a fundir |

## Como funciona

Três views, roteadas pelo hash da URL:

| View | Hash | O que é |
|---|---|---|
| Roadmap | *(nenhum)* | A espinha: 7 seções, 47 boxes, progresso salvo no navegador |
| Instalação | `#instalacao` | Roadmap detalhado de uma página só, etapa por etapa |
| Doc | `#doc/<slug>` | Renderiza um `.md` de `docs/` com a identidade visual do GovHub |

Clicar num box abre o documento. Clicar no quadradinho à esquerda marca como
lido. O selo colorido indica o tipo; clicar num selo da barra do topo destaca só
aquele tipo.

## Os quatro tipos

Cada documento serve a **uma** necessidade. Misturar os quatro numa página é o
erro mais comum da documentação técnica, e é o que o selo existe para evitar.

| Tipo | O leitor está | Precisa de |
|---|---|---|
| **tutorial** (verde) | aprendendo | um caminho único que funciona |
| **guia** (azul) | trabalhando | resolver um problema concreto |
| **referência** (roxo) | consultando | achar um dado rápido |
| **explicação** (marrom) | estudando | entender o porquê |

Teoria completa, com o modelo de cada tipo, em
[`.claude/skills/govhub-doc-writer/references/modelos-diataxis.md`](.claude/skills/govhub-doc-writer/references/modelos-diataxis.md).

## Escrever um documento

Os 47 arquivos já existem em `docs/`, cada um com o esqueleto do seu tipo e um
bloco `> [!TODO]` no topo dizendo o que falta. Nos 37 que vieram do site, esse
bloco linka a página do `gov-hub.io` a migrar.

Veja o que está pendente numa seção:

```bash
python3 .claude/skills/govhub-doc-writer/scripts/listar.py dash
```

Chaves das seções: `config` `arch` `data` `dash` `infra` `gov` `community`.

Antes de fechar, sempre:

```bash
python3 .claude/skills/govhub-doc-writer/scripts/verificar.py
```

Confere que todo box tem arquivo, todo arquivo tem box, nenhum link `#doc/` está
quebrado, os atributos dos boxes concordam entre si e o HTML e o JS não
quebraram. Sai com código 1 se achar problema.

### Convenções

- **Markdown puro**, sem HTML embutido — o estilo mora no `index.html`.
- Respeite o tipo do box. Se ao escrever ficar claro que o tipo está errado,
  corrija o `data-type` em vez de misturar.
- Links internos usam `#doc/<slug>`.
- `> [!TODO] …` no topo enquanto restar pendência; remova só quando não sobrar
  nenhum `*a escrever*`.
- **Não invente conteúdo técnico.** Sem fonte, a seção fica `*a escrever*`.
  Documentação plausível e falsa custa mais caro que documentação incompleta.

Sintaxe suportada pelo renderizador: títulos `#`–`####`, listas, tabelas, blocos
de código cercados, blockquote, `---`, links, imagens, **negrito**, *itálico* e
`código`.

### De onde vem o conteúdo

A maior parte espelha páginas do site, cuja fonte é o MkDocs em
[`GovHub-br/gov-hub`](https://github.com/GovHub-br/gov-hub). O mapeamento é
direto:

```
gov-hub.io/documentacao/adocao/requisitos/
→ GovHub-br/gov-hub : docs/documentacao/adocao/requisitos.md
```

Buscar a fonte de um documento, com o commit e o bloco de procedência pronto:

```bash
python3 .claude/skills/govhub-doc-refactor/scripts/espelho.py cfg-03-requisitos
python3 .claude/skills/govhub-doc-refactor/scripts/espelho.py cfg-03-requisitos --diff
```

Documento vindo de espelho **registra a procedência** numa seção `## Origem` no
rodapé. Sem isso ninguém sabe de onde re-sincronizar, e a cópia diverge em
silêncio.

## Skills

O repositório traz três skills de agente em `.claude/skills/`, versionadas junto
com a documentação que ajudam a escrever:

| Skill | Para |
|---|---|
| **govhub-doc-writer** | escrever do zero: escolhe a seção, entende a pendência, pede a fonte, escreve pelo modelo do tipo e liga o box no roadmap |
| **govhub-doc-refactor** | consertar o que já existe: mistura de tipos, conteúdo desatualizado, espelho de outro repositório da organização, fusão de duplicados |
| **govhub-visual-identity** | cores, tipografia e tokens oficiais da marca |

Os scripts das duas primeiras rodam soltos, sem agente nenhum:

| Script | Faz |
|---|---|
| `govhub-doc-writer/scripts/listar.py` | estado dos documentos por seção |
| `govhub-doc-writer/scripts/verificar.py` | valida o repositório inteiro |
| `govhub-doc-refactor/scripts/diagnosticar.py` | acha mistura de tipos num documento |
| `govhub-doc-refactor/scripts/espelho.py` | busca a fonte em outro repositório da organização |

Todos rodam a partir da **raiz do repositório**.

## Rodar localmente

A view de doc lê os `.md` com `fetch()`, e o navegador bloqueia isso em
`file://`. Abrir o `index.html` com duplo clique faz o roadmap e a Instalação
funcionarem, mas não a view de doc. Para ver tudo:

```bash
python3 -m http.server 8000
```

E acesse `http://localhost:8000`. No GitHub Pages funciona sem nada disso.

## Publicar

O GitHub Pages já está configurado — branch `main`, raiz. Um push em `main`
republica o site em um ou dois minutos.

```bash
python3 .claude/skills/govhub-doc-writer/scripts/verificar.py   # antes de tudo
git add docs/ index.html
git commit -m "docs: <o que mudou>"
git push
```

## Identidade visual

Segue o guia oficial: roxo `#7A34F3` como cor-assinatura, laranja `#F97316` só
como acento pontual, fundos claros neutros e fonte Inter. Os tokens estão no
`:root` do `index.html`, com os mesmos nomes do
[`tokens.css`](.claude/skills/govhub-visual-identity/references/tokens.css) da
skill — o que permite reaproveitar componentes entre artefatos do GovHub.

As cores dos quatro tipos Diátaxis são extensão deste artefato, não da marca. O
verde dos tutoriais é mais escuro que o `--color-success` oficial porque o selo
usa texto branco em 9px, e o tom oficial reprovaria em contraste AA.

## Arquivos

```
index.html                as três views, o desenho das arestas e o renderizador
docs/*.md                 os 47 documentos
.claude/skills/           as três skills e seus scripts
.nojekyll                 impede o GitHub de processar o repositório com Jekyll
```
