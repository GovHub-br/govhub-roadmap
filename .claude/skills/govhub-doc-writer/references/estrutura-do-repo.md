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

## Seções

A espinha é encadeada: cada seção tem `data-parent` apontando para a anterior.
Não reordene sem ajustar essa cadeia, ou as arestas ficam cruzadas.

| Seção | id do nó | data-parent | prefixo do slug |
|---|---|---|---|
| Configurações Gerais | `sec-config` | `rm-root` | `cfg-` |
| Arquitetura | `sec-arch` | `sec-config` | `arch-` |
| Dados & Pipeline | `sec-data` | `sec-arch` | `data-` |
| Dashboards & Relatórios | `sec-dash` | `sec-data` | `dash-` |
| Infraestrutura | `sec-infra` | `sec-dash` | `infra-` |
| Governança | `sec-gov` | `sec-infra` | `gov-` |
| Comunidade & Contribuição | `sec-community` | `sec-gov` | `com-` |

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
      <div class="rm-item" id="dash-11" data-parent="sec-dash" data-type="guia" data-md="dash-11-exportar-dados"><button class="rm-check" type="button" aria-label="marcar como lido"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></button><span class="rm-title">Exportar dados de um gráfico</span><span class="type guia">guia</span></div>
```

Atributos:

| Atributo | Valores | Para quê |
|---|---|---|
| `id` | curto e único (`dash-11`) | chave do progresso no localStorage |
| `data-parent` | `sec-<chave>` | de onde sai a aresta |
| `data-type` | `tutorial` `guia` `referencia` `explicacao` | cor do selo e filtro |
| `data-md` | o slug, sem `.md` | qual arquivo abrir |
| `data-tag` | `lacuna` `gap` `dup` `rascunho` | opcional; estado do documento |

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
