#!/usr/bin/env python3
"""Diagnostica um documento antes de refatorar.

Procura sinais de que o documento mistura tipos Diátaxis, está desatualizado
ou diverge do que o box declara no roadmap.

Uso:
    python3 scripts/diagnosticar.py <slug|caminho|id-do-box>
    python3 scripts/diagnosticar.py --todos      # varre os 47

Rode a partir da raiz do repositório govhub-roadmap.
"""
import os
import re
import sys

SINAIS = {
    "passos": (
        r"(?m)^#{2,3}\s*\d+\.\s|^\d+\.\s+\S",
        "passos numerados",
        {"tutorial", "guia"},
    ),
    # tabela_parametros não é regex: ver detectar_tabela_parametros()
    "justificativa": (
        r"(?i)(por que\b|porqu[êe]\b|escolhemos|optamos|alternativa[s]? considerada|trade-?off|em vez de)",
        "justificativa de decisão",
        {"explicacao"},
    ),
    "comandos": (
        r"(?m)^```(bash|sh|shell|console)",
        "blocos de comando",
        {"tutorial", "guia"},
    ),
    "pre_requisitos": (
        r"(?mi)^#{2,3}\s*(antes de come[çc]ar|pr[ée]-?requisitos)",
        "seção de pré-requisitos",
        {"tutorial", "guia"},
    ),
    "problemas": (
        r"(?mi)^#{2,3}\s*(problemas comuns|troubleshooting)",
        "seção de problemas comuns",
        {"guia"},
    ),
    "limites": (
        r"(?mi)^#{2,3}\s*(limites|quando n[ãa]o)",
        "seção de limites",
        {"explicacao"},
    ),
}

TIPO_NOME = {"tutorial": "tutorial", "guia": "guia",
             "referencia": "referência", "explicacao": "explicação"}

# Cabeçalhos que caracterizam uma tabela de parâmetros (material de referência).
# Só valem como *célula inteira* do cabeçalho: procurar a palavra solta no corpo
# da tabela dá falso positivo — "Erro de tipo na métrica" numa tabela de
# problemas comuns não faz dela uma referência.
CABECALHOS_PARAMETRO = {
    "parâmetro", "parametro", "parâmetros", "opção", "opcao", "opções", "opcoes",
    "campo", "campos", "tipo", "tipos", "padrão", "padrao", "valor padrão",
    "flag", "flags", "variável", "variavel", "variáveis", "chave", "atributo",
}


def detectar_tabela_parametros(texto):
    """Conta tabelas cujo CABEÇALHO tem célula de parâmetro.

    Exige pelo menos duas colunas reconhecidas, ou uma reconhecida junto de
    'descrição' — o padrão de uma tabela de referência de verdade.
    """
    linhas = texto.split("\n")
    achadas = 0
    for i, linha in enumerate(linhas[:-1]):
        if "|" not in linha or "|" not in linhas[i + 1]:
            continue
        if not re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", linhas[i + 1]):
            continue  # a linha seguinte precisa ser a separadora
        celulas = {c.strip().strip("*`").lower()
                   for c in linha.strip().strip("|").split("|")}
        reconhecidas = celulas & CABECALHOS_PARAMETRO
        if len(reconhecidas) >= 2 or (reconhecidas and celulas & {"descrição", "descricao"}):
            achadas += 1
    return achadas


def carregar_boxes():
    html = open("index.html", encoding="utf-8").read()
    boxes = {}
    for m in re.finditer(
            r'<div class="rm-item" id="(?P<id>[^"]+)" data-parent="sec-(?P<sec>[^"]+)"'
            r' data-type="(?P<tipo>[^"]+)" data-md="(?P<slug>[^"]+)"(?P<resto>[^>]*)>'
            r'.*?<span class="rm-title">(?P<titulo>[^<]+)</span>', html):
        d = m.groupdict()
        tag = re.search(r'data-tag="([^"]+)"', d["resto"])
        d["tag"] = tag.group(1) if tag else ""
        boxes[d["slug"]] = d
    return boxes


def resolver(alvo, boxes):
    """Aceita slug, caminho do arquivo ou id do box."""
    alvo = alvo.strip()
    if alvo.endswith(".md"):
        alvo = os.path.basename(alvo)[:-3]
    if alvo in boxes:
        return alvo
    porid = [s for s, b in boxes.items() if b["id"] == alvo]
    if porid:
        return porid[0]
    parciais = [s for s in boxes if alvo.lower() in s.lower()]
    if len(parciais) == 1:
        return parciais[0]
    if parciais:
        print("Ambíguo. Candidatos:", ", ".join(sorted(parciais)))
    return None


