# Repositórios da GovHub-br

Levantado em 2026-07-28 com `gh repo list GovHub-br`. Confirme antes de confiar —
a organização mexe nisso com frequência.

```bash
gh repo list GovHub-br --limit 40 --json name,description,isArchived,updatedAt \
  --jq '.[] | select(.isArchived==false) | "\(.name)\t\(.updatedAt[:10])\t\(.description // "")"'
```

## O que alimenta cada seção do roadmap

| Repositório | Alimenta |
|---|---|
| `gov-hub` | **A fonte do site.** MkDocs que gera gov-hub.io — espelho de 37 dos 47 documentos |
| `data-application-gov-hub` | Instalação, pipeline, dbt, Airflow, contribuição (`cfg-*`, `data-*`, `com-*`) |
| `data-framework` | Arquitetura, catálogo de dados, base para novos projetos (`arch-*`) |
| `data-application-cidades` | Fork Cidades (`com-05`) |
| `data-application-minc` | Fork MinC (`com-06`) |
| `data-application-mir` | Fork MIR — **sem box no roadmap** |
| `data-application-mgi` | Fork MGI — **sem box no roadmap** |
| `openmetadata-declarative-governance` | OpenMetadata (`gov-01`) |
| `data-governance-workshop` | Trino + Ranger (`gov-02`) — é workshop, confirma a nota de "não produção" |
| `cybersec` | Segurança (`gov-04`) |
| `govhub-research` | Pesquisa (`com-07`) |
| `CI-CD-PowerBI-MIR` | Dashboards do MIR — relevante para a seção de Dashboards |
| `continuous-deployment` | Infraestrutura, Argo CD (`infra-02`) |
| `govhub-plataform` | Plataforma |
| `graphrag-tais` | TAIS v2 |
| `dados-desestruturados` | OCR, parsers |
| `Dags-CID` | DAGs do Cidades |
| `GovHub-skills` | Skills de agente da organização |
| `cidades` | — |
| `govhub-roadmap` | **este repositório** |

Dois forks (`mir` e `mgi`) existem como repositório e não aparecem no roadmap,
que só tem Cidades e MinC. Vale confirmar com a equipe se devem entrar.

## O espelho do site

`gov-hub` é um MkDocs. O mapeamento de URL para arquivo é direto:

```
gov-hub.io/documentacao/adocao/requisitos/
→ GovHub-br/gov-hub : docs/documentacao/adocao/requisitos.md
```

Regra: tire o host, tire a barra final, prefixe `docs/`, sufixe `.md`.
É o que o `espelho.py` faz sozinho.

Estrutura de `docs/documentacao/`:

```
adocao/          conectar-fontes · deploy-inicial · requisitos
arquitetura/
comunidade/
dados/
forks/
governanca/
infraestrutura/
onboarding/
pipeline/
tutoriais/
visualizacao/
instalacao.md
CONTRIBUTING.md
index.md
```

Fora de `documentacao/`, o repositório do site ainda tem `dashboards/`,
`dicionario-dados/`, `guiasUso/`, `como-usar/`, `blog/` e
`acompanhamento-orcamentario/` — conteúdo que **não** está mapeado no roadmap.
Vale olhar antes de escrever algo do zero: pode já existir.

## Buscar em outro repositório

```bash
# listar um diretório
gh api repos/GovHub-br/<repo>/contents/<caminho> --jq '.[].name'

# procurar por termo no código da organização
gh search code --owner GovHub-br "<termo>" --limit 20

# último commit que tocou um arquivo
gh api "repos/GovHub-br/<repo>/commits?path=<caminho>&per_page=1" \
  --jq '.[0] | "\(.sha[0:7]) \(.commit.committer.date[:10]) \(.commit.author.name)"'
```
