# -*- coding: utf-8 -*-
"""Importa editais novos do site do DES/UFLA para oportunidades/posts/.

Le a lista em https://des.ufla.br/editais (a mesma fonte que hoje alguem da
equipe copia a mao - ver "Publicar em cada area > Oportunidades" no README),
baixa os que ainda nao existem no site e cria a pasta de post de cada um:

    oportunidades/posts/AAAA-MM-DD-slug-do-des/
    └── index.qmd

Cada edital importado recebe `categories: [Oportunidades, Editais]` mais a
area (Ensino, Pesquisa e/ou Extensao) quando o TITULO bate com as palavras em
AREA_PALAVRAS, abaixo. Editais que nao batem com nenhuma - convocacao de
eleicao para chefia, concurso para docente efetivo, professor substituto e
afins - continuam aparecendo em Oportunidades (a listagem geral), mas ficam
de fora das paginas de Ensino/Pesquisa/Extensao: o publico do site e formado
por estudantes e pos-graduandos, e esses editais nao sao uma oportunidade
para eles em a maioria dos casos.

So entram editais publicados dentro de JANELA_DIAS: a pagina de editais do
DES tem anos de historico, e a maior parte ja venceu. Como a lista vem da
mais recente para a mais antiga, a busca para na primeira pagina em que todo
mundo ja e mais velho que a janela.

Cada post importado carrega, comentado no topo do arquivo, o identificador
numerico do edital no site do DES (`<!-- fonte: des-editais-<id> -->`) - e
so por ele que uma proxima execucao reconhece "esse eu ja importei" e pula,
sem precisar de nenhum banco de dados a parte.

Uso:
    python scripts/importar_editais.py             # importa o que faltar
    python scripts/importar_editais.py --dry-run    # so mostra o que faria

Pensado para rodar como o job agendado de
.github/workflows/importar-editais.yml, mas funciona igual na sua maquina.
"""
from __future__ import annotations

import os
import re
import sys
import time
import unicodedata
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / "oportunidades" / "posts"
MODELO = RAIZ / "_templates" / "areas" / "edital.qmd"

FONTE = "https://des.ufla.br/editais"
JANELA_DIAS = 365
PAGINAS_NO_MAXIMO = 6          # trava de seguranca: 6 paginas = 60 editais

# Título do edital -> área(s) de Oportunidades por área do site (ver módulo
# acima). Um edital pode bater em mais de uma; quem não bate em nenhuma
# segue sem área (só na listagem geral).
AREA_PALAVRAS = {
    "Ensino": ["monitor", "monitoria", "docencia voluntaria", "docente voluntario"],
    "Pesquisa": ["mestrado", "doutorado", "ppgee", "iniciacao cientifica",
                 "pos-doutorado", "bolsista de pesquisa", "pibic", "pibiti", "pivic"],
    "Extensao": ["extensao", "proec", "voluntariado"],
}

# Só os 3 primeiros caracteres do mês (sem acento, minúsculo): o site do
# DES ora escreve o mês por extenso ("Maio"), ora abreviado ("Mai") - com
# 3 letras as duas formas caem na mesma chave.
MESES = {
    "jan": 1, "fev": 2, "mar": 3, "abr": 4, "mai": 5, "jun": 6,
    "jul": 7, "ago": 8, "set": 9, "out": 10, "nov": 11, "dez": 12,
}


# ---------------------------------------------------------------- básico
def sem_acento(texto: str) -> str:
    return unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()


def slug(texto: str) -> str:
    t = re.sub(r"[^a-zA-Z0-9]+", "-", sem_acento(texto)).strip("-").lower()
    return re.sub(r"-{2,}", "-", t)[:70] or "edital"


def baixa(url: str) -> str:
    """1 nova tentativa antes de desistir: o site do DES é lento às vezes,
    e uma execução agendada não tem ninguém olhando para tentar de novo."""
    req = urllib.request.Request(url, headers={"User-Agent": "conexao-estatistica-bot"})
    for tentativa in (1, 2):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", errors="replace")
        except Exception:
            if tentativa == 2:
                raise
            time.sleep(2)


def texto_limpo(html: str) -> str:
    t = re.sub(r"<[^>]+>", " ", html)
    t = re.sub(r"&nbsp;", " ", t)
    return " ".join(t.split())


def anota(chave: str, valor: str) -> None:
    saida = os.environ.get("GITHUB_OUTPUT")
    if saida:
        with open(saida, "a", encoding="utf-8") as f:
            f.write(f"{chave}={valor}\n")


# ---------------------------------------------------------------- listagem
def pagina_da_lista(indice: int) -> str:
    return FONTE if indice == 0 else f"{FONTE}?start={indice * 10}"


