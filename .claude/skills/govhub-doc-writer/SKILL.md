---
name: govhub-doc-writer
description: Use quando for escrever, preencher ou revisar documentação do GovHub no repositório govhub-roadmap — preencher um esqueleto de docs/*.md, resolver um bloco [!TODO], migrar conteúdo do gov-hub.io, criar uma página nova, ou adicionar/ajustar um box do roadmap no index.html.
---

# Escrever documentação do GovHub

O repositório `govhub-roadmap` é um roadmap visual onde cada box abre um documento
em `docs/`. Escrever documentação aqui significa três coisas ao mesmo tempo:
escolher o **tipo Diátaxis** certo, escrever o `.md`, e garantir que o box do
roadmap aponte para ele.

## A regra que não se negocia

**Não invente conteúdo técnico.** Estes documentos descrevem um sistema real, em
produção, usado por órgãos públicos. Um comando errado, uma porta errada ou uma
versão inventada custa horas de quem seguir o passo a passo — e destrói a
confiança no resto da documentação.

Quando não souber, escreva `*a escrever: <o que falta descobrir>*` e siga em
frente. Um esqueleto honesto é infinitamente melhor que prosa plausível e falsa.

| Racionalização | Realidade |
|---|---|
| "É só um exemplo genérico de Docker" | O leitor vai colar no terminal. Genérico e errado = errado. |
| "Provavelmente a porta é essa" | "Provavelmente" não vai pra documentação. Marque como a verificar. |
| "Dá pra inferir pelo nome do arquivo" | Inferência é hipótese. Verifique no código ou marque. |
| "O usuário confirma depois" | Ele confirma o que consegue ver que é dúvida. Prosa afirmativa não parece dúvida. |
| "Deixar em branco fica feio" | `*a escrever*` é um marcador de trabalho. Texto falso é um bug. |

Fontes aceitáveis, nesta ordem: código do repositório da aplicação → página atual
no `gov-hub.io` → o que o usuário disser explicitamente. Nada mais.

## Fluxo

### 1. Perguntar a seção

Sempre comece perguntando **qual seção**, mesmo que pareça óbvio pelo contexto.
Use AskUserQuestion com as sete opções:

| Seção | Chave | Prefixo do slug |
|---|---|---|
| Configurações Gerais | `config` | `cfg-` |
| Arquitetura | `arch` | `arch-` |
| Dados & Pipeline | `data` | `data-` |
| Dashboards & Relatórios | `dash` | `dash-` |
| Infraestrutura | `infra` | `infra-` |
| Governança | `gov` | `gov-` |
| Comunidade & Contribuição | `community` | `com-` |

### 2. Mostrar o que está pendente naquela seção

```bash
python3 .claude/skills/govhub-doc-writer/scripts/listar.py <chave-da-seção>
```

Lista os boxes da seção com o estado de cada `.md` (esqueleto, parcial ou
escrito), o tipo Diátaxis e as tags. Deixe o usuário escolher qual atacar — ou
confirme que é um documento novo.

### 3. Entender o que precisa ser feito

Leia o `.md` atual **antes de propor qualquer coisa**. O bloco `> [!TODO]` no topo
já diz o que falta e costuma linkar a página do `gov-hub.io` a migrar.

Descubra, nesta ordem:

- O tipo Diátaxis do box está certo? (ver `references/modelos-diataxis.md`)
- Existe conteúdo a migrar do `gov-hub.io`? Busque com WebFetch.
- Existe código no repositório da aplicação que responde as perguntas em aberto?
- O que sobra que só o usuário sabe?

### 4. Pedir a fonte

Pergunte explicitamente pela fonte do conteúdo antes de escrever. Ofereça as
opções concretas: URL da página atual, caminho de um arquivo no repo da
aplicação, um documento existente, ou "não tem, vou te ditar".

Se o usuário não tiver fonte para parte do conteúdo, **essa parte continua
`*a escrever*`**. Não preencha por conta própria.

### 5. Escrever o .md

Siga o modelo do tipo em `references/modelos-diataxis.md`. Regras de forma:

- Markdown puro. Sem HTML embutido — o estilo mora no `index.html`.
- Links internos: `#doc/<slug>`. Links externos: URL completa.
- `> [!TODO] …` no topo enquanto restar algo por escrever. Remova quando acabar.
- Português do Brasil, segunda pessoa implícita ("rode", "confira"), sem "nós".
- Uma necessidade por documento. Se ao escrever surgir conteúdo de outro tipo,
  ele vira **outro documento**, não uma seção extra.

### 6. Ligar ao roadmap

Documento de box **já existente**: nada a fazer no `index.html` — o `data-md` já
aponta pra lá. Só remova a tag de estado (`rascunho`, `gap`) se ela deixou de valer.

Documento **novo**: insira o box na **faixa** certa da seção. Decida a faixa pelo
papel do documento — Entender, Praticar, Resolver, Consultar ou Recomendações —
e ponha o `data-parent` no rótulo dela. Formato exato:

```html
      <div class="rm-item" id="<id-curto>" data-sec="<chave>" data-parent="band-<chave>-<faixa>" data-type="<tipo>" data-md="<slug>"><button class="rm-check" type="button" aria-label="marcar como lido"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></button><span class="rm-title"><Título></span><span class="type <tipo>"><rótulo></span></div>
```

Detalhes em `references/estrutura-do-repo.md`.

### 7. Verificar

```bash
python3 .claude/skills/govhub-doc-writer/scripts/verificar.py
```

Confere: todo `data-md` tem arquivo, todo arquivo tem box, links `#doc/` não
quebrados, coerência dos atributos do box, tags do HTML e sintaxe do JS.
Sai com código 1 se achar problema. **Rode sempre antes de dizer que terminou.**

Ambos os scripts rodam a partir da **raiz do repositório**, não de dentro da
pasta da skill.

## Escolher o tipo Diátaxis

O erro mais comum da documentação técnica é misturar os quatro tipos numa página.
Decida **antes** de escrever a primeira linha:

```
É sobre FAZER alguma coisa?
├── SIM: o leitor está APRENDENDO ou EXECUTANDO?
│   ├── aprendendo   → tutorial
│   └── executando   → guia
└── NÃO: ele quer FATOS ou ENTENDIMENTO?
    ├── fatos        → referência
    └── entendimento → explicação
```

Teste rápido: se a página tem passo a passo **e** tabela de parâmetros, são dois
documentos. Passo a passo **e** justificativa de arquitetura, idem.

**Leia `references/modelos-diataxis.md` antes de escrever.** Ele traz o que cada
tipo exige de forma e de tom, o modelo pronto de cada um, e as tabelas para
diagnosticar quando o tipo está errado.

## Erros comuns do processo

Os erros de *escrita* estão em `references/modelos-diataxis.md`. Os do
*processo* são estes:

| Erro | Consequência | Correção |
|---|---|---|
| Escrever sem ler o `.md` atual | Reescreve o que já estava certo e perde a anotação do `[!TODO]` | Passo 3 vem antes do 5 |
| Preencher sem fonte | Documentação plausível e falsa | Sem fonte, fica `*a escrever*` |
| Remover o `[!TODO]` com seções ainda `*a escrever*` | Documento parece pronto e não está | Só remova quando não restar nenhum marcador |
| Criar documento sem criar o box | Fica invisível no roadmap | Passo 6 |
| Editar `docs/` sem rodar `verificar.py` | Link quebrado passa despercebido | Passo 7 não é opcional |

## Referências

Esta skill vive em `.claude/skills/govhub-doc-writer/` dentro do próprio
repositório, versionada junto com a documentação que ela ajuda a escrever.

- `references/modelos-diataxis.md` — teoria dos quatro tipos, modelos prontos e
  diagnóstico. **Leitura obrigatória antes de escrever.**
- `references/estrutura-do-repo.md` — layout, slugs, markup do box, seções
- `scripts/listar.py` — estado dos documentos por seção
- `scripts/verificar.py` — validação completa antes de fechar

Para a identidade visual (cores, tipografia, tokens), use a skill
**govhub-visual-identity**, que fica ao lado desta em `.claude/skills/`.
