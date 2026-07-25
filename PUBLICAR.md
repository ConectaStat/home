# Como publicar em cada área do site

Guia prático para quem alimenta o **Conexão Estatística** no dia a dia. Não é
preciso saber programar: publicar é copiar uma pasta modelo, trocar o texto e
salvar.

As convenções por trás das regras estão em [CONTRIBUTING.md](CONTRIBUTING.md);
aqui só o passo a passo.

---

## A regra única

Vale para **todas** as áreas de conteúdo do site:

> Crie a pasta `<área>/posts/AAAA-MM-DD-assunto/`, coloque dentro dela um
> arquivo `index.qmd` e todos os anexos (capa, relatórios, imagens).

A data é a de publicação e serve para ordenar. O "assunto" é um apelido curto,
tudo minúsculo, sem acento e com hífen no lugar do espaço.

```
2026-08-12-edital-monitoria-2027/
├── index.qmd          ← o texto
└── thumbnail.png      ← a capa (opcional)
```

Nada além disso: você **nunca** precisa editar o menu nem cadastrar o conteúdo
em lista nenhuma. As páginas encontram o post sozinhas.

## Onde publicar o quê

| Quero publicar… | Vai em |
|---|---|
| Manchete, aviso, novidade do departamento | `noticias/posts/` |
| Edital, chamada, vaga de monitoria | `oportunidades/posts/` |
| Evento, curso, workshop, palestra futura | `eventos/posts/` |
| Texto de divulgação científica, coluna | `artigos/posts/` |
| Projeto de análise feito por estudante | `projetos/ensino/organizacao-e-apresentacao-de-dados/posts/` |
| Programa, pacote ou app do departamento | `projetos/ensino/softwares/posts/` |
| Apostila, tutorial, material didático | `projetos/ensino/materiais/posts/` |

Cada uma dessas áreas é detalhada abaixo.

---

## 1. Notícias

**Onde:** `noticias/posts/AAAA-MM-DD-assunto/index.qmd`
**Aparece em:** página inicial e na página Notícias.

```yaml
---
title: "Título da notícia"
description: "Uma ou duas frases que resumem — é o que aparece no card."
author: "Departamento de Estatística da UFLA"
date: "2026-08-12"
image: "thumbnail.png"
categories: [Notícias]
---

Escreva aqui o texto da notícia, em parágrafos normais.

[Leia a matéria completa no site do DES/UFLA »](https://des.ufla.br/)
```

## 2. Oportunidades (editais)

**Onde:** `oportunidades/posts/AAAA-MM-DD-assunto/index.qmd`
**Aparece em:** página inicial, página Oportunidades **e** nas três páginas de
editais dentro de Projetos (Ensino, Pesquisa e Extensão).

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

O costume aqui é **não** copiar o edital inteiro: um resumo curto e o link para
o documento oficial no site do DES.

## 3. Eventos

**Onde:** `eventos/posts/AAAA-MM-DD-assunto/index.qmd`
**Aparece em:** página inicial e na página Eventos.
**Data:** use a data **do evento**, não a do dia em que você está escrevendo.

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

## 4. Artigos & Colunas

**Onde:** `artigos/posts/AAAA-MM-DD-assunto/index.qmd`
**Aparece em:** página Artigos & Colunas.

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

Os artigos publicados até aqui não têm capa própria — sem a linha `image:`,
o site usa a capa padrão. Para divulgação de palestras, use
`categories: [Artigos, Palestras]`.

## 5. Organização e Apresentação de Dados (projetos dos estudantes)

**Onde:** `projetos/ensino/organizacao-e-apresentacao-de-dados/posts/AAAA-MM-DD-assunto/`
**Aparece em:** página do tópico, dentro de Projetos → Ensino.

Esta é a única área com anexos pesados. A pasta fica assim:

```
2026-08-12-nome-do-projeto/
├── index.qmd
├── thumbnail.png
└── relatorios/
    ├── relatorio.html       ← aparece embutido na página
    └── apresentacao.html    ← opcional (slides)
```

Comece copiando [`_templates/projeto-estudante.qmd`](_templates/projeto-estudante.qmd),
que já vem com tudo explicado. O essencial:

```yaml
---
title: "Título do projeto"
description: "2 a 4 frases enviadas pelo estudante; vira a descrição do card."
author: "usuario-do-estudante"
date: "2026-08-12"
image: "thumbnail.png"
categories: [Análise de dados, R, "FONTE DOS DADOS"]
---
```