def itens_da_lista(html: str) -> list[tuple[str, str, str]]:
    """[(id_des, url_absoluta, titulo), ...], na ordem em que aparecem."""
    achados = []
    for m in re.finditer(r'<a[^>]+href="(/editais/(\d+)[^"]*)"[^>]*>(.*?)</a>', html, re.S):
        caminho, id_des, titulo = m.group(1), m.group(2), texto_limpo(m.group(3))
        if titulo:
            achados.append((id_des, "https://des.ufla.br" + caminho, titulo))
    return achados


# ---------------------------------------------------------------- edital
def data_publicacao(html: str) -> date | None:
    m = re.search(r'documentPublished">\s*Publicado:\s*\w+,\s*(\d{1,2})\s+(\w+)\s+(\d{4})', html)
    if not m:
        return None
    dia, mes_nome, ano = m.group(1), sem_acento(m.group(2)).lower(), m.group(3)
    mes = MESES.get(mes_nome[:3])
    if not mes:
        return None
    try:
        return date(int(ano), mes, int(dia))
    except ValueError:
        return None


def resumo_do_corpo(html: str) -> str:
    corpo = html.split("documentByLine", 1)[-1]
    m = re.search(r"<p>(.*?)</p>", corpo, re.S)
    if not m:
        return "Confira os detalhes completos no site do DES/UFLA."
    resumo = texto_limpo(m.group(1))
    return (resumo[:297] + "...") if len(resumo) > 300 else resumo


def areas_do_titulo(titulo: str) -> list[str]:
    alvo = sem_acento(titulo).lower()
    return [area for area, palavras in AREA_PALAVRAS.items()
            if any(p in alvo for p in palavras)]


# ---------------------------------------------------------------- escrita
def ja_importado(id_des: str) -> bool:
    marca = f"fonte: des-editais-{id_des} "
    for post in DESTINO.glob("*/index.qmd"):
        if marca in post.read_text(encoding="utf-8"):
            return True
    return False


def preenche(modelo: str, valores: dict[str, str]) -> str:
    def bloco(m):
        return m.group(2) if valores.get(m.group(1), "").strip() else ""
    texto = re.sub(r"<!--se:(\w+)-->(.*?)<!--/se-->", bloco, modelo, flags=re.S)
    for chave, valor in valores.items():
        texto = texto.replace("{{" + chave + "}}", valor)
    return re.sub(r"\n{3,}", "\n\n", texto).strip() + "\n"


def importa_um(id_des: str, url: str, titulo: str, dry_run: bool) -> str | None:
    try:
        pagina = baixa(url)
    except Exception as e:
        print(f"[!!] não abri {url}: {e}")
        return None

    publicado = data_publicacao(pagina)
    if not publicado:
        print(f"[!!] sem data de publicação reconhecível: {url}")
        return None
    if publicado < date.today() - timedelta(days=JANELA_DIAS):
        return "velho"

    cats = ["Oportunidades", "Editais"] + areas_do_titulo(titulo)
    cats_fmt = ", ".join(cats)
    pasta = DESTINO / f"{publicado.isoformat()}-{slug(titulo)}"
    if pasta.exists():
        pasta = pasta.with_name(f"{pasta.name}-{id_des}")

    resumo = resumo_do_corpo(pagina).replace('"', "'")
    valores = {
        "titulo": titulo.replace('"', "'"),
        "resumo": resumo,
        "autor": "Departamento de Estatística da UFLA",
        "data": publicado.isoformat(),
        "texto": f"<!-- fonte: des-editais-{id_des} -->\n\n{resumo}",
        "categorias": cats_fmt,
        "link": url,
        "thumbnail": "", "relatorio": "", "relatorio_html": "",
        "relatorio_pdf": "", "apresentacao": "",
    }
    conteudo = preenche(MODELO.read_text(encoding="utf-8"), valores)

    rotulo = f"{pasta.relative_to(RAIZ).as_posix()} ({', '.join(cats[2:]) or 'sem área'})"
    if dry_run:
        print(f"[dry-run] importaria {rotulo}")
        return rotulo
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / "index.qmd").write_text(conteudo, encoding="utf-8", newline="\n")
    print(f"[ok] importado {rotulo}")
    return rotulo


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    importados: list[str] = []

    for indice in range(PAGINAS_NO_MAXIMO):
        try:
            html = baixa(pagina_da_lista(indice))
        except Exception as e:
            print(f"[!!] não abri a página {indice + 1} da listagem: {e}")
            break
        itens = itens_da_lista(html)
        if not itens:
            break

        parou = False
        for id_des, url, titulo in itens:
            if ja_importado(id_des):
                continue
            resultado = importa_um(id_des, url, titulo, dry_run)
            if resultado == "velho":
                parou = True
                break
            if resultado:
                importados.append(resultado)
            time.sleep(0.4)   # cortesia com o site do DES, não é nosso
        if parou:
            break

    print(f"\n{len(importados)} edital(is) {'a importar' if dry_run else 'importado(s)'}.")
    anota("importados", str(len(importados)))
    anota("lista", "; ".join(importados))
    return 0


if __name__ == "__main__":
    sys.exit(main())
