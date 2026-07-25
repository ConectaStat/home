# -*- coding: utf-8 -*-
"""Gera TEXTOS.md: inventario de todo o texto editavel do site, em arvore,
para revisao. Le os .qmd e o _quarto.yml e escreve os textos como blocos de
citacao, prontos para o revisor reescrever.

Registrado como `post-render` no _quarto.yml: roda sozinho a cada
`quarto render` (inclusive no deploy automatico), de modo que o TEXTOS.md
nunca fica defasado em relacao ao site. So reescreve o arquivo quando algo
mudou de fato.

Uso manual, se precisar:
    python scripts/gerar_textos.py
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------- utilidades
def le(p: Path) -> str:
    return p.read_text(encoding="utf-8")

def separa(texto):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", texto, re.S)
    return (m.group(1), m.group(2)) if m else ("", texto)

def campo(fm, nome):
    m = re.search(rf'(?m)^{nome}:\s*"?(.*?)"?\s*$', fm)
    if not m:
        return None
    v = m.group(1).strip()
    return v if v and v not in ("true", "false") else None

def limpa_corpo(corpo: str) -> str:
    """Remove blocos HTML/JS, comentarios e cercas de div, deixando so a prosa."""
    corpo = re.sub(r"```\{=html\}.*?```", "", corpo, flags=re.S)
    corpo = re.sub(r"```.*?```", "", corpo, flags=re.S)
    corpo = re.sub(r"<!--.*?-->", "", corpo, flags=re.S)
    corpo = re.sub(r"(?m)^:::.*$", "", corpo)
    corpo = re.sub(r"(?m)^\s*: \{tbl-colwidths.*$", "", corpo)
    corpo = re.sub(r"\n{3,}", "\n\n", corpo)
    return corpo.strip()

def citacao(texto: str) -> str:
    if not texto.strip():
        return "> *(sem texto próprio — a página só exibe a listagem)*"
    return "\n".join("> " + l if l.strip() else ">" for l in texto.split("\n"))

# ---------------------------------------------------------------- home
def blocos_home():
    txt = le(RAIZ / "index.qmd")
    fm, corpo = separa(txt)
    saida = []

    # hero: tagline + disclaimer
    tag = re.findall(r'<span[^>]*>([^<]+)<span class="tag-barra">/</span></span>|<span>([^<]+)<span class="hero-cursor"', txt)
    linhas = [a or b for a, b in tag]
    disc = re.search(r'<p class="hero-disclaimer">(.*?)</p>', txt, re.S)
    saida.append(("Hero (topo da home)",
                  "Slogan sobre a ilustração:\n\n" +
                  "\n".join(f"  {l}/" if i < 2 else f"  {l}" for i, l in enumerate(linhas))))
    if disc:
        saida.append(("Disclaimer abaixo da hero", " ".join(disc.group(1).split())))

    # secoes: corta o corpo limpo em pedacos que comecam com "## "
    for pedaco in re.split(r"(?m)^(?=## )", limpa_corpo(corpo)):
        pedaco = pedaco.strip()
        if not pedaco.startswith("## "):
            continue
        linhas = pedaco.split("\n")
        titulo = linhas[0][3:].strip()
        resto = "\n".join(linhas[1:]).strip()
        sub = re.match(r"^\[(.+?)\]\{\.sec-sub\}\s*(.*)$", resto, re.S)
        bloco = ""
        if sub:
            bloco += f"Subtítulo: {sub.group(1).strip()}"
            corpo_sec = sub.group(2).strip()
            if corpo_sec:
                bloco += "\n\n" + corpo_sec
        else:
            bloco = resto
        saida.append((f"Seção da home: {titulo}", bloco.strip()))

    # endereco do mapa (esta dentro do HTML)
    end = re.search(r'<h3><i class="bi bi-geo-alt-fill"></i> (.*?)</h3>\s*<p>\s*(.*?)\s*</p>', txt, re.S)
    if end:
        linhas = [l.strip() for l in re.sub(r"<br/?>", "\n", end.group(2)).split("\n") if l.strip()]
        saida.append(("Bloco do mapa (endereço)", end.group(1).strip() + "\n" + "\n".join(linhas)))
    return saida

def rodape_menu():
    y = le(RAIZ / "_quarto.yml")
    disc = re.search(r"\[(.*?)\]\{\.footer-disclaimer\}", y, re.S)
    des = re.search(r'footer-des-sigla">(.*?)</span><span class="footer-des-nome">(.*?)</span>', y)
    # itens do menu preservando a hierarquia (indentacao maior = submenu)
    nav = y.split("navbar:", 1)[1].split("page-navigation:", 1)[0]
    itens, base = [], None
    for m in re.finditer(r'(?m)^(\s+)- text: "(.*?)"', nav):
        ident, rotulo = len(m.group(1)), m.group(2)
        if base is None or ident <= base:
            base = ident
            itens.append((0, rotulo))
        else:
            itens.append((1, rotulo))
    return (disc.group(1).strip() if disc else None,
            (des.group(1), des.group(2).replace("<br>", " ")) if des else None,
            itens)

# ---------------------------------------------------------------- paginas
# ordem de leitura = ordem do site
ORDEM = [
    ("Estatística", "estatistica/index.qmd", []),
    ("Nossos Cursos › Graduação", "cursos/graduacao/index.qmd", []),
    ("Nossos Cursos › Pós-Graduação", "cursos/pos-graduacao/index.qmd", []),
    ("Nossos Cursos › Pós-Graduação › Painel dos Egressos", "cursos/pos-graduacao/egressos/index.qmd", []),
    ("Projetos › Ensino", "projetos/ensino/index.qmd", ["topicos-ensino"]),
    ("Projetos › Ensino › Organização e Apresentação de Dados", "projetos/ensino/organizacao-e-apresentacao-de-dados/index.qmd", []),
    ("Projetos › Ensino › Organização… › Envie seu projeto", "projetos/ensino/organizacao-e-apresentacao-de-dados/enviar.qmd", []),
    ("Projetos › Ensino › Softwares", "projetos/ensino/softwares/index.qmd", []),
    ("Projetos › Ensino › Materiais", "projetos/ensino/materiais/index.qmd", []),
    ("Projetos › Ensino › Editais", "projetos/ensino/editais/index.qmd", []),
    ("Projetos › Pesquisa", "projetos/pesquisa/index.qmd", ["topicos-pesquisa"]),
    ("Projetos › Pesquisa › Núcleos de Pesquisa", "projetos/pesquisa/nucleos/index.qmd", []),
    ("Projetos › Pesquisa › Núcleos › NLIN", "projetos/pesquisa/nucleos/nlin/index.qmd", []),
    ("Projetos › Pesquisa › Núcleos › GPS", "projetos/pesquisa/nucleos/gps/index.qmd", []),
    ("Projetos › Pesquisa › Núcleos › ST", "projetos/pesquisa/nucleos/st/index.qmd", []),
    ("Projetos › Pesquisa › Editais", "projetos/pesquisa/editais/index.qmd", []),
    ("Projetos › Extensão", "projetos/extensao/index.qmd", ["topicos-extensao"]),
    ("Projetos › Extensão › Editais", "projetos/extensao/editais/index.qmd", []),
    ("Ações › Revista Científica", "acoes/revista-cientifica/index.qmd", []),
    ("Ações › Assessoria e Consultoria Estatística", "assessoria/index.qmd", []),
    ("Ações › Eventos (arquivo)", "eventos/index.qmd", []),
    ("Notícias (arquivo)", "noticias/index.qmd", []),
    ("Oportunidades (arquivo)", "oportunidades/index.qmd", []),
    ("Artigos & Colunas (arquivo)", "artigos/index.qmd", []),
    ("Contato", "contato.qmd", []),
]

def cards_do_frontmatter(fm):
    """Extrai os cards de tópico declarados no cabeçalho (Projetos)."""
    itens = re.findall(r'- title: "(.*?)"\s*\n\s*description: "(.*?)"', fm)
    return itens

def bloco_pagina(rotulo, rel, ids):
    p = RAIZ / rel
    if not p.exists():
        return f"\n### {rotulo}\n\n*(arquivo não encontrado: {rel})*\n"
    fm, corpo = separa(le(p))
    out = [f"\n### {rotulo}", f"`{rel}`", ""]
    t, s, d = campo(fm, "title"), campo(fm, "subtitle"), campo(fm, "description")
    out.append(f"**Título (aparece no banner):** {t}" if t else "**Título:** —")
    if s:
        out.append(f"\n**Subtítulo:** {s}  \n*(hoje oculto no site; fica só no código)*")
    if d:
        out.append(f"\n**Descrição (para buscadores/compartilhamento):** {d}")
    corpo_limpo = limpa_corpo(corpo)
    out.append("\n**Texto da página:**\n")
    out.append(citacao(corpo_limpo))
    cards = cards_do_frontmatter(fm)
    if cards:
        out.append("\n**Cards de tópico desta página:**\n")
        for tit, desc in cards:
            out.append(f"> **{tit}**  \n> {desc}\n>")
    return "\n".join(out) + "\n"

def bloco_posts(rotulo, pasta):
    base = RAIZ / pasta
    posts = sorted(base.glob("*/index.qmd"), reverse=True)
    if not posts:
        return ""
    out = [f"\n### {rotulo} — posts publicados ({len(posts)})\n"]
    for p in posts:
        fm, corpo = separa(le(p))
        out.append(f"\n#### {campo(fm,'title')}")
        out.append(f"`{p.relative_to(RAIZ).as_posix()}`\n")
        if campo(fm, "description"):
            out.append(f"**Resumo (aparece no card):** {campo(fm,'description')}\n")
        out.append(citacao(limpa_corpo(corpo)))
    return "\n".join(out) + "\n"

# ---------------------------------------------------------------- montagem
L = []
L.append("""# Mapa de textos do site

