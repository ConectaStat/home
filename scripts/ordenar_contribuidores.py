# -*- coding: utf-8 -*-
"""Coloca os docentes no topo da lista de contribuidores e regenera a tabela
do README.

O all-contributors nao tem ideia de grupos: ele escreve a tabela na ordem em
que as pessoas aparecem no .all-contributorsrc. Este script reordena esse
arquivo em dois blocos, preservando a ordem de entrada dentro de cada um:

    1. quem tem a contribuicao "coordenacao"
    2. todos os demais

Depois basta rodar `npx all-contributors-cli generate` para a tabela do README
sair na ordem nova. Os workflows fazem isso sozinhos; para rodar a mao:

    python scripts/ordenar_contribuidores.py && npx all-contributors-cli generate
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
ARQ = RAIZ / ".all-contributorsrc"

ORDEM = ["coordenacao"]


def posicao(pessoa: dict) -> int:
    """0 para quem coordena, 1 para os demais."""
    tipos = pessoa.get("contributions", [])
    for i, marca in enumerate(ORDEM):
        if marca in tipos:
            return i
    return len(ORDEM)


def main() -> int:
    if not ARQ.exists():
        print("[!!] .all-contributorsrc não encontrado")
        return 1

    dados = json.loads(ARQ.read_text(encoding="utf-8"))
    pessoas = dados.get("contributors", [])
    antes = [p.get("login") for p in pessoas]

    # sorted é estável: quem já estava antes continua antes dentro do bloco
    dados["contributors"] = sorted(pessoas, key=posicao)
    depois = [p.get("login") for p in dados["contributors"]]

    if antes == depois:
        print("[ordenar_contribuidores] a ordem já estava correta.")
        return 0

    ARQ.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8", newline="\n")
    coord = sum(1 for p in dados["contributors"] if "coordenacao" in p.get("contributions", []))
    print(f"[ordenar_contribuidores] lista reordenada: {coord} na coordenação no topo, "
          f"{len(depois)} pessoa(s) no total.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
