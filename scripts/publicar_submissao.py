# -*- coding: utf-8 -*-
"""Transforma uma submissao do formulario "Envie seu projeto" na pasta do post.

Le a issue gerada por .github/ISSUE_TEMPLATE/submissao.yml, confere a area
pelo campo "Onde isso deve ser publicado?", preenche o modelo correspondente
de _templates/areas/ e escreve:

    <area>/posts/AAAA-MM-DD-slug/
    ├── index.qmd
    ├── thumbnail.png          (se a pessoa anexou)
    └── relatorios/            (se a pessoa mandou um documento)
        ├── relatorio.html
        └── apresentacao.html

Hoje a unica area com submissao aberta e Organizacao e Apresentacao de Dados
(ver AREAS, abaixo), e nela o relatorio e obrigatorio: a pagina o exibe
embutido, em vez de so apontar um link.

Nos modelos, {{campo}} e substituido pelo valor e os trechos entre
<!--se:campo--> e <!--/se--> somem quando o campo vem vazio.

Uso:
    python scripts/publicar_submissao.py issue.json
"""
from __future__ import annotations

import json
import os
import re
import sys
import unicodedata
import urllib.request
import zipfile
from datetime import date
from io import BytesIO
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
MODELOS = RAIZ / "_templates" / "areas"

# area escolhida no formulario -> pasta de destino, modelo e categorias fixas
#
# So Organizacao e Apresentacao de Dados passa pelo robo: e a unica secao com
# submissao aberta ao publico. As demais sao publicadas a mao pela equipe, com
# os modelos de _templates/areas/ - o caminho esta em sobre/como-contribuir/
# e na secao "Publicar em cada area" do README.
AREAS = {
    "projeto de estudante": ("projetos/ensino/organizacao-e-apresentacao-de-dados/posts",
                             "projeto-estudante.qmd", ["Análise de dados"]),
}

VAZIO = {"", "_no response_", "_nenhuma resposta_", "n/a", "-", "nenhum"}


# ---------------------------------------------------------------- leitura
def separa_campos(corpo: str) -> dict[str, str]:
    """Cada '### Rotulo' do corpo da issue vira uma entrada do dicionario."""
    blocos, atual, linhas = {}, None, []
    for linha in (corpo or "").splitlines():
        m = re.match(r"^#{2,4}\s+(.*?)\s*$", linha)
        if m:
            if atual:
                blocos[atual] = "\n".join(linhas).strip()
            atual, linhas = m.group(1).strip().lower(), []
        elif atual:
            linhas.append(linha)
    if atual:
        blocos[atual] = "\n".join(linhas).strip()
    return {k: ("" if v.lower() in VAZIO else v) for k, v in blocos.items()}


def campo(blocos: dict, inicio: str) -> str:
    for titulo, valor in blocos.items():
        if titulo.startswith(inicio.lower()):
            return valor
    return ""


def descobre_area(texto: str):
    t = (texto or "").lower()
    for chave, destino in AREAS.items():
        if chave in t:
            return chave, destino
    return None, None


def slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return re.sub(r"-{2,}", "-", t)[:60] or "publicacao"


def urls_em(texto: str) -> list[str]:
    achados, limpos = re.findall(r"https?://[^\s)>\]]+", texto or ""), []
    for u in achados:
        u = u.rstrip(".,;")
        if u not in limpos:
            limpos.append(u)
    return limpos


