# Ciência| <br/> Estatística| <br/> &amp; Sociedade

Bem-vindo à casa do [ConectaStat](https://conectastat.github.io/), um projeto do [Departamento de Estatística da UFLA](https://des.ufla.br/). Este repositório contém todo o código-fonte e o conteúdo do site, uma plataforma que busca a popularização da estatística e da ciência de dados no sul de Minas.

O site é construído com [Quarto](https://quarto.org) e publicado pelo GitHub Pages. Qualquer pessoa da comunidade do DES pode publicar aqui: não é preciso saber programar, e todo o passo a passo está neste documento.

> Site de projeto vinculado ao Departamento de Estatística da UFLA. Este não é um site institucional da Universidade.

## Índice
1. [Coordenação](#coordenação)
2. [Contribuidores](#contribuidores)
3. [Seja um contribuidor](#seja-um-contribuidor)
4. [Estrutura do site e do repositório](#estrutura-do-site-e-do-repositório)
5. [A regra única para publicar](#a-regra-única-para-publicar)
6. [Publicar em cada área](#publicar-em-cada-área)
7. [Páginas que não são posts](#páginas-que-não-são-posts)
8. [Rodar e publicar o site](#rodar-e-publicar-o-site)
9. [Pendências](#pendências)

## Coordenação

O ConectaStat é conduzido no Departamento de Estatística da UFLA. A coordenação responde pelo rumo do projeto, pela orientação acadêmica e pela revisão do que é publicado.

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/USUARIO"><img src="https://github.com/USUARIO.png?size=100" width="100px;" alt="Nome do docente"/><br /><sub><b>Nome do docente</b></sub></a><br /><sub>Coordenação</sub></td>
    </tr>
  </tbody>
</table>

> Tabela a preencher: troque `USUARIO` pelo usuário do GitHub de cada docente e o nome exibido. Enquanto estiver assim, a foto aparece quebrada.

## Contribuidores

Aqui entra todo mundo que somou ao projeto, de qualquer forma: análises publicadas, código, ideias e correções. A lista não é fechada, e cresce a cada contribuição aceita. O significado de cada marca está em [como funciona o crédito](#como-funciona-o-crédito).

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/Leocarletto"><img src="https://avatars.githubusercontent.com/u/290053745?v=4?s=100" width="100px;" alt="Leonardo Carletto"/><br /><sub><b>Leonardo Carletto</b></sub></a><br /><a href="https://github.com/ConectaStat/conectastat.github.io/commits?author=Leocarletto" title="Código">💻</a> <a href="https://conectastat.github.io/" title="Conteúdo publicado no site">📈</a> <a href="https://github.com/Leocarletto" title="Coordenação do projeto">📊</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/uaipedro"><img src="https://avatars.githubusercontent.com/u/44395968?v=4?s=100" width="100px;" alt="Pedro Mambelli Fernandes"/><br /><sub><b>Pedro Mambelli Fernandes</b></sub></a><br /><a href="https://github.com/ConectaStat/conectastat.github.io/commits?author=uaipedro" title="Código">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/PedroEu781"><img src="https://avatars.githubusercontent.com/u/153462117?v=4?s=100" width="100px;" alt="Pedro"/><br /><sub><b>Pedro</b></sub></a><br /><a href="https://conectastat.github.io/" title="Conteúdo publicado no site">📈</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/Carolinabrito1304"><img src="https://avatars.githubusercontent.com/u/290053524?v=4?s=100" width="100px;" alt="Carolina Brito"/><br /><sub><b>Carolina Brito</b></sub></a><br /><a href="https://conectastat.github.io/" title="Conteúdo publicado no site">📈</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/amacielp73"><img src="https://avatars.githubusercontent.com/u/288349650?v=4?s=100" width="100px;" alt="André Maciel"/><br /><sub><b>André Maciel</b></sub></a><br /><a href="https://conectastat.github.io/" title="Conteúdo publicado no site">📈</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/carlossouza11052007-collab"><img src="https://avatars.githubusercontent.com/u/290053234?v=4?s=100" width="100px;" alt="Carlos Eduardo Silva Sousa"/><br /><sub><b>Carlos Eduardo Silva Sousa</b></sub></a><br /><a href="https://conectastat.github.io/" title="Conteúdo publicado no site">📈</a></td>
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

Troque `content` pelo tipo de contribuição: `coordenacao`, `code`, `bug`, `ideas`, `design` ou `translation`. O robô abre um pull request atualizando a tabela e o arquivo `.all-contributorsrc`.

## Seja um contribuidor

Quase toda seção do site aceita contribuição de fora, e nenhuma delas exige experiência com Git. O caminho é sempre o mesmo: preencher o [formulário de envio](https://conectastat.github.io/enviar.html) no próprio site.

Ao enviar, o GitHub abre com a submissão pronta. Assim que você confirma, o robô monta a página e abre um pedido de publicação para a equipe revisar. Você recebe a resposta na própria submissão.

| O que você tem | Vai parar em |
|---|---|
| Uma notícia ou aviso | [Notícias](https://conectastat.github.io/noticias/) |
| Um evento, curso ou palestra | [Eventos](https://conectastat.github.io/eventos/) |
| Um edital ou oportunidade | [Oportunidades](https://conectastat.github.io/oportunidades/) |
| Um texto de divulgação | [Artigos & Colunas](https://conectastat.github.io/artigos/) |
| Um programa, pacote ou aplicativo | [Softwares](https://conectastat.github.io/projetos/ensino/softwares/) |
| Uma apostila, tutorial ou slides | [Materiais](https://conectastat.github.io/projetos/ensino/materiais/) |
| Uma ação de extensão | [Ações de Extensão](https://conectastat.github.io/projetos/extensao/acoes/) |
| Uma análise feita na graduação | [Organização e Apresentação de Dados](https://conectastat.github.io/projetos/ensino/organizacao-e-apresentacao-de-dados/) |

Cada uma dessas páginas tem o próprio botão de envio, que abre o formulário com a seção já escolhida.

O formulário pergunta o seu **vínculo com o DES**, e é isso que define como você aparece na lista de contribuidores.

**Erro de digitação ou link quebrado?** [Abra uma issue](https://github.com/ConectaStat/conectastat.github.io/issues/new) dizendo em qual página está, ou edite o arquivo direto pelo GitHub e envie a sugestão. Se ela for aceita, você entra na lista automaticamente.

**Núcleos de pesquisa e páginas de texto** não passam pelo formulário, porque não são conteúdo datado. Abra uma issue descrevendo a proposta.

### Como funciona o crédito

Cada pessoa carrega uma ou mais marcas na lista, e elas se acumulam: ninguém perde uma marca antiga ao ganhar outra.

| | | |
|---|---|---|
| 📊 | `coordenacao` | Coordenação do projeto |
| 📈 | `content` | Conteúdo publicado no site |
| 💻 | `code` | Código |
| 🐛 | `bug` | Correção de erro |
| 💡 | `ideas` | Ideias e sugestões |
| 🎨 | `design` | Design |
| 🌍 | `translation` | Tradução |

A marca 📊 é atribuída a quem se identifica como **docente** ao enviar uma contribuição, e é ela que ordena a lista: quem coordena aparece no topo. Um docente que publica um material fica com 📊 📈; um estudante que publica uma análise fica com 📈.

## Estrutura do site e do repositório

### Visão geral

```
conectastat.github.io/
├── _quarto.yml                 configuração do site e menu
├── index.qmd                   página inicial
├── enviar.qmd                  formulário de envio de conteúdo
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
| `images/capa-padrao.svg` e `.png` | capa dos posts sem imagem própria, fundo branco |
| `images/capa-padrao-azul.svg` e `.png` | a mesma em fundo azul, para Notícias, Oportunidades e Eventos |
| `images/capa-social.svg` e `.png` | prévia dos links compartilhados em redes e mensageiros |
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

Se não houver capa, apague a linha `image:`: o site usa a capa padrão da seção. Evite arquivos grandes: acima de 500 KB, reduza antes de subir.

São duas capas padrão, as duas com o mesmo desenho (histograma com a curva normal ajustada, na linguagem dos gráficos que aparecem ao fundo dos banners de seção):

| Capa | Onde vale |
|---|---|
| `images/capa-padrao-azul.png` | Notícias, Oportunidades e Eventos |
| `images/capa-padrao.png` | Artigos, Projetos e todo o resto |

Cada uma está declarada em um `posts/_metadata.yml`, que o Quarto aplica a todos os posts da pasta. A capa passa a pertencer ao post, e não à página: por isso um mesmo edital aparece com a capa azul tanto em Oportunidades quanto nas três páginas de Editais dentro de Projetos, que listam os mesmos arquivos.

Para trocar o desenho de uma seção inteira, edite o `image:` do `_metadata.yml` dela. Para trocar em todas, refaça o PNG.

Não use `image-placeholder:` nas listagens: o Quarto só o aplica nos templates nativos de grade, e as listagens de manchete deste site usam o `_assets/cards.ejs`, que não recebe as opções da listagem.

Uma exceção: em Organização e Apresentação de Dados, um post sem `image:` ganha capa automática no próximo render completo, recortada de um gráfico do próprio relatório. Ali o desenho de verdade vale mais que a capa genérica. As demais seções não têm geração automática.

De cada capa existem duas versões: o `.svg`, que é o desenho editável, e o `.png` gerado a partir dele, que é o publicado. O PNG é obrigatório porque a mesma imagem serve de prévia quando alguém cola o link do post no WhatsApp, no LinkedIn ou no Telegram, e essas redes não leem SVG.

Depois de editar um SVG, refaça o PNG correspondente:

```
chrome --headless --screenshot=images/capa-padrao.png --window-size=1200,675 images/capa-padrao.svg
```

As duas capas de post são 1200 por 675, a mesma proporção dos cards. O `images/capa-social.svg`, que é a prévia dos endereços do site em si e não de um post, é 1200 por 630: essa é a proporção que as redes esperam, e fora dela a imagem aparece cortada.

### Documento embutido na página

Qualquer área aceita um documento: relatório, apostila, slides, tutorial. Quando a submissão traz um, a página **exibe o arquivo inteiro**, em vez de mostrar um botão que leva o leitor para fora do site. É o campo "Documento para exibir na página" do formulário, e ele aceita tanto um link de arquivo no GitHub quanto o arquivo arrastado direto na issue.

O robô baixa o arquivo para `relatorios/` dentro da pasta do post. HTML precisa vir compactado em `.zip`; PDF pode vir direto. Em Organização e Apresentação de Dados o documento é obrigatório: sem relatório não há projeto. Nas demais áreas é opcional, e sem ele a página fica só com o texto e os links.

**HTML e PDF são exibidos de formas diferentes**, e o modelo escolhe sozinho pela extensão do arquivo.

O HTML entra num `<iframe>`. A página esconde o título e o índice internos do documento, que ela já mostra por conta própria, mede a altura real do conteúdo e deixa o documento rolar junto com o resto da página, sem barra de rolagem interna. As seções dele viram o índice "Nesta página" na margem direita. Esse índice depende de duas linhas no `posts/_metadata.yml` da seção, `toc: true` e `margin-width: 250px`: sem elas o Quarto não cria a margem e o índice não aparece.

O PDF entra num `<object>` de altura fixa, porque quem o desenha é o visualizador do próprio navegador. Não há conteúdo para medir nem seções para indexar, e o documento rola por dentro da moldura. Boa parte dos navegadores de celular não exibe PDF embutido: nesses casos aparece, no lugar da moldura, um parágrafo com o link para abrir o arquivo em outra aba. Por isso, **quando houver escolha, prefira HTML**: só ele se integra à página de verdade.

Se um dia o PDF voltar a aparecer espremido numa faixa de uns 450 px, é porque alguém tirou o `:not(.report-pdf)` do seletor em `_includes/listing-cards.html`. Aquele ajuste automático de altura serve só ao HTML; aplicado a PDF, ele lê um valor sem sentido do visualizador e encolhe a moldura.

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

É por aqui que chega a maior parte das contribuições de fora, e o caminho tem duas pontas: o estudante envia pelo formulário do site, e alguém da equipe publica.

#### O que o estudante faz

Preenche o [formulário de envio](https://conectastat.github.io/enviar.html?area=projeto), escolhendo a seção "Projeto de estudante". Ao enviar, o GitHub abre com a issue pronta: ele revisa, anexa o relatório e confirma. Só precisa estar logado no GitHub, e a conta é gratuita.

#### O que a equipe faz

Nada até o pull request aparecer. O robô monta tudo sozinho assim que a submissão chega:

```
pessoa preenche o formulário no site
        ↓
issue criada, com todos os campos
        ↓
o robô monta a página, baixa o relatório e credita quem enviou
        ↓
abre um pull request e avisa na issue
        ↓
VOCÊ decide na aba Pull requests
   Merge = publica     Close = recusa
```

A sua decisão é um clique. Ao mesclar, o site republica sozinho e o crédito entra junto.

#### Como fica a pasta

Esta é a única área com anexos pesados. A pasta fica assim:

```
projetos/ensino/organizacao-e-apresentacao-de-dados/posts/2026-08-12-nome-do-projeto/
├── index.qmd
├── thumbnail.png
└── relatorios/
    ├── relatorio.html       aparece embutido na página
    └── apresentacao.html    opcional (slides)
```

O robô monta o cabeçalho a partir do modelo `_templates/areas/projeto-estudante.qmd`. Publicando à mão, o essencial é:

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

**Páginas de texto.** Estatística, Assessoria e Consultoria, Revista Científica, Graduação, Pós-Graduação e Painel dos Egressos: abra o `index.qmd` da pasta correspondente e edite o texto.

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
| antes | `scripts/gerar_thumbnails.py` | recorta a capa de um gráfico do relatório, só em Organização e Apresentação de Dados |
| depois | `scripts/ajustar_titulos.py` | ajusta o separador dos títulos e normaliza os redirecionamentos |
| depois | `scripts/gerar_textos.py` | refaz o `TEXTOS.md`, o mapa de textos usado na revisão editorial |

Só o primeiro tem requisitos extras (Chrome e as bibliotecas Python). Os outros dois usam apenas a biblioteca padrão.

Além desses, três workflows cuidam do repositório sozinhos:

| Arquivo | Quando roda | O que faz |
|---|---|---|
| `.github/workflows/publicar.yml` | a cada envio para a `master` | renderiza o site e atualiza a pasta publicada |
| `.github/workflows/receber-submissao.yml` | quando chega uma submissão | monta a página na seção escolhida, credita quem enviou e abre o pull request |
| `.github/workflows/contribuidores.yml` | ao mesclar um pull request | credita quem teve a contribuição aceita |

Quatro scripts dão apoio a esses workflows:

| Script | O que faz |
|---|---|
| `scripts/publicar_submissao.py` | lê a submissão, escolhe o modelo da área e monta a pasta do post |
| `scripts/creditar_submissao.py` | deduz os tipos de contribuição a partir do vínculo declarado |
| `scripts/creditar_contribuidor.py` | soma o novo tipo aos que a pessoa já tinha, em vez de substituir |
| `scripts/ordenar_contribuidores.py` | coloca a coordenação no topo da lista antes de regenerar a tabela |

Os modelos de página de cada área ficam em `_templates/areas/`, um `.qmd` por seção. Neles, `{{campo}}` é substituído pelo dado do formulário e os trechos entre `<!--se:campo-->` e `<!--/se-->` somem quando o campo vem vazio. Para mudar como uma seção é publicada, basta editar o modelo dela.

Para tudo isso funcionar, o repositório precisa, em **Settings › Actions › General**, da opção *Allow GitHub Actions to create and approve pull requests* marcada. Sem ela o robô monta a página mas não consegue abrir o pedido de publicação.

O workflow reconhece uma submissão pelo corpo da issue, e não por etiqueta: ele procura a pergunta "Onde isso deve ser publicado" ou um título começando com `[Envio]`. Foi feito assim porque o GitHub descarta em silêncio uma etiqueta declarada no formulário que não exista no repositório, e a submissão passava batida.

### Serviços externos

O site é estático, mas as páginas carregam alguns recursos de terceiros no navegador de quem visita. Se houver política de domínios na rede institucional, estes são os endereços usados:

| Domínio | Para quê |
|---|---|
| `fonts.googleapis.com`, `fonts.gstatic.com` | fontes Inter (texto e slogan) e JetBrains Mono (blocos de código) |
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

**Nome do projeto.** O endereço público e o nome do repositório ainda trazem a marca antiga. Se a organização for renomeada no GitHub, atualizar `site-url` e `repo-url` no `_quarto.yml` e o link do GitHub no rodapé, que hoje apontam para `conectastat.github.io`.

**Coordenação.** A tabela da seção Coordenação está com `USUARIO` e "Nome do docente" no lugar dos dados reais, e enquanto estiver assim a foto aparece quebrada. É a única tabela do documento mantida à mão: a de contribuidores se atualiza sozinha.

**Arquivos grandes.** Os relatórios enviados são versionados junto com o site, e alguns passam de 10 MB. Funciona, mas engorda o histórico do git para sempre e torna impraticável revisar o conteúdo num pull request. Se o volume crescer, avaliar outro destino para esses arquivos.