Inventário de **todo o texto editável** do Conexão Estatística, na ordem em que
o visitante encontra. Serve para revisão: reescreva o que quiser dentro dos
blocos citados e devolva — cada bloco indica o arquivo exato onde ele mora.

Está tudo aqui: títulos, textos corridos, tabelas e os resumos que aparecem nos
cards. Ficam de fora apenas os relatórios enviados pelos estudantes, que são
conteúdo de terceiros e não devem ser reescritos.

**Como devolver correções:** copie o trecho que quiser mudar, reescreva e
devolva indicando o arquivo (cada bloco traz o caminho logo abaixo do título).
Não precisa se preocupar com formatação — negrito, links e acentos são
ajustados na hora de aplicar.

Este documento é gerado a partir dos arquivos do site. Depois de aplicar
correções, refaça com:

```bash
python scripts/gerar_textos.py
```

---

## Mapa do site

```
home/
├── index.qmd ─────────────────── página inicial ................. §1
│   ├── hero ........................ slogan sobre a ilustração
│   ├── disclaimer .................. logo abaixo da hero
│   ├── "O que é o Conexão…" ........ texto de apresentação
│   ├── notícias · oportunidades · eventos ... carrosséis
│   └── onde estamos ................ mapa + endereço
├── _quarto.yml ───────────────── rodapé e menu ................. §2 e §3
│
├── estatistica/index.qmd ─────── Estatística .................... §4
├── assessoria/index.qmd ──────── Assessoria e Consultoria
├── acoes/
│   └── revista-cientifica/index.qmd ── Revista Científica
├── cursos/
│   ├── graduacao/index.qmd ─────── Graduação
│   └── pos-graduacao/
│       ├── index.qmd ───────────── Pós-Graduação
│       └── egressos/index.qmd ──── Painel dos Egressos
├── projetos/
│   ├── ensino/
│   │   ├── index.qmd ───────────── Projetos de Ensino (+ cards de tópico)
│   │   ├── organizacao-e-apresentacao-de-dados/
│   │   │   ├── index.qmd ───────── Organização e Apresentação de Dados
│   │   │   ├── enviar.qmd ──────── Envie seu projeto
│   │   │   └── posts/ ──────────── 5 projetos publicados ....... §5
│   │   ├── softwares/index.qmd ─── Softwares (sem conteúdo ainda)
│   │   ├── materiais/index.qmd ─── Materiais (sem conteúdo ainda)
│   │   └── editais/index.qmd ───── Editais de Ensino
│   ├── pesquisa/
│   │   ├── index.qmd ───────────── Projetos de Pesquisa (+ cards)
│   │   ├── nucleos/
│   │   │   ├── index.qmd ───────── Núcleos de Pesquisa
│   │   │   └── nlin/ gps/ st/ ──── um index.qmd por núcleo
│   │   └── editais/index.qmd ───── Editais de Pesquisa
│   └── extensao/
│       ├── index.qmd ───────────── Projetos de Extensão (+ cards)
│       └── editais/index.qmd ───── Editais de Extensão
│
├── noticias/       ┐
├── oportunidades/  │  cada uma com:
├── eventos/        │    index.qmd ── página de arquivo ......... §4
├── artigos/        ┘    posts/ ───── conteúdo datado ........... §5
│
└── contato.qmd ───────────────── Contato
```

