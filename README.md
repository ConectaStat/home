# Ciência/ <br/> Estatística/ <br/> Conexão

Bem-vindo à casa do [Conexão Estatística](https://conectastat.github.io/), um projeto do [Departamento de Estatística da UFLA](https://des.ufla.br/). Este repositório contém todo o código-fonte e o conteúdo do site, uma plataforma que busca a popularização da estatística e da ciência de dados no sul de Minas.

O site é construído com [Quarto](https://quarto.org) e publicado pelo GitHub Pages. Qualquer pessoa da comunidade do DES pode publicar aqui: não é preciso saber programar, e todo o passo a passo está neste documento.

> Site de projeto vinculado ao Departamento de Estatística da UFLA. Este não é um site institucional da Universidade.

## Índice
1. [Contribuidores](#contribuidores-)
2. [Seja um contribuidor](#seja-um-contribuidor)
3. [Estrutura do site e do repositório](#estrutura-do-site-e-do-repositório)
4. [A regra única para publicar](#a-regra-única-para-publicar)
5. [Publicar em cada área](#publicar-em-cada-área)
6. [Páginas que não são posts](#páginas-que-não-são-posts)
7. [Rodar e publicar o site](#rodar-e-publicar-o-site)
8. [Pendências](#pendências)

## Contribuidores ✨
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg)](#contribuidores-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Nosso agradecimento a estas pessoas por tudo que trouxeram ao Conexão Estatística: análises publicadas, código, documentação, ideias e correções ([legenda dos emojis](https://allcontributors.org/docs/en/emoji-key)).

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/Leocarletto"><img src="https://avatars.githubusercontent.com/u/290053745?v=4?s=100" width="100px;" alt="Leonardo Carletto"/><br /><sub><b>Leonardo Carletto</b></sub></a><br /><a href="https://github.com/ConectaStat/conectastat.github.io/commits?author=Leocarletto" title="Code">💻</a> <a href="#content-Leocarletto" title="Content">🖋</a> <a href="https://github.com/ConectaStat/conectastat.github.io/commits?author=Leocarletto" title="Documentation">📖</a> <a href="#maintenance-Leocarletto" title="Maintenance">🚧</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/uaipedro"><img src="https://avatars.githubusercontent.com/u/44395968?v=4?s=100" width="100px;" alt="Pedro Mambelli Fernandes"/><br /><sub><b>Pedro Mambelli Fernandes</b></sub></a><br /><a href="https://github.com/ConectaStat/conectastat.github.io/commits?author=uaipedro" title="Code">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/PedroEu781"><img src="https://avatars.githubusercontent.com/u/153462117?v=4?s=100" width="100px;" alt="Pedro"/><br /><sub><b>Pedro</b></sub></a><br /><a href="#content-PedroEu781" title="Content">🖋</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/Carolinabrito1304"><img src="https://avatars.githubusercontent.com/u/290053524?v=4?s=100" width="100px;" alt="Carolina Brito"/><br /><sub><b>Carolina Brito</b></sub></a><br /><a href="#content-Carolinabrito1304" title="Content">🖋</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/amacielp73"><img src="https://avatars.githubusercontent.com/u/288349650?v=4?s=100" width="100px;" alt="André Maciel"/><br /><sub><b>André Maciel</b></sub></a><br /><a href="#content-amacielp73" title="Content">🖋</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/carlossouza11052007-collab"><img src="https://avatars.githubusercontent.com/u/290053234?v=4?s=100" width="100px;" alt="Carlos Eduardo Silva Sousa"/><br /><sub><b>Carlos Eduardo Silva Sousa</b></sub></a><br /><a href="#content-carlossouza11052007-collab" title="Content">🖋</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

Este projeto segue a especificação [all-contributors](https://github.com/all-contributors/all-contributors). Toda forma de contribuição é bem-vinda, não só código.

A lista acima se mantém sozinha. Para incluir alguém, basta comentar em qualquer issue ou pull request do repositório:

```
@all-contributors please add @usuario for content
```

Troque `content` pelo tipo de contribuição (`code`, `doc`, `ideas`, `bug`, `design`, `review`). O robô abre um pull request atualizando a tabela e o arquivo `.all-contributorsrc`.

## Seja um contribuidor

Há várias formas de participar, e nenhuma delas exige experiência com Git.

**Publicou uma análise na disciplina?** Os projetos de Organização e Apresentação de Dados são publicados no site com crédito ao autor e link para o seu repositório. Use o formulário em [Envie seu projeto](https://conectastat.github.io/projetos/ensino/organizacao-e-apresentacao-de-dados/enviar.html).

**Tem uma pauta, notícia ou evento?** [Abra uma issue](https://github.com/ConectaStat/conectastat.github.io/issues/new) contando o que é. Alguém da equipe ajuda a publicar.

**Achou um erro no site?** Erro de digitação, link quebrado, informação desatualizada: abra uma issue descrevendo onde está.

**Quer escrever direto no repositório?** Siga o passo a passo das seções seguintes. Toda publicação é um arquivo de texto em uma pasta nova.

## Estrutura do site e do repositório

### Visão geral

```
conectastat.github.io/
├── _quarto.yml                 configuração do site e menu
├── index.qmd                   página inicial
├── contato.qmd
├── _assets/                    tema (.scss e .css) e template de cards
├── _includes/                  HTML injetado em todas as páginas
├── _templates/                 modelos para começar um post
├── images/                     imagens da marca e capas dos tópicos
├── scripts/                    automações do build
│
├── estatistica/index.qmd
├── assessoria/index.qmd
├── acoes/revista-cientifica/index.qmd
│
├── artigos/          ┐
├── eventos/          │  cada uma com index.qmd (página de arquivo)
├── noticias/         │  e posts/ (o conteúdo datado)
├── oportunidades/    ┘
│
├── cursos/
│   ├── graduacao/index.qmd
│   └── pos-graduacao/
│       ├── index.qmd
│       └── egressos/index.qmd
│
├── projetos/
│   ├── ensino/
│   │   ├── index.qmd
│   │   ├── organizacao-e-apresentacao-de-dados/
│   │   ├── softwares/  materiais/  editais/
│   │   ├── pesquisa/   (nucleos/ com nlin, gps, st, e editais/)
│   │   └── extensao/   (editais/)
│
└── docs/                       saída do build, publicada pelo GitHub Pages
```

O prefixo `_` marca infraestrutura: o Quarto ignora essas pastas ao procurar páginas. Por isso `_assets`, `_includes`, `_templates` e qualquer arquivo começando com `_` nunca viram página do site.

### Página ou post

A pasta `posts/` é a fronteira. Tudo que está **dentro** dela é post e entra automaticamente na listagem da seção. Tudo **fora** dela é página.

```
eventos/
├── _metadata.yml     padrões da seção (layout e banner), valem para tudo aqui
├── index.qmd         a página de listagem
└── posts/
    ├── 2026-01-15-programa-de-verao-2026/
    │   ├── index.qmd
    │   └── thumbnail.png
    └── 2025-05-20-v-workshop-data-science/
        ├── index.qmd
        └── thumbnail.png
```

Por isso as listagens são simplesmente `contents: posts`, sem exclusões frágeis do tipo `"!index.qmd"`.

As seções com conteúdo datado (Notícias, Oportunidades, Eventos e Artigos) têm cada uma a sua página de arquivo, além de aparecerem na home. As três primeiras usam o mesmo template de cards dos Projetos, para o mesmo conteúdo ter a mesma aparência em qualquer lugar do site.

### Outros arquivos e pastas

| Caminho | O que é |
|---|---|
| `_quarto.yml` | configuração do site: menu, rodapé, tema e automações |
| `_assets/conexao-estatistica.scss` | tema visual (cores, tipografia, componentes) |
| `_assets/cards.ejs` | template dos cards de manchete usados nas listagens |
| `_includes/` | JavaScript das listagens e transições entre páginas |
| `_templates/` | modelos para começar um post novo |
| `images/topicos/` | capas dos cards de tópico da área de Projetos |
| `scripts/` | automações do build, descritas mais abaixo |
| `TEXTOS.md` | mapa de todos os textos do site, para revisão editorial |
| `docs/` | saída do build, gerada automaticamente e nunca editada à mão |

## A regra única para publicar

Vale para todas as áreas de conteúdo:

> Crie a pasta `<área>/posts/AAAA-MM-DD-assunto/`, coloque dentro dela um arquivo `index.qmd` e todos os anexos (capa, relatórios, imagens).

A data é a de publicação e serve para ordenar. O assunto é um apelido curto, tudo minúsculo, sem acento e com hífen no lugar do espaço.

```
2026-08-12-edital-monitoria-2027/
├── index.qmd          o texto
└── thumbnail.png      a capa (opcional)
```

Nada além disso. Você nunca precisa editar o menu nem cadastrar o conteúdo em lista alguma: as páginas encontram o post sozinhas.

### Onde publicar o quê

| Quero publicar | Vai em |
|---|---|
| Manchete, aviso, novidade do departamento | `noticias/posts/` |
| Edital, chamada, vaga de monitoria | `oportunidades/posts/` |
| Evento, curso, workshop, palestra futura | `eventos/posts/` |
| Texto de divulgação científica, coluna | `artigos/posts/` |
| Projeto de análise feito por estudante | `projetos/ensino/organizacao-e-apresentacao-de-dados/posts/` |
| Programa, pacote ou app do departamento | `projetos/ensino/softwares/posts/` |
| Apostila, tutorial, material didático | `projetos/ensino/materiais/posts/` |

### Capas

Salve como `thumbnail.png` dentro da pasta do post, em formato paisagem 16:9 (por exemplo 1200 por 675), e mantenha a linha `image: "thumbnail.png"` no cabeçalho.

Se não houver capa, apague a linha `image:`. O site usa a capa padrão e, no próximo render completo, o gerador automático tenta criar uma a partir da própria página ou do relatório. Evite arquivos grandes: acima de 500 KB, reduza antes de subir.

### Conferindo antes de publicar

Quem tem o Quarto instalado:

```bash
quarto preview
```

O site abre no navegador e recarrega sozinho a cada arquivo salvo.

Quem não tem: publique mesmo assim. A cada envio para o repositório, o robô do GitHub renderiza e atualiza o site automaticamente, e depois é só conferir a página no ar.

## Publicar em cada área

### Notícias

Arquivo em `noticias/posts/AAAA-MM-DD-assunto/index.qmd`. Aparece na página inicial e na página Notícias.

```yaml
---
title: "Título da notícia"
description: "Uma ou duas frases que resumem, é o que aparece no card."
author: "Departamento de Estatística da UFLA"
date: "2026-08-12"
image: "thumbnail.png"
categories: [Notícias]
---

Escreva aqui o texto da notícia, em parágrafos normais.

[Leia a matéria completa no site do DES/UFLA »](https://des.ufla.br/)
```

### Oportunidades (editais)

Arquivo em `oportunidades/posts/AAAA-MM-DD-assunto/index.qmd`. Aparece na página inicial, na página Oportunidades e nas três páginas de editais dentro de Projetos (Ensino, Pesquisa e Extensão).

```yaml
---
title: "Edital Nº 004/2026: Seleção de monitores voluntários"
description: "Processo seletivo para monitores voluntários das disciplinas do DES em 2027."
author: "Departamento de Estatística da UFLA"
date: "2026-08-12"
image: "thumbnail.png"
categories: [Oportunidades, Editais]
---

Um parágrafo curto explicando do que se trata.

[Ler edital no site do DES/UFLA »](https://des.ufla.br/editais)
```

O costume aqui é não copiar o edital inteiro: um resumo curto e o link para o documento oficial no site do DES.

### Eventos

Arquivo em `eventos/posts/AAAA-MM-DD-assunto/index.qmd`. Use a data **do evento**, não a do dia em que você está escrevendo.

```yaml
---
title: "VI Workshop em Data Science"
description: "Workshop com palestras e atividades sobre métodos estatísticos e aplicações."
author: "Departamento de Estatística da UFLA"
date: "2026-09-15"
image: "thumbnail.png"
categories: [Eventos]
---

Descrição do evento: público, formato, inscrições.

[Saiba mais »](https://des.ufla.br/eventos)
```

Para minicursos e capacitações, use `categories: [Cursos]`.

### Artigos e Colunas

Arquivo em `artigos/posts/AAAA-MM-DD-assunto/index.qmd`.

```yaml
---
title: "Título do texto"
description: "Resumo em uma ou duas frases."
author: "Nome de quem escreveu"
date: "2026-08-12"
categories: [Artigos]
---

O texto em si, em parágrafos.
```

Os artigos publicados até aqui não têm capa própria: sem a linha `image:`, o site usa a capa padrão. Para divulgação de palestras, use `categories: [Artigos, Palestras]`.

### Organização e Apresentação de Dados

Esta é a única área com anexos pesados. A pasta fica assim:

```
projetos/ensino/organizacao-e-apresentacao-de-dados/posts/2026-08-12-nome-do-projeto/
├── index.qmd
├── thumbnail.png
└── relatorios/
    ├── relatorio.html       aparece embutido na página
    └── apresentacao.html    opcional (slides)
```

Comece copiando `_templates/projeto-estudante.qmd`, que já vem com tudo explicado. O essencial do cabeçalho:

```yaml
---
title: "Título do projeto"
description: "2 a 4 frases enviadas pelo estudante, vira a descrição do card."
author: "usuario-do-estudante"
date: "2026-08-12"
image: "thumbnail.png"
categories: [Análise de dados, R, "FONTE DOS DADOS"]
---
```

Três cuidados próprios desta área:

1. **Renomeie os arquivos recebidos** para `relatorio.html` e `apresentacao.html`. O nome importa: é o que a página procura.
2. **Não edite o conteúdo dos relatórios.** São trabalho de terceiros e entram como vieram.
3. **Categorias**: sempre a linguagem (`R`, `Python`), o tema (`Saúde`, `Economia`, `Meio ambiente`) e a fonte dos dados entre aspas, como `"Vigitel (Ministério da Saúde)"` ou `"PBEV (INMETRO)"`.

### Softwares e Materiais

Estas duas áreas ainda não têm conteúdo, então a pasta `posts/` **ainda não existe**. No primeiro item, crie-a junto:

```
projetos/ensino/softwares/
├── index.qmd
└── posts/                          criar
    └── 2026-08-12-pacote-x/        criar
        ├── index.qmd
        └── thumbnail.png
```

```yaml
---
title: "Nome do software"
description: "O que ele faz, em uma ou duas frases."
author: "Quem desenvolveu"
date: "2026-08-12"
image: "thumbnail.png"
---

Para que serve, quem pode usar, como instalar.

[Código no GitHub »](https://github.com/)
```

Enquanto estiverem vazias, o `quarto render` avisa que a listagem não encontrou nada. É esperado, e some com o primeiro item publicado.

## Páginas que não são posts

Estas mudam com pouca frequência e são editadas direto no arquivo, sem criar pasta nova.

**Páginas de texto.** Estatística, Assessoria e Consultoria, Revista Científica, Contato, Graduação, Pós-Graduação e Painel dos Egressos: abra o `index.qmd` da pasta correspondente e edite o texto.

**Núcleo de pesquisa novo.** Crie `projetos/pesquisa/nucleos/<sigla>/index.qmd` copiando `nlin/`, `gps/` ou `st/`, e acrescente uma linha na listagem de `projetos/pesquisa/nucleos/index.qmd`:

```yaml
  contents:
    - "nlin/index.qmd"
    - "gps/index.qmd"
    - "st/index.qmd"
    - "nova-sigla/index.qmd"
```

**Tópico novo em Projetos** (Ensino, Pesquisa ou Extensão). Crie a pasta do tópico com seu `index.qmd` e acrescente um item na lista do cabeçalho de `projetos/<área>/index.qmd`, sempre antes do item de Editais, que fica por último:

```yaml
    - title: "Nome do tópico"
      description: "Uma ou duas frases."
      path: nome-da-pasta/index.html
      image: ../../images/topicos/nome-da-capa.svg
```

**Seção nova no menu.** Só nesse caso se mexe no `_quarto.yml`, na parte `navbar`. É raro e vale chamar quem cuida do site.

**Mudou o endereço de uma página?** Enquanto o site não estiver divulgado, mover ou renomear páginas é livre, porque não há links antigos circulando. Depois que ele estiver no ar, acrescente a URL antiga em `aliases:` no cabeçalho, e o Quarto gera um redirecionamento:

```yaml
aliases:
  - /noticias/slug-antigo.html
```

## Rodar e publicar o site

### Requisitos

Para editar textos, nada. Para renderizar na sua máquina, o [Quarto](https://quarto.org/docs/get-started/) 1.4 ou superior. Para as capas automáticas, também Python 3 com `selenium` e `pillow` e o Google Chrome instalado, tudo opcional: sem eles o site renderiza normalmente e o post fica com a capa padrão.

```bash
quarto preview     # trabalha com recarga automática
quarto render      # gera a versão publicável em docs/
```

### Publicação

O site sai direto em `docs/`, que é a pasta servida pelo GitHub Pages. A cada envio para a `master`, o workflow `.github/workflows/publicar.yml` renderiza e atualiza `docs/` automaticamente. Não é preciso rodar nada à mão para publicar.

### Automações do build

O `_quarto.yml` registra três scripts Python que rodam sozinhos a cada `quarto render`, todos à prova de falha: se algo der errado, o render segue e o site é publicado do mesmo jeito.

| Quando | Script | O que faz |
|---|---|---|
| antes | `scripts/gerar_thumbnails.py` | gera a capa dos posts que estão sem `image:` |
| depois | `scripts/ajustar_titulos.py` | ajusta o separador dos títulos e normaliza os redirecionamentos |
| depois | `scripts/gerar_textos.py` | refaz o `TEXTOS.md`, o mapa de textos usado na revisão editorial |

Só o primeiro tem requisitos extras (Chrome e as bibliotecas Python). Os outros dois usam apenas a biblioteca padrão.

Uso manual do gerador de capas, quando necessário:

```bash
python scripts/gerar_thumbnails.py            # gera capas de quem não tem
python scripts/gerar_thumbnails.py --force    # regenera todas
python scripts/gerar_thumbnails.py <slug>     # apenas posts específicos
```

### Serviços externos

O site é estático, mas as páginas carregam alguns recursos de terceiros no navegador de quem visita. Se houver política de domínios na rede institucional, estes são os endereços usados:

| Domínio | Para quê |
|---|---|
| `fonts.googleapis.com`, `fonts.gstatic.com` | fontes Inter (texto) e JetBrains Mono (slogan) |
| `unpkg.com`, `tile.openstreetmap.org` | biblioteca e imagens do mapa de rota da página inicial |
| `router.project-osrm.org`, `nominatim.openstreetmap.org` | cálculo de rota e busca de endereço |
| `www.google.com/maps` | mapa institucional embutido na página inicial |
| `www.youtube.com` | vídeo embutido na página Estatística |
| `github.com` | formulário Envie seu projeto e links de código |
| `des.ufla.br` | links institucionais |

### O que nunca fazer

- **Não edite nada dentro de `docs/`.** É a pasta gerada automaticamente, e tudo o que for escrito ali é apagado no próximo render.
- **Não mexa em `_assets/`, `_includes/` e `scripts/`** sem saber o que está fazendo: são o tema e as automações do site.
- **Não apague a linha `date:`** de um post, porque sem ela ele não aparece nas listagens.
- **Não use acento, espaço ou letra maiúscula** em nome de pasta ou de arquivo.
- **Não commite** `_site/`, `.DS_Store` ou arquivos do RStudio. O `.gitignore` já cuida disso.

## Pendências

Decisões em aberto e trabalhos que ainda serão feitos. Ao concluir um item, remova-o daqui, porque o histórico fica no git.

**Assinatura do DES no rodapé.** O rodapé usa hoje um bloco de texto montado à mão. O correto, pelo Manual de Identidade Visual da UFLA (§6.5 e §6.13), é o arquivo oficial da assinatura horizontal do departamento, na versão monocromática negativa, que precisa ser solicitado à DCOM.

**App "Probabilidade na prática".** O laboratório interativo que ficava na página Estatística foi ocultado, mas o código está preservado em `estatistica/_probabilidade-na-pratica.qmd`. Para reativar, inclua no `index.qmd` da seção:

```
{{{< include _probabilidade-na-pratica.qmd >}}}
```

**Editais abertos e encerrados.** Adicionar um esquema visual nas páginas de editais, com uma imagem para os que estão abertos e outra para os encerrados, conforme o status no cabeçalho de cada post.

**Editais por área.** Hoje as três páginas de editais listam todos os posts de `oportunidades/`. Quando houver volume, marcar cada edital com uma categoria e filtrar a listagem de cada página.

**Hero em largura total.** A imagem da página inicial deverá ocupar todo o espaço da seção, com o slogan sobreposto a ela, em vez de ficarem lado a lado.

**Disclaimer.** O texto provisório abaixo da hero será substituído pelo definitivo.

**Endereço e nome.** O endereço público e o nome do repositório ainda trazem a marca antiga do projeto. Ao renomear a organização no GitHub, atualizar `site-url` e `repo-url` no `_quarto.yml` e o link em `contato.qmd`.
