#!/usr/bin/env python3
"""Lista os boxes de uma seção do roadmap com o estado de cada documento.

Uso:
    python3 scripts/listar.py            # todas as seções, resumido
    python3 scripts/listar.py dash        # só a seção de Dashboards

Rode a partir da raiz do repositório govhub-roadmap.
"""
import os
import re
import sys

SECOES = {
    "config": "Configurações Gerais",
    "arch": "Arquitetura",
    "data": "Dados & Pipeline",
    "dash": "Dashboards & Relatórios",
    "infra": "Infraestrutura",
    "gov": "Governança",
    "community": "Comunidade & Contribuição",
}

BOX = re.compile(
    r'<div class="rm-item" id="(?P<id>[^"]+)" data-parent="sec-(?P<sec>[^"]+)"'
    r' data-type="(?P<tipo>[^"]+)" data-md="(?P<slug>[^"]+)"(?P<resto>[^>]*)>'
    r'.*?<span class="rm-title">(?P<titulo>[^<]+)</span>'
)


def estado(slug):
    """Classifica o documento pelo quanto ainda falta escrever."""
    caminho = os.path.join("docs", slug + ".md")
    if not os.path.exists(caminho):
        return "SEM ARQUIVO", 0
    texto = open(caminho, encoding="utf-8").read()
    pendencias = len(re.findall(r"\*[Aa] escrever", texto))
    tem_todo = "[!TODO]" in texto
    if not tem_todo and pendencias == 0:
        return "escrito", 0
    if pendencias == 0:
        return "quase (só o [!TODO] sobrou)", 0
    return "esqueleto", pendencias


def main():
    if not os.path.exists("index.html"):
        sys.exit("Rode a partir da raiz do repositório govhub-roadmap.")

    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    if alvo and alvo not in SECOES:
        sys.exit("Seção desconhecida: %s\nUse uma de: %s" % (alvo, ", ".join(SECOES)))

    html = open("index.html", encoding="utf-8").read()
    boxes = [m.groupdict() for m in BOX.finditer(html)]

    total_pend = 0
    for chave, nome in SECOES.items():
        if alvo and chave != alvo:
            continue
        da_secao = [b for b in boxes if b["sec"] == chave]
        if not da_secao:
            continue
        print("\n%s  (%d documentos)" % (nome, len(da_secao)))
        print("-" * 74)
        for b in da_secao:
            tag = re.search(r'data-tag="([^"]+)"', b["resto"])
            st, pend = estado(b["slug"])
            total_pend += pend
            marca = {"escrito": "  ok"}.get(st, "  --")
            print("%s %-34s %-11s %-13s %s%s" % (
                marca,
                b["slug"],
                b["tipo"],
                st if st != "esqueleto" else "esqueleto",
                "%d pendências" % pend if pend else "",
                "  [%s]" % tag.group(1) if tag else "",
            ))

    print("\n%d boxes  ·  %d marcadores '*a escrever*' no total" % (
        len(boxes) if not alvo else len([b for b in boxes if b["sec"] == alvo]),
        total_pend))


if __name__ == "__main__":
    main()
