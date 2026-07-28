# GovHub — Roadmap de Documentação

Página única (`index.html`), sem build, sem dependências — GitHub Pages serve exatamente como está.

## Publicar em um repositório novo

Rode isso na pasta `govhub-roadmap-pages/` (ou copie o conteúdo dela pra onde preferir):

```bash
git init
git add index.html .nojekyll README.md
git commit -m "docs: primeira versão do roadmap GovHub"
git branch -M main
git remote add origin git@github.com:SEU-USUARIO/govhub-roadmap.git
git push -u origin main
```

Troque `SEU-USUARIO/govhub-roadmap` pelo repositório que você criar no GitHub (repo vazio, sem README/gitignore automático, pra não conflitar com o push acima).

## Ativar o GitHub Pages

Isso só dá pra fazer pela interface web (não tem comando git pra isso):

1. No repositório, vá em **Settings → Pages**.
2. Em "Build and deployment", **Source**: `Deploy from a branch`.
3. **Branch**: `main` / `(root)`.
4. Salve. Em 1–2 minutos o site sobe em `https://SEU-USUARIO.github.io/govhub-roadmap/`.

## Se preferir colocar dentro de um repo GovHub-br existente

Em vez de `git remote add origin ...` acima, copie `index.html` e `.nojekyll` pra uma pasta `docs/` do repo existente (ex: `govhub-research`), faça commit normal, e em Settings → Pages escolha **Branch**: `main` / **`/docs`** em vez de `/(root)`.

## Arquivos

- `index.html` — o roadmap completo (board por seções + detalhe da Instalação com arestas)
- `.nojekyll` — evita que o GitHub processe o arquivo com Jekyll (não precisamos, é HTML puro)
