# Estrutura do repositório govhub-roadmap

```
govhub-roadmap/
├── index.html      # as 3 views, o desenho das arestas e o renderizador de Markdown
├── docs/*.md       # os documentos (47 hoje)
├── .nojekyll       # impede o GitHub de processar com Jekyll
└── README.md
```

Publicado em <https://govhub-br.github.io/govhub-roadmap/> pelo GitHub Pages
(branch `main`, raiz). Sem build: o que está no repositório é o que vai ao ar.

## As três views

| View | Hash | Elemento |
|---|---|---|
| Roadmap | *(nenhum)* | `#view-roadmap` |
| Instalação | `#instalacao` | `#view-instalacao` |
| Doc | `#doc/<slug>` | `#view-doc` |

A view de doc lê `docs/<slug>.md` com `fetch()`. Isso **não funciona em `file://`** —
para testar localmente, `python3 -m http.server 8000`.

## Faixas

Dentro de cada seção os documentos ficam em cinco faixas, sempre nesta ordem.
A faixa diz o **papel** do documento no percurso de leitura; o selo diz o **tipo**
Diátaxis. São eixos independentes — uma recomendação pode ser guia ou explicação.

| Faixa | id do rótulo | Papel | Tipo mais comum |
|---|---|---|---|
| *(introdução)* | — | porta de entrada da seção | explicação |
| Entender | `band-<sec>-entender` | contexto e conceitos | explicação |
| Praticar | `band-<sec>-praticar` | aprender fazendo | tutorial |
| Resolver | `band-<sec>-resolver` | resolver um problema | guia |
| Consultar | `band-<sec>-consultar` | achar um dado | referência |
| Recomendações | `band-<sec>-recomendacoes` | o que fazer e evitar | guia ou explicação |

A introdução fica presa direto no nó da seção, com a classe extra `intro`. As
demais penduram no rótulo da sua faixa.

Faixa sem documento renderiza tracejada, com "nenhum documento nesta faixa
ainda". **Não esconda uma faixa vazia** — ela é a lacuna que o roadmap existe
para mostrar.

## Seções

A espinha é encadeada: cada seção tem `data-parent` apontando para a última
faixa da seção anterior. Não reordene sem ajustar essa cadeia, ou as arestas
ficam cruzadas.

| Seção | id do nó | data-parent | prefixo do slug |
|---|---|---|---|
| Configurações Gerais | `sec-config` | `rm-root` | `cfg-` |
| Arquitetura | `sec-arch` | `band-config-recomendacoes` | `arch-` |
| Dados & Pipeline | `sec-data` | `band-arch-recomendacoes` | `data-` |
| Dashboards & Relatórios | `sec-dash` | `band-data-recomendacoes` | `dash-` |
| Infraestrutura | `sec-infra` | `band-dash-recomendacoes` | `infra-` |
| Governança | `sec-gov` | `band-infra-recomendacoes` | `gov-` |
| Comunidade & Contribuição | `sec-community` | `band-gov-recomendacoes` | `com-` |

## Slugs

Formato: `<prefixo>-<NN>-<nome-curto>`, tudo minúsculo, sem acento, hifenizado.
O `NN` é a ordem dentro da seção, com dois dígitos.

```
cfg-01-instalacao
dash-05-tipos-de-grafico
com-09-primeiro-pr
```

O nome do arquivo é `docs/<slug>.md`. O atributo `data-md` do box guarda o slug
**sem** a extensão.

## Markup do box

Uma linha só, dentro da `<div class="rm-row">` da seção:

```html
      <div class="rm-item" id="dash-12" data-sec="dash" data-parent="band-dash-resolver" data-type="guia" data-md="dash-12-exportar-dados"><button class="rm-check" type="button" aria-label="marcar como lido"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></button><span class="rm-title">Exportar dados de um gráfico</span><span class="type guia">guia</span></div>
```

Atributos:

| Atributo | Valores | Para quê |
|---|---|---|
| `id` | curto e único (`dash-12`) | chave do progresso no localStorage |
| `data-sec` | a chave da seção | agrupa o progresso e os scripts |
| `data-parent` | `band-<sec>-<faixa>` | de onde sai a aresta |
| `data-type` | `tutorial` `guia` `referencia` `explicacao` | cor do selo e filtro |
| `data-md` | o slug, sem `.md` | qual arquivo abrir |
| `data-tag` | `lacuna` `gap` `dup` `rascunho` | opcional; estado do documento |

`data-sec` e `data-parent` precisam concordar: um box em `band-dash-resolver`
tem que ter `data-sec="dash"`. O `verificar.py` confere que o `data-parent`
aponta para um id existente.

O `<span class="type …">` precisa do **rótulo com acento** (`referência`,
`explicação`), enquanto a classe e o `data-type` usam a forma sem acento
(`referencia`, `explicacao`). Trocar isso quebra o filtro do topo.

## Tags de estado

| Tag | Significado | Quando remover |
|---|---|---|
| `rascunho` | proposta ainda não validada com quem opera | depois de validada |
| `lacuna` | existe, mas o tipo Diátaxis está em dúvida | ao confirmar o tipo |
| `gap` | não existe em lugar nenhum | quando o documento for escrito |
| `dup` | duplica outro documento | depois de fundir |

Ao terminar um documento, reavalie a tag. Um `rascunho` escrito mas não validado
continua `rascunho`.

## Renderizador de Markdown

Fica no `index.html` (`var mdToHtml`). É próprio, sem CDN. Suporta:

títulos `#`–`####` · listas ordenadas e não ordenadas · tabelas · blocos de
código cercados · blockquote · `---` · links · imagens · `**negrito**` ·
`*itálico*` · `` `código` `` · alertas `> [!TODO] …`

**Não** suporta: listas aninhadas, HTML embutido, notas de rodapé, listas de
definição. Se precisar de algo fora dessa lista, estenda o renderizador em vez
de embutir HTML no `.md`.

## Identidade visual

Tokens no `:root` do `index.html`, seguindo o guia oficial: roxo `#7A34F3` como
assinatura, laranja `#F97316` só como acento, Inter em tudo. Os selos de tipo
usam versões escurecidas (verde `#0B7355`, marrom `#8F4F26`) para passar em
contraste AA com texto branco em 9px. **Não clareie esses dois** sem refazer a
conta de contraste.
