# -*- coding: utf-8 -*-
"""Acrescenta tipos de contribuicao a uma pessoa, sem apagar os que ela ja tem.

Existe porque o `all-contributors-cli add` SUBSTITUI a lista de tipos da
pessoa em vez de somar: chamado uma vez por tipo, cada chamada apaga a
anterior, e os tipos antigos se perdem.

Aqui a soma e feita direto no .all-contributorsrc, com uniao de conjuntos.
Quem nao esta na lista e criado, com nome e avatar buscados na API publica
do GitHub. Depois basta rodar `all-contributors-cli generate` para a tabela
do README refletir o arquivo.

Uso:
    python scripts/creditar_contribuidor.py <usuario> <tipo>[,<tipo>...]
"""
import json
import sys
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
ARQ = RAIZ / ".all-contributorsrc"


def perfil(login: str) -> dict:
    """Nome e avatar da pessoa, para quem ainda nao esta na lista."""
    try:
        req = urllib.request.Request(
            f"https://api.github.com/users/{login}",
            headers={"User-Agent": "conexao-estatistica-bot",
                     "Accept": "application/vnd.github+json"})
        d = json.loads(urllib.request.urlopen(req, timeout=30).read())
        return {"name": d.get("name") or d["login"],
                "avatar_url": d.get("avatar_url", ""),
                "profile": d.get("blog") or d.get("html_url", "")}
    except Exception as e:
        print(f"[!!] não consegui buscar o perfil de {login} ({e}); uso o mínimo")
        return {"name": login,
                "avatar_url": f"https://github.com/{login}.png",
                "profile": f"https://github.com/{login}"}


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    login = sys.argv[1].strip().lstrip("@")
    novos = [t.strip() for t in sys.argv[2].split(",") if t.strip()]
    if not login or not novos:
        print("[!!] informe o usuário e ao menos um tipo")
        return 1

    dados = json.loads(ARQ.read_text(encoding="utf-8"))
    pessoas = dados.setdefault("contributors", [])

    pessoa = next((p for p in pessoas if p.get("login", "").lower() == login.lower()), None)
    if pessoa is None:
        pessoa = {"login": login, **perfil(login), "contributions": []}
        pessoas.append(pessoa)
        print(f"[novo] {login} entrou na lista")

    antes = list(pessoa.get("contributions", []))
    # união preservando a ordem: o que já existia primeiro, o novo depois
    pessoa["contributions"] = antes + [t for t in novos if t not in antes]

    if pessoa["contributions"] == antes:
        print(f"[ok] {login} já tinha {', '.join(novos)}: nada a mudar")
        return 0

    ARQ.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8", newline="\n")
    ganhos = [t for t in novos if t not in antes]
    print(f"[ok] {login}: +{', '.join(ganhos)} "
          f"(agora com {', '.join(pessoa['contributions'])})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
