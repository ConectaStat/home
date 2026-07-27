"""Pós-render: dois ajustes finos sobre a pasta de saída do site.

1. Título das páginas: troca o separador " – " (meia-risca) que o Quarto
   insere no <title> e no og:title/twitter:title por " | ". O separador é
   montado pelo próprio Quarto ("Página – ConectaStat") e não pode
   ser configurado nos .qmd.

2. Redirecionamentos (aliases): no Windows o Quarto escreve o destino com
   contrabarras ("..\\..\\pagina\\index.html"). Os navegadores toleram, mas
   o arquivo fica diferente do gerado no Linux (CI) e a URL sai torta em
   servidores de preview. Aqui as barras são normalizadas.

Registrado em _quarto.yml (project > post-render), roda a cada quarto render.
"""

import os
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
# Pasta de saída: o Quarto informa a dele; fora do render, vale o output-dir.
SITE = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR") or (RAIZ / "docs"))
if not SITE.is_absolute():
    SITE = RAIZ / SITE

# Relatórios enviados pelos estudantes são conteúdo de terceiros: não tocar.
# Cada projeto guarda os seus em posts/<data>-<slug>/relatorios/.
IGNORAR = "/relatorios/"

RE_TITLE = re.compile(r"(<title>[^<]*?) – ([^<]*?</title>)")
RE_META = re.compile(
    r'(<meta[^>]*?(?:og|twitter):title[^>]*?content=")([^"]*?) – ([^"]*?")'
)
# "ConectaStat | slogan | ConectaStat" -> sem a repetição
# (caso da home, cujo pagetitle já começa com o nome do site)
RE_DUP = re.compile(r"(<title>)([^<|]+?) \| ([^<]*?) \| \2(</title>)")

# Linha "var redirects = {...};" das páginas de alias geradas pelo Quarto
RE_REDIRECT = re.compile(r"(var redirects = \{)(.*?)(\};)", re.S)


def normaliza_redirect(texto: str) -> str:
    """Troca \\ por / apenas dentro do mapa de redirecionamento."""
    return RE_REDIRECT.sub(
        lambda m: m.group(1) + m.group(2).replace("\\\\", "/") + m.group(3),
        texto,
    )


def main():
    titulos, redirects = 0, 0
    for arq in SITE.rglob("*.html"):
        if IGNORAR in arq.as_posix():
            continue
        texto = arq.read_text(encoding="utf-8")

        novo = RE_TITLE.sub(r"\1 | \2", texto)
        novo = RE_META.sub(r"\1\2 | \3", novo)
        novo = RE_DUP.sub(r"\1\2 | \3\4", novo)
        se_titulo_mudou = novo != texto

        depois = normaliza_redirect(novo)
        if depois != novo:
            redirects += 1
        if se_titulo_mudou:
            titulos += 1

        if depois != texto:
            arq.write_text(depois, encoding="utf-8")

    print(f"[ajustar_titulos] {titulos} página(s) com título ajustado, "
          f"{redirects} redirecionamento(s) normalizado(s).")


if __name__ == "__main__":
    main()
