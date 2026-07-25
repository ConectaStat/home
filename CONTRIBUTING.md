# Como contribuir com o site

Site do **Conexão Estatística** (Departamento de Estatística da UFLA), feito
com [Quarto](https://quarto.org). Este documento reúne as convenções de
organização do repositório. Documentos `.md` como este não viram página do
site (o `_quarto.yml` só renderiza `.qmd`).

## As quatro regras

1. **Post novo** → uma pasta nova em `<seção>/posts/AAAA-MM-DD-slug/index.qmd`,
   com a capa e os anexos dentro dela. Comece copiando de `_templates/`.
2. **Página nova** (não é post) → um `.qmd` na raiz da seção, nunca dentro de
   `posts/`.
3. **Nunca commitar** `_site/`, `.DS_Store` ou arquivos do RStudio — o
   `.gitignore` já cuida disso. A pasta publicada é `docs/`, gerada pelo
   `quarto render`.
4. **Menu (`_quarto.yml`) só recebe páginas**, nunca posts: quem lista os
   posts são as listagens das páginas de seção.

## Página ou post?

A pasta `posts/` é a fronteira. Tudo que está **dentro** dela é post e entra
automaticamente na listagem da seção; tudo **fora** dela é página.

```
eventos/
├── _metadata.yml     # padrões da seção (layout, banner) - vale para tudo aqui
├── index.qmd         # a página de listagem
└── posts/
    ├── 2026-01-15-programa-de-verao-2026/
    │   ├── index.qmd
    │   └── thumbnail.png
    └── 2025-05-20-v-workshop-data-science/
        ├── index.qmd
        └── thumbnail.png
```

Por isso as listagens são simplesmente `contents: posts`, sem exclusões
frágeis do tipo `"!index.qmd"`.

## Publicando um post

1. Crie a pasta `<seção>/posts/AAAA-MM-DD-slug/` (a data é a de publicação e
   serve para ordenar os posts também no explorador de arquivos).
2. Escreva o `index.qmd` com, no mínimo: `title`, `description`, `author`,
   `date` e `categories`.
3. **Capa**: salve `thumbnail.png` (16:9) na mesma pasta e aponte
   `image: "thumbnail.png"` no front matter. Se você não tiver capa, apague a
   linha `image:` — o `scripts/gerar_thumbnails.py` gera uma sozinho no
   próximo `quarto render`.
4. Rode `quarto render` e confira a página antes de publicar.

### Projetos dos estudantes (Organização e Apresentação de Dados)

Copie `_templates/projeto-estudante.qmd` para
`projetos/ensino/organizacao-e-apresentacao-de-dados/posts/AAAA-MM-DD-slug/index.qmd`
e coloque o material recebido dentro da mesma pasta:

```
posts/2026-06-22-populacao-e-pib/
├── index.qmd
├── thumbnail.png
└── relatorios/
    ├── relatorio.html      # embutido na página pelo iframe
    └── apresentacao.html   # opcional (slides)
```

Os HTML de `relatorios/` são **conteúdo de terceiros já renderizado**: entram
no repositório como vieram e nenhum script os reescreve.

## Mudou o endereço de uma página?

Acrescente a URL antiga em `aliases:` no front matter — o Quarto gera um
redirecionamento e os links já compartilhados continuam funcionando:

```yaml
aliases:
  - /noticias/slug-antigo.html
```

## Onde fica cada coisa

| Pasta | O que é |
|---|---|
| `_assets/` | tema (`.scss`/`.css`) e o template de cards das listagens |
| `_includes/` | HTML injetado em todas as páginas (JS das listagens, transições) |
| `_templates/` | modelos para começar um post novo |
| `images/` | imagens da marca e do site; `images/topicos/` são as capas dos tópicos de Projetos |
| `scripts/` | automações do build (capas automáticas, ajuste de títulos) |
| `docs/` | **saída do build** — gerada pelo `quarto render`, não edite à mão |

O prefixo `_` marca infraestrutura: o Quarto ignora essas pastas ao procurar
páginas.

## Build e publicação

```bash
quarto render
```

O site sai direto em `docs/`, que é a pasta servida pelo GitHub Pages. A cada
push na `master`, o workflow `.github/workflows/publicar.yml` renderiza e
commita `docs/` automaticamente.

Para trabalhar com recarga automática:

```bash
quarto preview
```
