# -*- coding: utf-8 -*-
"""Descobre quais tipos de contribuicao uma submissao gera.

Le a issue aberta por um dos formularios de .github/ISSUE_TEMPLATE e devolve
os tipos do all-contributors:

  * quem se identifica como Docente ganha "coordenacao", a marca de quem
    conduz o projeto;
  * toda submissao publicada rende "content", que e a contribuicao em si.

Um docente que envia um software fica com coordenacao e content. Um discente
que envia uma analise fica com content. As marcas se acumulam ao longo do
tempo, sem nunca substituir as anteriores.

Uso:
    python scripts/creditar_submissao.py issue.json
"""
import json
import os
import re
import sys
from pathlib import Path


def campo(corpo: str, rotulo_inicio: str) -> str:
    """Valor do bloco '### Rotulo' cujo titulo comeca com o texto dado."""
    atual, linhas, blocos = None, [], {}
    for linha in (corpo or "").splitlines():
        m = re.match(r"^#{2,4}\s+(.*?)\s*$", linha)
        if m:
            if atual:
                blocos[atual] = "\n".join(linhas).strip()
            atual, linhas = m.group(1), []
        elif atual:
            linhas.append(linha)
    if atual:
        blocos[atual] = "\n".join(linhas).strip()

    alvo = rotulo_inicio.lower()
    for titulo, valor in blocos.items():
        if titulo.lower().startswith(alvo):
            return valor.strip()
    return ""


def main() -> int:
    issue = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    corpo = issue.get("body", "")

    tipos = []
    vinculo = (campo(corpo, "seu vínculo") or campo(corpo, "seu vinculo")).lower()
    if "docente" in vinculo:
        tipos.append("coordenacao")
    tipos.append("content")

    tipos = list(dict.fromkeys(tipos))
    print(",".join(tipos))

    saida = os.environ.get("GITHUB_OUTPUT")
    if saida:
        with open(saida, "a", encoding="utf-8") as f:
            f.write(f"tipos={','.join(tipos)}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
