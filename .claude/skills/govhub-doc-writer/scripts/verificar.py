#!/usr/bin/env python3
"""Valida o repositório govhub-roadmap antes de fechar um trabalho de escrita.

Confere:
  1. todo data-md tem arquivo em docs/ e todo arquivo tem box
  2. links internos #doc/ apontam para documentos existentes
  3. atributos do box coerentes (tipo válido, seção existente, rótulo do selo)
  4. tags HTML do index.html fecham corretamente
  5. sintaxe do JS embutido (se o node estiver disponível)

Uso:
    python3 scripts/verificar.py

Sai com código 1 se encontrar qualquer problema.
"""
import os
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser

TIPOS = {"tutorial": "tutorial", "guia": "guia",
         "referencia": "referência", "explicacao": "explicação"}
SECOES = {"config", "arch", "data", "dash", "infra", "gov", "community"}
VOID = {"meta", "link", "br", "hr", "img", "input", "polyline", "path", "source"}

problemas = []
avisos = []


def erro(msg):
    problemas.append(msg)


def aviso(msg):
    avisos.append(msg)


class Aninhamento(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pilha = []
        self.erros = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID and tag != "svg":
            self.pilha.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in VOID or tag == "svg":
            return
        if not self.pilha:
            self.erros.append("</%s> sem abertura, linha %d" % (tag, self.getpos()[0]))
            return
        if self.pilha[-1][0] != tag:
            self.erros.append("</%s> na linha %d fecha <%s> da linha %d"
                              % (tag, self.getpos()[0], self.pilha[-1][0], self.pilha[-1][1]))
        else:
            self.pilha.pop()


def main():
    if not os.path.exists("index.html"):
        sys.exit("Rode a partir da raiz do repositório govhub-roadmap.")

    html = open("index.html", encoding="utf-8").read()
    arquivos = {f[:-3] for f in os.listdir("docs") if f.endswith(".md")}

    # ---- 1. ligação box <-> arquivo
    boxes = re.findall(
        r'<div class="rm-item[^"]*" id="([^"]+)" data-sec="([^"]+)"'
        r' data-parent="([^"]+)" data-type="([^"]+)" data-md="([^"]+)"([^>]*)>'
        r'.*?<span class="rm-title">([^<]+)</span>'
        r'(?:<span class="type ([^"]+)">([^<]+)</span>)?', html)

    ids_existentes = set(re.findall(r'\bid="([^"]+)"', html))

    slugs = {b[4] for b in boxes}
    for s in sorted(slugs - arquivos):
        erro("box aponta para docs/%s.md, que não existe" % s)
    for s in sorted(arquivos - slugs):
        erro("docs/%s.md existe mas nenhum box aponta para ele" % s)

    # ---- 3. coerência dos atributos
    ids = [b[0] for b in boxes]
    for dup in {i for i in ids if ids.count(i) > 1}:
        erro("id de box repetido: %s" % dup)
    for bid, sec, parent, tipo, slug, resto, titulo, cls, rotulo in boxes:
        if sec not in SECOES:
            erro("%s: data-sec='%s' não é uma seção conhecida" % (slug, sec))
        if parent not in ids_existentes:
            erro("%s: data-parent='%s' não existe no documento" % (slug, parent))
        if tipo not in TIPOS:
            erro("%s: data-type='%s' inválido" % (slug, tipo))
            continue
        if cls and cls != tipo:
            erro("%s: classe do selo ('%s') diferente do data-type ('%s')" % (slug, cls, tipo))
        if rotulo and rotulo != TIPOS[tipo]:
            erro("%s: rótulo do selo é '%s', esperado '%s'" % (slug, rotulo, TIPOS[tipo]))
        tag = re.search(r'data-tag="([^"]+)"', resto)
        if tag and tag.group(1) not in {"lacuna", "gap", "dup", "rascunho"}:
            erro("%s: data-tag='%s' desconhecido" % (slug, tag.group(1)))

    # ---- 2. links internos e estado dos documentos
    for slug in sorted(arquivos):
        texto = open(os.path.join("docs", slug + ".md"), encoding="utf-8").read()
        for alvo in sorted(set(re.findall(r"\(#doc/([a-z0-9-]+)\)", texto))):
            if alvo not in arquivos:
                erro("docs/%s.md linka #doc/%s, que não existe" % (slug, alvo))
        if "[!TODO]" not in texto and re.search(r"\*[Aa] escrever", texto):
            erro("docs/%s.md perdeu o [!TODO] mas ainda tem '*a escrever*'" % slug)
        if not texto.lstrip().startswith("# "):
            erro("docs/%s.md não começa com um título de nível 1" % slug)
        if re.search(r"^\s*<[a-z]+[ >]", texto, re.M):
            aviso("docs/%s.md tem HTML embutido — o estilo deve ficar no index.html" % slug)

    # ---- 4. aninhamento do HTML
    p = Aninhamento()
    p.feed(html)
    for e in p.erros:
        erro("HTML: " + e)
    for tag, linha in p.pilha:
        erro("HTML: <%s> aberto na linha %d nunca fecha" % (tag, linha))

    # ---- 5. sintaxe do JS
    js = re.search(r"<script>(.*)</script>", html, re.S)
    if js:
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
            f.write(js.group(1))
            caminho = f.name
        try:
            r = subprocess.run(["node", "--check", caminho],
                               capture_output=True, text=True)
            if r.returncode != 0:
                erro("JS com erro de sintaxe:\n" + r.stderr.strip())
        except FileNotFoundError:
            aviso("node não encontrado — sintaxe do JS não verificada")
        finally:
            os.unlink(caminho)

    # ---- relatório
    print("%d boxes · %d documentos" % (len(boxes), len(arquivos)))
    for a in avisos:
        print("  aviso: " + a)
    if problemas:
        print("\n%d problema(s):" % len(problemas))
        for e in problemas:
            print("  - " + e)
        sys.exit(1)
    print("tudo consistente.")


if __name__ == "__main__":
    main()