def baixa(url: str) -> bytes:
    if "github.com" in url and "/blob/" in url:
        url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    req = urllib.request.Request(url, headers={"User-Agent": "conexao-estatistica-bot"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


# ---------------------------------------------------------------- anexos
def guarda_relatorios(texto: str, destino: Path) -> list[str]:
    gravados: list[str] = []
    for url in urls_em(texto):
        try:
            dados = baixa(url)
        except Exception as e:
            print(f"[!!] não baixei {url}: {e}")
            continue
        destino.mkdir(parents=True, exist_ok=True)
        nome = url.split("/")[-1].split("?")[0].lower()
        if nome.endswith(".zip") or dados[:2] == b"PK":
            with zipfile.ZipFile(BytesIO(dados)) as z:
                htmls = [n for n in z.namelist()
                         if n.lower().endswith((".html", ".htm")) and not n.startswith("__MACOSX")]
                htmls.sort(key=lambda n: ("apresenta" in n.lower(), len(n)))
                for i, interno in enumerate(htmls[:2]):
                    alvo = "relatorio.html" if i == 0 else "apresentacao.html"
                    (destino / alvo).write_bytes(z.read(interno))
                    gravados.append(alvo)
        elif nome.endswith((".html", ".htm")):
            alvo = "apresentacao.html" if ("apresenta" in nome or "slide" in nome) and gravados else "relatorio.html"
            (destino / alvo).write_bytes(dados)
            gravados.append(alvo)
        elif nome.endswith(".pdf"):
            (destino / "relatorio.pdf").write_bytes(dados)
            gravados.append("relatorio.pdf")
    return gravados


def guarda_capa(texto: str, pasta: Path) -> bool:
    for url in urls_em(texto):
        if url.split("?")[0].lower().endswith((".png", ".jpg", ".jpeg", ".webp")) or "user-attachments" in url:
            try:
                (pasta / "thumbnail.png").write_bytes(baixa(url))
                return True
            except Exception as e:
                print(f"[!!] capa não baixou: {e}")
    return False


# ---------------------------------------------------------------- modelo
def preenche(modelo: str, valores: dict[str, str]) -> str:
    """Remove os blocos <!--se:campo--> vazios e troca os {{campo}}."""
    def bloco(m):
        return m.group(2) if valores.get(m.group(1), "").strip() else ""
    texto = re.sub(r"<!--se:(\w+)-->(.*?)<!--/se-->", bloco, modelo, flags=re.S)
    for chave, valor in valores.items():
        texto = texto.replace("{{" + chave + "}}", valor)
    return re.sub(r"\n{3,}", "\n\n", texto).strip() + "\n"


def anota(chave: str, valor: str) -> None:
    saida = os.environ.get("GITHUB_OUTPUT")
    if saida:
        with open(saida, "a", encoding="utf-8") as f:
            f.write(f"{chave}={valor}\n")


def main() -> int:
    issue = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    blocos = separa_campos(issue.get("body", ""))

    nome_area, destino = descobre_area(campo(blocos, "onde isso deve"))
    if not destino:
        print("[!!] área não automatizada: o robô só publica em Organização e "
              "Apresentação de Dados. As demais seções são publicadas à mão "
              "pela equipe (ver sobre/como-contribuir/).")
        return 1
    pasta_area, modelo, cats_fixas = destino

    titulo = campo(blocos, "título")
    resumo = campo(blocos, "resumo")
    if not titulo or not resumo:
        print("[!!] a submissão está sem título ou sem resumo")
        return 1

    data = campo(blocos, "data")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", data or ""):
        data = (issue.get("created_at") or "")[:10] or date.today().isoformat()

    # Se já existir pasta com esse nome (mesmo título na mesma data), o número
    # da issue desempata: sem isso a branch colidiria com a de outra submissão.
    base = RAIZ / pasta_area / f"{data}-{slug(titulo)}"
    pasta = base
    if pasta.exists():
        numero = issue.get("number")
        pasta = base.with_name(f"{base.name}-{numero}" if numero else f"{base.name}-2")
        print(f"[..] já havia {base.name}: usando {pasta.name}")
    pasta.mkdir(parents=True, exist_ok=True)

    # anexos: qualquer área pode mandar um documento para ficar embutido na
    # página. Só projeto de estudante exige um: sem relatório não há projeto.
    gravados = guarda_relatorios(campo(blocos, "documento"), pasta / "relatorios")
    if nome_area == "projeto de estudante" and not gravados:
        print("[!!] projeto de estudante sem relatório: confira o link ou o anexo")
        return 1
    tem_capa = guarda_capa(campo(blocos, "imagem de capa"), pasta)

    # categorias: as fixas da área mais as que a pessoa escreveu
    extras = [c.strip() for c in campo(blocos, "categorias").split(",") if c.strip()]
    cats = cats_fixas + [c for c in extras if c not in cats_fixas]
    cats_fmt = ", ".join(f'"{c}"' if ("," in c or "(" in c) else c for c in cats)

    valores = {
        "titulo": titulo.replace('"', "'"),
        "resumo": " ".join(resumo.split())[:300].replace('"', "'"),
        "autor": campo(blocos, "autoria").replace('"', "'"),
        "data": data,
        "texto": campo(blocos, "texto da publicação") or resumo,
        "categorias": cats_fmt,
        "link": (urls_em(campo(blocos, "link principal")) or [""])[0],
        "repositorio": (urls_em(campo(blocos, "repositório")) or [""])[0],
        "thumbnail": "sim" if tem_capa else "",
        # Documento embutido. HTML e PDF sao exibidos de formas diferentes: o
        # HTML entra num <iframe>, que o JS mede e indexa; o PDF depende do
        # visualizador do navegador, que falha em boa parte dos celulares,
        # entao vai num <object> com link de saida no lugar quando falha.
        "relatorio": f"relatorios/{gravados[0]}" if gravados else "",
        "relatorio_html": "sim" if gravados and gravados[0].endswith((".html", ".htm")) else "",
        "relatorio_pdf": "sim" if gravados and gravados[0].endswith(".pdf") else "",
        "apresentacao": "sim" if "apresentacao.html" in gravados else "",
    }

    conteudo = preenche((MODELOS / modelo).read_text(encoding="utf-8"), valores)
    (pasta / "index.qmd").write_text(conteudo, encoding="utf-8", newline="\n")

    rel = pasta.relative_to(RAIZ).as_posix()
    print(f"[ok] {nome_area}: {rel}" + (f" ({', '.join(gravados)})" if gravados else ""))
    anota("slug", pasta.name)
    anota("titulo", titulo)
    anota("area", nome_area)
    anota("caminho", rel)
    anota("capa", "sim" if tem_capa else "nao")
    return 0


if __name__ == "__main__":
    sys.exit(main())