def sem_marcadores(texto):
    """Remove o bloco [!TODO] e os '*a escrever…*'.

    Sem isso um esqueleto acusa mistura de tipos por causa do texto dos
    marcadores — '*a escrever: por que essa versão*' dispara o sinal de
    justificativa sem que exista justificativa nenhuma no documento.
    """
    texto = re.sub(r"(?m)^>\s*\[!TODO\].*(?:\n>.*)*", "", texto)
    texto = re.sub(r"\*[Aa] escrever[^*]*\*", "", texto)
    texto = re.sub(r"(?m)^\s*<[^>]+>\s*$", "", texto)  # <placeholders angulares>
    return texto


def diagnosticar(slug, box, verboso=True):
    caminho = os.path.join("docs", slug + ".md")
    bruto = open(caminho, encoding="utf-8").read()
    texto = sem_marcadores(bruto)
    tipo = box["tipo"]

    presentes = {}
    for chave, (padrao, rotulo, tipos) in SINAIS.items():
        achados = re.findall(padrao, texto)
        if achados:
            presentes[chave] = (rotulo, tipos, len(achados))

    n_tabelas = detectar_tabela_parametros(texto)
    if n_tabelas:
        presentes["tabela_parametros"] = ("tabela de parâmetros", {"referencia"}, n_tabelas)

    # tipos sugeridos pelos sinais encontrados
    sugeridos = set()
    for _, (_, tipos, _) in presentes.items():
        sugeridos |= tipos

    conflitos = []
    # mistura clássica: passo a passo + tabela de parâmetros
    if "passos" in presentes and "tabela_parametros" in presentes:
        conflitos.append("passo a passo + tabela de parâmetros → separe a referência")
    if "passos" in presentes and "justificativa" in presentes:
        conflitos.append("passo a passo + justificativa → separe a explicação")
    if tipo == "explicacao" and "comandos" in presentes:
        conflitos.append("explicação com blocos de comando → mova os comandos")
    if tipo == "referencia" and "passos" in presentes:
        conflitos.append("referência com passos numerados → isso é guia ou tutorial")
    if tipo == "explicacao" and "tabela_parametros" in presentes:
        conflitos.append("explicação com tabela de parâmetros → extraia a referência")

    pendencias = len(re.findall(r"\*[Aa] escrever", bruto))
    tem_todo = "[!TODO]" in bruto
    tem_origem = bool(re.search(r"(?mi)^##\s*Origem", bruto))
    linhas = bruto.count("\n") + 1

    if not verboso:
        marca = "!!" if conflitos else ("  " if not pendencias else " ~")
        print("%s %-34s %-11s %3d linhas  %2d pend.  %s" % (
            marca, slug, tipo, linhas, pendencias,
            conflitos[0] if conflitos else ""))
        return bool(conflitos)

    print("=" * 72)
    print("%s" % box["titulo"])
    print("  arquivo   docs/%s.md  (%d linhas)" % (slug, linhas))
    print("  box       %s · seção sec-%s · tipo declarado: %s%s" % (
        box["id"], box["sec"], TIPO_NOME[tipo],
        "  [%s]" % box["tag"] if box["tag"] else ""))
    print("  estado    %s%s%s" % (
        "%d marcadores '*a escrever*'" % pendencias if pendencias else "sem pendências",
        "  ·  tem [!TODO]" if tem_todo else "",
        "  ·  procedência registrada" if tem_origem else "  ·  SEM seção Origem"))

    print("\n  sinais encontrados no texto:")
    if not presentes:
        print("    (nenhum — provavelmente ainda é esqueleto)")
    for chave, (rotulo, tipos, n) in sorted(presentes.items()):
        combina = tipo in tipos
        print("    %-28s %2dx   típico de: %-22s %s" % (
            rotulo, n, "/".join(sorted(tipos)),
            "coerente" if combina else "NÃO combina com o tipo declarado"))

    if conflitos:
        print("\n  MISTURA DE TIPOS:")
        for c in conflitos:
            print("    - " + c)
    elif presentes and tipo not in sugeridos:
        print("\n  ATENÇÃO: nenhum sinal encontrado é típico de %s." % TIPO_NOME[tipo])
        print("    Sugerido pelos sinais: %s" % ", ".join(sorted(TIPO_NOME[t] for t in sugeridos)))
    else:
        print("\n  Nenhuma mistura de tipos detectada.")

    return bool(conflitos)


def main():
    if not os.path.exists("index.html"):
        sys.exit("Rode a partir da raiz do repositório govhub-roadmap.")
    if len(sys.argv) < 2:
        sys.exit(__doc__)

    boxes = carregar_boxes()

    if sys.argv[1] == "--todos":
        print("Varredura dos %d documentos ('!!' = mistura de tipos)\n" % len(boxes))
        com_problema = 0
        for slug in sorted(boxes):
            if diagnosticar(slug, boxes[slug], verboso=False):
                com_problema += 1
        print("\n%d documento(s) com mistura de tipos." % com_problema)
        return

    slug = resolver(sys.argv[1], boxes)
    if not slug:
        sys.exit("Não achei documento para '%s'." % sys.argv[1])
    diagnosticar(slug, boxes[slug])


if __name__ == "__main__":
    main()