---
""")

# ---- home
L.append("## 1. Página inicial\n")
L.append("```\nindex.qmd\n├── hero .................. slogan + ilustração\n"
         "├── disclaimer ............ abaixo da hero\n"
         "├── o projeto ............. texto de apresentação\n"
         "├── notícias .............. carrossel\n"
         "├── oportunidades ......... carrossel\n"
         "├── eventos ............... carrossel\n"
         "└── onde estamos .......... mapa + endereço\n```\n")
for titulo, texto in blocos_home():
    L.append(f"\n### {titulo}\n")
    L.append(citacao(texto))
    L.append("")

# ---- rodape e menu
disc, des, itens = rodape_menu()
L.append("\n---\n\n## 2. Rodapé (todas as páginas)\n")
L.append("`_quarto.yml` › `website: page-footer`\n")
if disc:
    L.append("\n**Disclaimer (canto esquerdo):**\n")
    L.append(citacao(disc))
if des:
    L.append("\n**Assinatura institucional (canto direito):**\n")
    L.append(citacao(f"{des[0]}\n{des[1]}\n\n(ao lado da marca da UFLA)"))
L.append("\n**Ícones:** GitHub, Instagram e LinkedIn (os dois últimos ainda sem link).\n")

L.append("\n---\n\n## 3. Menu do topo\n")
L.append("`_quarto.yml` › `website: navbar`\n")
L.append("\n```")
L.append("Ciência/ Estatística/ Conexão   ← slogan à esquerda (leva à home)")
L.append("")
for nivel, rotulo in itens:
    L.append(("  " if nivel == 0 else "      └── ") + rotulo)
L.append("```\n")

# ---- paginas
L.append("\n---\n\n## 4. Páginas das seções\n")
for rotulo, rel, ids in ORDEM:
    L.append(bloco_pagina(rotulo, rel, ids))

# ---- posts
L.append("\n---\n\n## 5. Conteúdo datado (posts já publicados)\n")
for rotulo, pasta in [
    ("Notícias", "noticias/posts"),
    ("Oportunidades", "oportunidades/posts"),
    ("Eventos", "eventos/posts"),
    ("Artigos & Colunas", "artigos/posts"),
    ("Organização e Apresentação de Dados", "projetos/ensino/organizacao-e-apresentacao-de-dados/posts"),
]:
    L.append(bloco_posts(rotulo, pasta))

# Só escreve se algo mudou: rodando como post-render do Quarto, isso evita
# reescrever o arquivo a cada render (e qualquer risco de laço no preview).
destino = RAIZ / "TEXTOS.md"
novo = "\n".join(L) + "\n"
atual = destino.read_text(encoding="utf-8") if destino.exists() else None

if novo == atual:
    print("[gerar_textos] TEXTOS.md já está atualizado.")
else:
    destino.write_text(novo, encoding="utf-8", newline="\n")
    print(f"[gerar_textos] TEXTOS.md atualizado ({novo.count(chr(10))} linhas).")
