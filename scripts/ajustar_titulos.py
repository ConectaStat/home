"""Pós-render: troca o separador " – " (meia-risca) que o Quarto insere no
<title> e no og:title/twitter:title de cada página por " | ".

O separador é montado pelo próprio Quarto ("Página – ConectaStat") e não pode
ser configurado nos .qmd; por isso o ajuste é feito aqui, sobre o _site/.
Registrado em _quarto.yml (project > post-render), roda a cada quarto render.
"""

import re
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "_site"

# Relatórios enviados pelos estudantes são conteúdo de terceiros: não tocar.
IGNORAR = "projetos-estudantes/relatorios"

RE_TITLE = re.compile(r"(<title>[^<]*?) – ([^<]*?</title>)")
RE_META = re.compile(
    r'(<meta[^>]*?(?:og|twitter):title[^>]*?content=")([^"]*?) – ([^"]*?")'
)
# "ConectaStat | slogan | ConectaStat" -> "ConectaStat | slogan" (caso da home,
# cujo pagetitle já começa com o nome do site)
RE_DUP = re.compile(r"(<title>)([^<|]+?) \| ([^<]*?) \| \2(</title>)")


def main():
    ajustados = 0
    for arq in SITE.rglob("*.html"):
        if IGNORAR in arq.as_posix():
            continue
        texto = arq.read_text(encoding="utf-8")
        novo = RE_TITLE.sub(r"\1 | \2", texto)
        novo = RE_META.sub(r"\1\2 | \3", novo)
        novo = RE_DUP.sub(r"\1\2 | \3\4", novo)
        if novo != texto:
            arq.write_text(novo, encoding="utf-8")
            ajustados += 1
    print(f"[ajustar_titulos] {ajustados} página(s) com título ajustado.")


if __name__ == "__main__":
    main()
