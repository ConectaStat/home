# Roadmap / Tarefas do projeto

Pendências e decisões em aberto do Conexão Estatística. Ao concluir um item,
remova-o daqui (o histórico fica no git). As convenções já adotadas estão em
[CONTRIBUTING.md](CONTRIBUTING.md).

## Renomear o repositório e o endereço do site (fora do código)

Os fontes já não falam mais em "ConectaStat", mas o endereço público
(`conectastat.github.io/home`) e o nome do repositório (`ConectaStat/home`)
seguem com a marca antiga — isso só muda no próprio GitHub (configurações da
organização/repositório). Ao renomear, atualizar `site-url` e `repo-url` no
`_quarto.yml` e o link em `contato.qmd`.

## App "Probabilidade na prática" (oculto, uso futuro)

O laboratório interativo de probabilidade que ficava na página **Estatística**
foi ocultado do site, mas o código está preservado em
[`estatistica/_probabilidade-na-pratica.qmd`](estatistica/_probabilidade-na-pratica.qmd)
(arquivos com prefixo `_` não são renderizados pelo Quarto).

Para reativar, basta adicionar em `estatistica/index.qmd`, no ponto desejado:

```
{{{< include _probabilidade-na-pratica.qmd >}}}
```

Obs.: ao reativar, reavaliar os textos vizinhos da página (a introdução que
apresentava o app e a menção ao exemplo do ENEM foram adaptadas quando ele
foi ocultado).

## Editais: imagem para "aberto" e "fechado"

Nas páginas de editais (`projetos/ensino/editais/`, `projetos/extensao/editais/`
e `projetos/pesquisa/editais/`), adicionar um esquema visual com **uma imagem
positiva para editais abertos e outra para editais encerrados** — por exemplo,
duas thumbnails padrão (ou um selo/badge sobre o card) trocadas conforme o
status do edital no frontmatter de cada post em `oportunidades/`.

## Editais por tipo de projeto

Hoje as três páginas de editais (ensino, extensão e pesquisa) listam **todos**
os posts de `oportunidades/`. Quando houver volume, marcar cada edital com uma
categoria (`ensino`, `extensao`, `pesquisa`) no frontmatter e filtrar a listagem
de cada página pelo tipo correspondente.

## Tópicos "Softwares" e "Materiais" (Projetos de Ensino)

As páginas `projetos/ensino/softwares/` e `projetos/ensino/materiais/` foram
criadas com a estrutura de listagem pronta, mas ainda sem conteúdo (por isso
o `quarto render` avisa que a listagem está vazia — o aviso some com o
primeiro item publicado). Para publicar, crie a pasta `posts/` dentro delas e
o primeiro post, conforme o [CONTRIBUTING.md](CONTRIBUTING.md).

## Assinatura própria do DES no rodapé

O rodapé segue com o bloco de texto "DES / Departamento de Estatística" ao
lado da marca da UFLA. A assinatura própria (oficial) do DES ainda será
definida/fornecida para substituir esse bloco.

## Hero em largura total

A hero image deverá ocupar todo o espaço da seção, com o
"Ciência/ Estatística/ Conexão" sobreposto à imagem (hoje ficam lado a lado).

## Imagens dos cards de tópicos (área de Projetos)

Os cards de tópicos e de núcleos usam miniaturas temáticas em SVG
(`images/topicos/*.svg`, geradas a partir dos gráficos da identidade visual
do site). Se quiser usar fotos/manchetes próprias em algum tópico, basta
trocar o campo `image:` do item na listagem de `projetos/*/index.qmd`
(ou o `image:` do frontmatter, no caso dos núcleos).

## Disclaimer abaixo da hero image

O texto provisório abaixo da hero na home ("Site de projeto vinculado ao
Departamento de Estatística da UFLA. Este não é um site institucional da
Universidade.") será substituído por um texto definitivo.