Três cuidados próprios desta área:

1. **Renomeie os arquivos recebidos** para `relatorio.html` e
   `apresentacao.html`. O nome importa: é o que a página procura.
2. **Não edite o conteúdo dos relatórios.** São trabalho de terceiros e entram
   como vieram.
3. **Categorias**: sempre a linguagem (`R`, `Python`), o tema
   (`Saúde`, `Economia`, `Meio ambiente`…) e a fonte dos dados entre aspas
   (`"Vigitel (Ministério da Saúde)"`, `"PBEV (INMETRO)"`).

Os estudantes enviam os trabalhos pelo formulário da página "Envie seu
projeto". *(Atenção: hoje esse formulário abre uma issue no repositório antigo
do projeto — precisa ser corrigido antes de divulgar o site.)*

## 6. Softwares e 7. Materiais (Projetos de Ensino)

**Onde:** `projetos/ensino/softwares/posts/…` e `projetos/ensino/materiais/posts/…`

Estas duas áreas ainda não têm nenhum conteúdo, então a pasta `posts/` **ainda
não existe** — no primeiro item, crie-a junto:

```
projetos/ensino/softwares/
├── index.qmd
└── posts/                          ← criar
    └── 2026-08-12-pacote-x/        ← criar
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

Enquanto estiverem vazias, o `quarto render` avisa que a listagem não encontrou
nada. É esperado, e some com o primeiro item publicado.

---

## Capas (thumbnail)

- **Tem imagem?** Salve como `thumbnail.png` dentro da pasta do post, no
  formato paisagem 16:9 (ex.: 1200×675), e mantenha a linha
  `image: "thumbnail.png"`.
- **Não tem?** Apague a linha `image:`. O site usa a capa padrão e, no próximo
  render completo, o gerador automático tenta criar uma a partir da própria
  página ou do relatório.
- Evite arquivos gigantes: acima de 500 KB, reduza antes de subir.

## Conferindo antes de publicar

Quem tem o Quarto instalado:

```bash
quarto preview
```

O site abre no navegador e recarrega sozinho a cada arquivo salvo.

Quem não tem: publique mesmo assim. A cada envio para o repositório, o robô do
GitHub renderiza e atualiza o site automaticamente — depois é só conferir a
página no ar.

---

## Áreas que não são "posts"

Estas mudam com pouca frequência e são editadas direto no arquivo, sem criar
pasta nova.

**Páginas de texto** — Estatística, Assessoria e Consultoria, Revista
Científica, Contato, Graduação, Pós-Graduação, Painel dos Egressos: abra o
`index.qmd` da pasta correspondente e edite o texto.

**Núcleo de pesquisa novo** — crie
`projetos/pesquisa/nucleos/<sigla>/index.qmd` (copiando `nlin/`, `gps/` ou
`st/`) e acrescente uma linha na listagem de
`projetos/pesquisa/nucleos/index.qmd`:

```yaml
  contents:
    - "nlin/index.qmd"
    - "gps/index.qmd"
    - "st/index.qmd"
    - "nova-sigla/index.qmd"     ← acrescente aqui
```

**Tópico novo em Projetos** (Ensino, Pesquisa ou Extensão) — crie a pasta do
tópico com seu `index.qmd` e acrescente um item na lista do cabeçalho de
`projetos/<área>/index.qmd`, **sempre antes do item de Editais**, que fica por
último:

```yaml
    - title: "Nome do tópico"
      description: "Uma ou duas frases."
      path: nome-da-pasta/index.html
      image: ../../images/topicos/nome-da-capa.svg
```

**Seção nova no menu** — só nesse caso se mexe no `_quarto.yml`, na parte
`navbar`. É raro e vale chamar quem cuida do site.

---

## O que nunca fazer

- **Não edite nada dentro de `docs/`.** É a pasta gerada automaticamente; tudo
  o que for escrito ali é apagado no próximo render.
- **Não mexa em `_assets/`, `_includes/` e `scripts/`** sem saber o que está
  fazendo: são o tema e as automações do site.
- **Não apague a linha `date:`** de um post — sem ela ele não aparece nas
  listagens.
- **Não use acento, espaço ou letra maiúscula** em nome de pasta ou de arquivo.
