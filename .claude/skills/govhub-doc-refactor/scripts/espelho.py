#!/usr/bin/env python3
"""Resolve e busca o arquivo de origem de um documento em outro repositório da
organização GovHub-br.

A maior parte dos documentos deste repositório espelha páginas do site, cuja
fonte é o MkDocs em GovHub-br/gov-hub. O mapeamento é direto:

    gov-hub.io/documentacao/adocao/requisitos/
    → GovHub-br/gov-hub : docs/documentacao/adocao/requisitos.md

Uso:
    python3 scripts/espelho.py <slug>                    # resolve pela URL no [!TODO]
    python3 scripts/espelho.py <slug> --repo <repo> --path <caminho>
    python3 scripts/espelho.py <slug> --diff             # compara com o local

Depende do `gh` autenticado.
"""
import argparse
import base64
import json
import os
import re
import subprocess
import sys

ORG = "GovHub-br"
REPO_SITE = "gov-hub"


def gh(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if r.returncode != 0:
        return None, r.stderr.strip()
    return r.stdout, None


def url_para_caminho(url):
    """gov-hub.io/documentacao/adocao/requisitos/ -> docs/documentacao/adocao/requisitos.md"""
    caminho = re.sub(r"^https?://[^/]+", "", url).strip("/")
    if not caminho:
        return None
    return "docs/%s.md" % caminho


def origem_declarada(texto):
    """Procura a URL do site no bloco [!TODO] ou na seção Origem."""
    m = re.search(r"https?://gov-hub\.io[^\s\)\]]*", texto)
    if m:
        return m.group(0)
    m = re.search(r"\]\((/documentacao[^\)]*)\)", texto)
    if m:
        return "http://gov-hub.io" + m.group(1)
    return None


def buscar(repo, caminho):
    saida, erro = gh("api", "repos/%s/%s/contents/%s" % (ORG, repo, caminho))
    if erro:
        return None, erro
    dados = json.loads(saida)
    conteudo = base64.b64decode(dados["content"]).decode("utf-8", "replace")
    return {"conteudo": conteudo, "sha": dados["sha"],
            "url": dados["html_url"], "caminho": caminho, "repo": repo}, None


def ultimo_commit(repo, caminho):
    saida, erro = gh("api", "repos/%s/%s/commits?path=%s&per_page=1" % (ORG, repo, caminho))
    if erro:
        return None
    c = json.loads(saida)
    if not c:
        return None
    return {"sha": c[0]["sha"][:7], "data": c[0]["commit"]["committer"]["date"][:10],
            "autor": c[0]["commit"]["author"]["name"]}


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("slug")
    p.add_argument("--repo", default=None, help="repositório da organização (padrão: gov-hub)")
    p.add_argument("--path", default=None, help="caminho do arquivo no repositório de origem")
    p.add_argument("--diff", action="store_true", help="compara com o arquivo local")
    a = p.parse_args()

    if not os.path.exists("index.html"):
        sys.exit("Rode a partir da raiz do repositório govhub-roadmap.")

    local = os.path.join("docs", a.slug + ".md")
    if not os.path.exists(local):
        sys.exit("docs/%s.md não existe." % a.slug)
    texto_local = open(local, encoding="utf-8").read()

    repo = a.repo or REPO_SITE
    caminho = a.path
    if not caminho:
        url = origem_declarada(texto_local)
        if not url:
            sys.exit("Não achei URL de origem em docs/%s.md.\n"
                     "Informe explicitamente: --repo <repo> --path <caminho>" % a.slug)
        caminho = url_para_caminho(url)
        print("origem declarada no documento: %s" % url)

    print("buscando  %s/%s : %s\n" % (ORG, repo, caminho))
    res, erro = buscar(repo, caminho)
    if erro:
        print("não encontrado.\n%s" % erro)
        print("\nDica: liste o diretório com")
        print("  gh api repos/%s/%s/contents/%s --jq '.[].name'"
              % (ORG, repo, os.path.dirname(caminho)))
        sys.exit(1)

    commit = ultimo_commit(repo, caminho)
    linhas = res["conteudo"].count("\n") + 1
    print("ENCONTRADO")
    print("  url          %s" % res["url"])
    print("  tamanho      %d linhas" % linhas)
    if commit:
        print("  último commit %s em %s por %s" % (commit["sha"], commit["data"], commit["autor"]))
    print("\n  Registre a procedência no rodapé do .md:\n")
    print("    ## Origem\n")
    print("    Espelho de [`%s`](%s) em `%s/%s`," % (caminho, res["url"], ORG, repo))
    print("    sincronizado em %s%s." % (
        commit["data"] if commit else "<data>",
        " (commit `%s`)" % commit["sha"] if commit else ""))

    if a.diff:
        import difflib
        d = list(difflib.unified_diff(
            texto_local.splitlines(), res["conteudo"].splitlines(),
            fromfile="local/%s.md" % a.slug, tofile="%s/%s" % (repo, caminho), lineterm=""))
        print("\n" + "=" * 72)
        if not d:
            print("Idêntico ao local.")
        else:
            print("Diferenças (%d linhas de diff):\n" % len(d))
            print("\n".join(d[:200]))
            if len(d) > 200:
                print("\n… %d linhas omitidas" % (len(d) - 200))
    else:
        print("\n" + "=" * 72)
        print(res["conteudo"])


if __name__ == "__main__":
    main()
