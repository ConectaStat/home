# Conexão Estatística

Site do **Departamento de Estatística da UFLA** — ciência, estatística e
conexão. Feito com [Quarto](https://quarto.org) e publicado no GitHub Pages:

**<https://conectastat.github.io/home/>**

> Site de projeto vinculado ao Departamento de Estatística da UFLA.
> Este não é um site institucional da Universidade.

## Rodando localmente

Requisitos: [Quarto](https://quarto.org/docs/get-started/) 1.4+. Para as capas
automáticas dos posts, também Python 3 com `selenium` e `pillow` e o Google
Chrome instalado (opcional — sem eles o site renderiza normalmente).

```bash
quarto preview
```

Para gerar a versão publicável (sai em `docs/`):

```bash
quarto render
```

## Organização

```
├── _quarto.yml                 # configuração do site e menu
├── index.qmd                   # página inicial
├── _assets/ _includes/ _templates/   # tema, scripts de página e modelos
├── images/  scripts/           # imagens da marca e automações do build
├── estatistica/ assessoria/ contato.qmd
├── artigos/ eventos/ noticias/ oportunidades/   # seções com posts/
├── cursos/                     # graduação e pós-graduação
├── projetos/                   # ensino, pesquisa e extensão
├── acoes/                      # revista científica
└── docs/                       # saída do build (publicada)
```

Cada seção com conteúdo datado guarda os posts em `posts/AAAA-MM-DD-slug/`,
com a capa e os anexos na mesma pasta.

## Contribuindo

As convenções do repositório (como criar um post, onde fica cada coisa, o que
nunca commitar) estão em [CONTRIBUTING.md](CONTRIBUTING.md). As pendências e
decisões em aberto estão em [ROADMAP.md](ROADMAP.md), e o guia de implantação
em servidor próprio em [DEPLOY.md](DEPLOY.md).
