# -*- coding: utf-8 -*-
"""Monta a pasta de um projeto de Organizacao e Apresentacao de Dados a partir
da issue enviada pelo formulario "Envie seu projeto".

Chamado pelo workflow .github/workflows/publicar-projeto.yml quando a issue
recebe a etiqueta "aprovado". Le o corpo da issue (gerado pelo modelo
.github/ISSUE_TEMPLATE/submissao-projeto.yml), cria

    projetos/ensino/organizacao-e-apresentacao-de-dados/posts/AAAA-MM-DD-slug/
    ├── index.qmd
    ├── thumbnail.png            (se a pessoa anexou)
    └── relatorios/
        ├── relatorio.html
        └── apresentacao.html    (se houver um segundo arquivo)

e imprime o slug no GITHUB_OUTPUT, para o workflow abrir o pull request.

Uso:
    python scripts/publicar_projeto.py issue.json
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
SECAO = RAIZ / "projetos" / "ensino" / "organizacao-e-apresentacao-de-dados"

# Rotulos do modelo de issue, na ordem em que aparecem no corpo
CAMPOS = {
    "titulo": "Título do projeto",
    "autor": "Autor(es)",
    "resumo": "Resumo da análise",
    "linguagem": "Linguagem de programação",
    "formato": "Formato do relatório",
    "codigo": "O código aparece no documento?",
    "fonte": "Fonte dos dados (vira tag do post)",
    "relatorio": "Relatório: link no GitHub OU arquivo anexado",
    "thumbnail": "Imagem para thumbnail (opcional)",
    "repositorio": "Repositório no GitHub (opcional)",
}

VAZIO = {"", "_no response_", "_nenhuma resposta_", "n/a", "-"}


# ---------------------------------------------------------------- leitura
def separa_campos(corpo: str) -> dict[str, str]:
    """Quebra o corpo da issue nos blocos '### Rotulo' que o formulario gera."""
    blocos: dict[str, str] = {}
    atual = None
    linhas: list[str] = []
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

    saida = {}
    for chave, rotulo in CAMPOS.items():
        valor = blocos.get(rotulo, "").strip()
        saida[chave] = "" if valor.lower() in VAZIO else valor
    return saida


def slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return re.sub(r"-{2,}", "-", t)[:60] or "projeto"


def urls_em(texto: str) -> list[str]:
    """Todos os endereços citados no campo, sejam links markdown ou soltos."""
    achados = re.findall(r"https?://[^\s)>\]]+", texto or "")
    limpos = []
    for u in achados:
        u = u.rstrip(".,;")
        if u not in limpos:
            limpos.append(u)
    return limpos


def para_raw(url: str) -> str:
    """Converte link de página do GitHub em link do arquivo cru."""
    if "github.com" in url and "/blob/" in url:
        return url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    return url


def baixa(url: str) -> bytes:
    req = urllib.request.Request(para_raw(url), headers={"User-Agent": "conexao-estatistica-bot"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


# ---------------------------------------------------------------- anexos
def guarda_relatorios(campo: str, destino: Path) -> list[str]:
    """Baixa o relatório (HTML, PDF ou ZIP) e devolve os nomes gravados."""
    destino.mkdir(parents=True, exist_ok=True)
    gravados: list[str] = []

    for url in urls_em(campo):
        try:
            dados = baixa(url)
        except Exception as e:
            print(f"[!!] não consegui baixar {url}: {e}")
            continue

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


def guarda_thumbnail(campo: str, pasta: Path) -> bool:
    for url in urls_em(campo):
        if url.split("?")[0].lower().endswith((".png", ".jpg", ".jpeg", ".webp")) or "user-attachments" in url:
            try:
                (pasta / "thumbnail.png").write_bytes(baixa(url))
                return True
            except Exception as e:
                print(f"[!!] thumbnail não baixou: {e}")
    return False


# ---------------------------------------------------------------- post
def categorias(dados: dict[str, str]) -> str:
    itens = ["Análise de dados"]
    ling = dados.get("linguagem", "")
    for nome in ("R", "Python", "Julia", "SQL"):
        if re.search(rf"\b{nome}\b", ling, re.I) and nome not in itens:
            itens.append(nome)
    fonte = dados.get("fonte", "").strip()
    if fonte:
        itens.append(f'"{fonte}"' if not fonte.startswith('"') else fonte)
    return "[" + ", ".join(itens) + "]"


def monta_index(dados, gravados, tem_thumb, quando) -> str:
    titulo = dados["titulo"].replace('"', "'")
    principal = "relatorio.pdf" if "relatorio.pdf" in gravados else "relatorio.html"

    cabecalho = [
        "---",
        f'title: "{titulo}"',
        f'description: "{" ".join(dados["resumo"].split())[:300].replace(chr(34), chr(39))}"',
        f'author: "{dados["autor"]}"',
        f'date: "{quando}"',
    ]
    if tem_thumb:
        cabecalho.append('image: "thumbnail.png"')
    cabecalho += [f"categories: {categorias(dados)}", "---", ""]

    corpo = [
        "```{=html}",
        '<a class="btn-voltar" href="../../index.html"',
        '   onclick="if (document.referrer && new URL(document.referrer).origin === location.origin)'
        " { history.back(); return false; }\">",
        '  <i class="bi bi-arrow-left"></i> Voltar',
        "</a>",
        "```",
        "",
        dados["resumo"],
        "",
        "```{=html}",
        '<div class="report-nativo">',
        f'  <iframe src="relatorios/{principal}"',
        f'          title="Relatório: {titulo}"></iframe>',
        "</div>",
        "",
        '<div class="projeto-links">',
        f'  <a href="relatorios/{principal}" target="_blank" rel="noopener">',
        '    <i class="bi bi-arrows-fullscreen"></i> Relatório em tela cheia',
        "  </a>",
    ]
    if "apresentacao.html" in gravados:
        corpo += [
            '  <a href="relatorios/apresentacao.html" target="_blank" rel="noopener">',
            '    <i class="bi bi-easel"></i> Apresentação de slides',
            "  </a>",
        ]
    repo = (urls_em(dados.get("repositorio", "")) or [""])[0]
    if repo:
        corpo += [
            f'  <a href="{repo}" target="_blank" rel="noopener">',
            '    <i class="bi bi-github"></i> Código-fonte no GitHub',
            "  </a>",
        ]
    corpo += ["</div>", "```", ""]
    return "\n".join(cabecalho + corpo)


def anota(chave: str, valor: str) -> None:
    saida = os.environ.get("GITHUB_OUTPUT")
    if saida:
        with open(saida, "a", encoding="utf-8") as f:
            f.write(f"{chave}={valor}\n")


def main() -> int:
    issue = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    dados = separa_campos(issue.get("body", ""))

    if not dados["titulo"] or not dados["resumo"]:
        print("[!!] a issue não tem título ou resumo: nada a publicar")
        return 1

    quando = (issue.get("created_at") or "")[:10] or date.today().isoformat()
    nome = f"{quando}-{slug(dados['titulo'])}"
    pasta = SECAO / "posts" / nome
    pasta.mkdir(parents=True, exist_ok=True)

    gravados = guarda_relatorios(dados["relatorio"], pasta / "relatorios")
    if not gravados:
        print("[!!] nenhum relatório foi baixado: confira o link ou o anexo da issue")
        return 1
    tem_thumb = guarda_thumbnail(dados["thumbnail"], pasta)

    (pasta / "index.qmd").write_text(monta_index(dados, gravados, tem_thumb, quando),
                                     encoding="utf-8", newline="\n")

    print(f"[ok] {nome}: {', '.join(gravados)}" + (", thumbnail.png" if tem_thumb else ""))
    anota("slug", nome)
    anota("titulo", dados["titulo"])
    anota("autor_post", dados["autor"])
    anota("caminho", (pasta.relative_to(RAIZ)).as_posix())
    anota("capa", "sim" if tem_thumb else "nao")
    return 0


if __name__ == "__main__":
    sys.exit(main())
