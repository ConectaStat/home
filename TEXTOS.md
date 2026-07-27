# Mapa de textos do site

Inventário de **todo o texto editável** do ConectaStat, na ordem em que
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
└── enviar.qmd ────────────────── Formulário de envio
```

---

## 1. Página inicial

```
index.qmd
├── hero .................. slogan + ilustração
├── disclaimer ............ abaixo da hero
├── o projeto ............. texto de apresentação
├── notícias .............. carrossel
├── oportunidades ......... carrossel
├── eventos ............... carrossel
└── onde estamos .......... mapa + endereço
```


### Hero (topo da home)

> Slogan sobre a ilustração:
>
>


### Disclaimer abaixo da hero

> Site de projeto vinculado ao Departamento de Estatística da UFLA. Este não é um site institucional da Universidade.


### Seção da home: Notícias

> Subtítulo: Manchetes e novidades do Departamento de Estatística


### Seção da home: Oportunidades

> Subtítulo: Editais internos e oportunidades de estudo


### Seção da home: Eventos

> Subtítulo: Cursos, workshops e encontros da comunidade


### Seção da home: Onde estamos

> Subtítulo: Visite o Departamento de Estatística no campus da UFLA


### Bloco do mapa (endereço)

> Departamento de Estatística da UFLA
> Trevo Rotatório Professor Edmir Sá Santos, s/n
> Campus Universitário, Lavras/MG
> CEP 37203-202 · Caixa Postal 3037


---

## 2. Rodapé (todas as páginas)

`_quarto.yml` › `website: page-footer`


**Disclaimer (canto esquerdo):**

> Site de projeto vinculado ao Departamento de Estatística da UFLA. Este não é um site institucional da Universidade.

**Assinatura institucional (canto direito):**

> DES
> Departamento de Estatística
>
> (ao lado da marca da UFLA)

**Ícones:** GitHub, Instagram e LinkedIn (os dois últimos ainda sem link).


---

## 3. Menu do topo

`_quarto.yml` › `website: navbar`


```
Ciência/ Estatística/ Conexão   ← slogan à esquerda (leva à home)

  Estatística
  Nossos Cursos
      └── Graduação
      └── Pós-Graduação
  Projetos
      └── Pesquisa
      └── Ensino
      └── Extensão
  Ações
      └── Revista Científica
      └── Assessoria e Consultoria Estatística
      └── Eventos
```


---

## 4. Páginas das seções


### Estatística
`estatistica/index.qmd`

**Título (aparece no banner):** Estatística

**Subtítulo:** A ciência de aprender com os dados. E uma das profissões mais promissoras da atualidade.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## O que é a Estatística?
>
> A Estatística é a ciência que desenvolve e aplica métodos para **coletar,
> organizar, analisar e interpretar dados**, transformando informação em
> conhecimento e apoiando decisões em condições de incerteza. Ela é a base
> fundamental da Ciência de Dados e está presente em praticamente todas as
> áreas do conhecimento: agricultura, saúde, indústria, finanças, esportes,
> políticas públicas e inteligência artificial.
>
> ## Onde atua o estatístico?
>
> O profissional de Estatística atua em um mercado amplo e em expansão:
>
> - **Ciência de Dados e Inteligência Artificial**: modelagem preditiva,
>   aprendizado de máquina e análise de grandes volumes de dados;
> - **Agronegócio e experimentação**: planejamento e análise de experimentos,
>   melhoramento genético e agricultura de precisão;
> - **Saúde e bioestatística**: ensaios clínicos, epidemiologia e vigilância
>   em saúde pública;
> - **Mercado financeiro e seguros**: análise de risco, precificação e
>   modelagem atuarial;
> - **Indústria e qualidade**: controle estatístico de processos e
>   confiabilidade;
> - **Pesquisa e academia**: desenvolvimento de novos métodos e formação de
>   pessoas.
>
> Pesquisas de mercado apontam a carreira de estatístico e de cientista de
> dados entre as **melhores e mais bem remuneradas profissões** da era digital,
> com demanda muito superior à oferta de profissionais qualificados.
>
> ## A Estatística em um vídeo
>
> Assista à apresentação do professor Júlio sobre a área e a atuação do
> estatístico:
>
> ## Estude Estatística na UFLA
>
> O Departamento de Estatística da UFLA oferece formação completa na área,
> da graduação à pós-graduação, além de
> [assessoria e consultoria estatística](../assessoria/index.qmd) para a
> comunidade acadêmica e a sociedade. São dois caminhos com focos
> complementares:
>
> ### Graduação: foco em Ciência de Dados
>
> Embora seja um **Bacharelado em Estatística**, o
> [curso de graduação](../cursos/graduacao/index.qmd) da UFLA tem forte **ênfase
> em Ciência de Dados**: além da base sólida em probabilidade e inferência, o
> estudante aprende programação, bancos de dados e aprendizado de máquina para
> extrair conhecimento de grandes volumes de dados. É o caminho de quem quer
> partir de dados reais, chegar a modelos preditivos e ir muito além.
>
> ### Pós-graduação: foco em Ciências Agrárias
>
> O [Programa de Pós-Graduação em Estatística e Experimentação Agropecuária
> (PPGEEA)](../cursos/pos-graduacao/index.qmd) oferece **mestrado** e
> **doutorado** com tradição na interface entre a Estatística e as **ciências
> agrárias**: planejamento e análise de experimentos, melhoramento genético e
> agricultura de precisão. É a formação de quem transforma dados de campo, como
> as safras de café da região de Lavras, em decisões com rigor científico.


### Nossos Cursos › Graduação
`cursos/graduacao/index.qmd`

**Título (aparece no banner):** Graduação

**Subtítulo:** Bacharelado em Estatística com ênfase em Ciência de Dados.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## Sobre o curso
>
> O curso de **Graduação em Estatística** da UFLA iniciou suas atividades no
> semestre 2024/1 e forma profissionais preparados para atuar com análise de
> dados, modelagem estatística e ciência de dados em empresas, instituições de
> pesquisa e órgãos públicos.
>
> Com uma ampla formação os alunos são expostos aos mais variados tipos de situações, alguns exemplos são os projetos de **Organização e Apresentação de Dados** em que cada aluno escolhe uma base de dados publica para desenvolver uma analise exploratória e desenvolver um relatório do assunto, isso tudo desde o primeiro período! Esses projetos podem ser visualizados
> [aqui](../../projetos/ensino/organizacao-e-apresentacao-de-dados/index.qmd).
>
> ## Matriz curricular
>
> A matriz curricular está organizada em núcleos de formação, cursados ao longo
> de 8 semestres:
>
> | Núcleo | Conteúdos principais |
> |---|---|
> | **Base matemática** | Cálculo, Álgebra Linear, Matemática Discreta |
> | **Probabilidade e Inferência** | Probabilidade, Inferência Estatística, Processos Estocásticos |
> | **Modelagem estatística** | Modelos de Regressão, Planejamento e Análise de Experimentos, Análise Multivariada, Séries Temporais |
> | **Computação e dados** | Programação, Estatística Computacional, Bancos de Dados, Aprendizado de Máquina |
> | **Formação complementar** | Amostragem, Controle de Qualidade, Estatística Espacial, disciplinas eletivas |
> | **Prática profissional** | Projetos orientados, Estágio Supervisionado, Trabalho de Conclusão de Curso |
>
> A matriz oficial completa, com ementas e pré-requisitos detalhados, está no
> [site do DES/UFLA](https://des.ufla.br/graduacao). Ou veja aqui, módulo a
> módulo:
>
> ### 1º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES110 | Matemática para Estatística I | 8 | - |
> | GES136 | Introdução aos Planos Experimentais | 4 | - |
> | GES139 | Organização e Apresentação de Dados | 8 | - |
> | GES140 | Vivência Profissional em Estatística | 2 | - |
>
> ### 2º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES113 | Probabilidade I | 8 | GES110 |
> | GES135 | Fundamentos de Programação | 4 | - |
> | GES137 | Matemática para Estatística II | 10 | GES110 |
>
> ### 3º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES116 | Matemática para Estatística III | 8 | GES137 |
> | GES117 | Probabilidade II | 6 | GES113 |
> | GES134 | Estrutura de Dados | 8 | GES135 |
> | GES141 | Consultoria em Estatística I | 2 | GES136 |
>
> ### 4º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES118 | Inferência Estatística I | 8 | GES113 |
> | GES119 | Modelos Lineares I | 8 | GES113 |
> | GES142 | Amostragem | 4 | GES113 |
>
> ### 5º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES122 | Modelos Lineares II | 8 | GES119 |
> | GES123 | Planejamento e Análise de Experimentos | 4 | GES136 |
> | GES124 | Inferência Estatística II | 8 | GES118 |
>
> ### 6º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES125 | Séries Temporais | 4 | GES124 |
> | GES126 | Estatística Computacional | 6 | GES135 |
> | GES127 | Consultoria em Estatística II | 4 | GES141 |
> | GES130 | Ciência de Dados e Big Data | 4 | GES134 |
> | GES138 | Técnicas Multivariadas | 4 | GES124 |
>
> ### 7º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES128 | Modelos Lineares Generalizados | 6 | GES119 |
> | GES129 | Inferência Bayesiana | 4 | GES118 |
> | GES131 | Mineração de Dados e Aprendizagem de Máquinas | 6 | GES134 |
>
> ### 8º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | EES5889 | Estágio Supervisionado | 0 | - |


### Nossos Cursos › Pós-Graduação
`cursos/pos-graduacao/index.qmd`

**Título (aparece no banner):** Pós-Graduação

**Subtítulo:** Programa de Pós-Graduação em Estatística e Experimentação Agropecuária: mestrado e doutorado.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> O Departamento de Estatística da UFLA abriga o **Programa de Pós-Graduação em
> Estatística e Experimentação Agropecuária (PPGEEA)**, com cursos de
> **mestrado** e **doutorado**, formando pesquisadores e docentes com sólida
> base teórica e forte vocação aplicada.
>
> O programa tem tradição na interface entre a Estatística e as ciências
> agrárias, e vem ampliando sua atuação para a ciência de dados, a modelagem
> computacional e as aplicações em saúde, indústria e meio ambiente.
>
> ## Áreas de concentração e linhas de pesquisa
>
> - **Métodos estatísticos**: inferência, modelos lineares e não lineares,
>   modelos mistos e estatística bayesiana;
> - **Experimentação agropecuária**: planejamento e análise de experimentos,
>   melhoramento genético e agricultura de precisão;
> - **Modelagem e computação**: estatística computacional, séries temporais,
>   estatística espacial e aprendizado de máquina.
>
> ## Disciplinas
>
> Entre as disciplinas oferecidas regularmente estão:
>
> | Disciplina | Tema |
> |---|---|
> | Inferência Estatística | Estimação, testes de hipóteses e teoria assintótica |
> | Modelos Lineares | Teoria e aplicação de modelos de regressão |
> | Planejamento de Experimentos | Delineamentos experimentais e análise |
> | Estatística Computacional | Simulação, métodos de Monte Carlo e otimização |
> | Modelos Mistos | Efeitos aleatórios e dados longitudinais |
> | Estatística Bayesiana | Inferência bayesiana e métodos MCMC |
> | Séries Temporais | Modelagem e previsão de dados temporais |
>
> A relação completa de disciplinas, docentes e projetos está no
> [site do DES/UFLA](https://des.ufla.br/).
>
> ## Painel dos Egressos
>
> A trajetória dos nossos egressos (setores de atuação, regiões e formação
> continuada) está reunida em um dashboard interativo: o
> [Painel dos Egressos](egressos/index.qmd).


### Nossos Cursos › Pós-Graduação › Painel dos Egressos
`cursos/pos-graduacao/egressos/index.qmd`

**Título (aparece no banner):** Painel dos Egressos

**Subtítulo:** Para onde foram os egressos da Estatística da UFLA: setores, regiões e formação continuada.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> O **Painel dos Egressos** reúne, em um dashboard interativo, a trajetória
> dos egressos da graduação e da pós-graduação em Estatística da UFLA:
> os setores em que atuam, as regiões do país e do exterior para onde foram
> e a formação continuada que seguiram após o curso.


### Projetos › Ensino
`projetos/ensino/index.qmd`

**Título (aparece no banner):** Projetos de Ensino

**Subtítulo:** Iniciativas que fortalecem a formação em Estatística dentro e fora da sala de aula.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## Ensino no DES/UFLA
>
> Além das disciplinas da graduação e da pós-graduação, o Departamento de
> Estatística desenvolve projetos de ensino que apoiam a aprendizagem e a
> permanência dos estudantes: monitorias, docência voluntária, cursos e
> oficinas, e produção de material didático aberto. Explore os tópicos abaixo:

**Cards de tópico desta página:**

> **Organização e Apresentação de Dados**  
> Projetos de análise de dados feitos pelos estudantes de primeiro período da graduação, do dado bruto ao relatório final.
>
> **Softwares**  
> Aplicativos, pacotes e ferramentas computacionais desenvolvidos como apoio ao ensino de Estatística.
>
> **Materiais**  
> Apostilas, tutoriais e recursos didáticos abertos produzidos pelo departamento.
>
> **Editais de Projetos de Ensino**  
> Vagas de monitoria, docência voluntária e demais chamadas dos projetos de ensino, da mais recente à mais antiga.
>


### Projetos › Ensino › Organização e Apresentação de Dados
`projetos/ensino/organizacao-e-apresentacao-de-dados/index.qmd`

**Título (aparece no banner):** Organização e Apresentação de Dados

**Subtítulo:** Análises e projetos desenvolvidos pelos estudantes de Estatística da UFLA desde o primeiro período.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Cada card abaixo é um projeto publicado: análises de dados reais feitas
> pelos nossos estudantes, do dado bruto ao relatório final. Explore os
> trabalhos e, quando estiver pronto, envie o seu.


### Projetos › Ensino › Softwares
`projetos/ensino/softwares/index.qmd`

**Título (aparece no banner):** Softwares

**Subtítulo:** Aplicativos, pacotes e ferramentas computacionais de apoio ao ensino de Estatística.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Ferramentas computacionais desenvolvidas nos projetos de ensino do
> departamento. Os primeiros itens serão publicados em breve.


### Projetos › Ensino › Materiais
`projetos/ensino/materiais/index.qmd`

**Título (aparece no banner):** Materiais

**Subtítulo:** Apostilas, tutoriais e recursos didáticos abertos de apoio às disciplinas.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Materiais didáticos produzidos nos projetos de ensino do departamento.
> Os primeiros itens serão publicados em breve.


### Projetos › Ensino › Editais
`projetos/ensino/editais/index.qmd`

**Título (aparece no banner):** Editais de Projetos de Ensino

**Subtítulo:** Monitorias, docência voluntária e demais chamadas dos projetos de ensino.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Editais e chamadas ligados aos projetos de ensino, do mais recente ao mais
> antigo.


### Projetos › Pesquisa
`projetos/pesquisa/index.qmd`

**Título (aparece no banner):** Projetos de Pesquisa

**Subtítulo:** A investigação científica desenvolvida no Departamento de Estatística da UFLA.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## Pesquisa no DES/UFLA
>
> Os docentes e estudantes do Departamento de Estatística desenvolvem projetos
> de pesquisa em métodos estatísticos e em aplicações, com destaque para:
>
> - **Modelos de regressão não lineares** aplicados ao crescimento de seres
>   vivos e a fenômenos agronômicos;
> - **Modelos mistos e experimentação agropecuária**;
> - **Estatística bayesiana e métodos computacionais**;
> - **Séries temporais** e modelos para dados de contagem;
> - **Estatística espacial e geoestatística**;
> - **Aprendizado de máquina e ciência de dados**.
>
> Os resultados são publicados em periódicos nacionais e internacionais e
> apresentados em eventos científicos, muitos deles divulgados aqui no
> ConectaStat, na seção de [artigos](../../artigos/index.qmd).
> Explore os tópicos abaixo:

**Cards de tópico desta página:**

> **Núcleos de Pesquisa**  
> NLIN, GPS e ST: os núcleos que reúnem docentes, pós-graduandos e graduandos em torno de temas da Estatística.
>
> **Editais de Projetos de Pesquisa**  
> Iniciação científica e demais chamadas ligadas à pesquisa, da mais recente à mais antiga.
>


### Projetos › Pesquisa › Núcleos de Pesquisa
`projetos/pesquisa/nucleos/index.qmd`

**Título (aparece no banner):** Núcleos de Pesquisa

**Subtítulo:** NLIN, GPS e ST: grupos que reúnem estudantes e docentes em torno de temas da Estatística.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Os núcleos de pesquisa do Departamento de Estatística da UFLA reúnem
> graduandos, pós-graduandos e docentes em encontros periódicos de estudo,
> pesquisa e divulgação científica. Escolha um núcleo para conhecer:


### Projetos › Pesquisa › Núcleos › NLIN
`projetos/pesquisa/nucleos/nlin/index.qmd`

**Título (aparece no banner):** NLIN

**Subtítulo:** Núcleo de Estudos em Regressão Não Linear Aplicada.  
*(hoje oculto no site; fica só no código)*

**Descrição (para buscadores/compartilhamento):** Núcleo de Estudos em Regressão Não Linear Aplicada: modelos de crescimento e aplicações em agronomia e biologia.

**Texto da página:**

> O **NLIN** reúne estudantes e docentes interessados em **modelos de
> regressão não lineares** e suas aplicações, do crescimento de seres vivos
> à agronomia, passando por curvas de produção e fenômenos biológicos.
>
> ## O que fazemos
>
> - Encontros periódicos de estudo e discussão de artigos;
> - Desenvolvimento de projetos de pesquisa e iniciação científica;
> - Oficinas de ajuste de modelos não lineares no software R.
>
> ## Como participar
>
> O núcleo é aberto a estudantes de todos os cursos da UFLA. Acompanhe as
> chamadas na seção de [oportunidades](../../../../index.qmd#oportunidades) ou
> procure a coordenação pelo [site do DES](https://des.ufla.br/).


### Projetos › Pesquisa › Núcleos › GPS
`projetos/pesquisa/nucleos/gps/index.qmd`

**Título (aparece no banner):** GPS

**Subtítulo:** Núcleo de Estudos em Geoestatística e Processos Espaciais.  
*(hoje oculto no site; fica só no código)*

**Descrição (para buscadores/compartilhamento):** Núcleo de Estudos em Geoestatística e Processos Espaciais: estatística espacial aplicada à agricultura, ao ambiente e à saúde.

**Texto da página:**

> O **GPS** dedica-se à **estatística espacial**: geoestatística, processos
> pontuais e dados de área, com aplicações em agricultura de precisão, meio
> ambiente, epidemiologia e planejamento urbano.
>
> ## O que fazemos
>
> - Encontros de estudo sobre métodos de estatística espacial;
> - Análises aplicadas com dados georreferenciados;
> - Colaborações com grupos de pesquisa em agricultura de precisão.
>
> ## Como participar
>
> O núcleo é aberto a estudantes de todos os cursos da UFLA. Acompanhe as
> chamadas na seção de [oportunidades](../../../../index.qmd#oportunidades) ou
> procure a coordenação pelo [site do DES](https://des.ufla.br/).


### Projetos › Pesquisa › Núcleos › ST
`projetos/pesquisa/nucleos/st/index.qmd`

**Título (aparece no banner):** ST

**Subtítulo:** Núcleo de Estudos em Séries Temporais.  
*(hoje oculto no site; fica só no código)*

**Descrição (para buscadores/compartilhamento):** Núcleo de Estudos em Séries Temporais: modelagem e previsão de dados ao longo do tempo.

**Texto da página:**

> O **ST** estuda a **modelagem e a previsão de dados ao longo do tempo**:
> modelos ARIMA e GARCH, modelos para dados de contagem (como os GLARMA),
> séries ambientais, econômicas e epidemiológicas.
>
> ## O que fazemos
>
> - Encontros de estudo e discussão de artigos sobre séries temporais;
> - Projetos aplicados de previsão e monitoramento;
> - Oficinas de análise de séries temporais no software R.
>
> ## Como participar
>
> O núcleo é aberto a estudantes de todos os cursos da UFLA. Acompanhe as
> chamadas na seção de [oportunidades](../../../../index.qmd#oportunidades) ou
> procure a coordenação pelo [site do DES](https://des.ufla.br/).


### Projetos › Pesquisa › Editais
`projetos/pesquisa/editais/index.qmd`

**Título (aparece no banner):** Editais de Projetos de Pesquisa

**Subtítulo:** Iniciação científica e demais chamadas ligadas à pesquisa.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Editais e chamadas ligados aos projetos de pesquisa, do mais recente ao mais
> antigo.


### Projetos › Extensão
`projetos/extensao/index.qmd`

**Título (aparece no banner):** Projetos de Extensão

**Subtítulo:** A Estatística a serviço da comunidade: popularização da ciência e letramento estatístico.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## Extensão no DES/UFLA
>
> Os projetos de extensão levam a Estatística para além dos muros da
> universidade, promovendo o letramento estatístico e o pensamento crítico na
> sociedade:
>
> - **ConectaStat**: esta plataforma de popularização da ciência, com
>   notícias, artigos e eventos abertos à comunidade;
> - **Assessoria e consultoria estatística**: apoio a pesquisadores,
>   produtores, empresas e órgãos públicos
>   ([saiba mais](../../assessoria/index.qmd));
> - **Palestras e eventos abertos**: divulgação científica em escolas e
>   eventos regionais ([agenda de eventos](../../eventos/index.qmd));
> - **Cursos para a comunidade**: capacitações em análise de dados e
>   software estatístico.
>
> Explore os tópicos abaixo:

**Cards de tópico desta página:**

> **Ações de Extensão**  
> Cursos abertos, palestras, parcerias e atividades de divulgação científica levadas à comunidade.
>
> **Editais de Projetos de Extensão**  
> Chamadas e editais ligados aos projetos de extensão, da mais recente à mais antiga.
>


### Projetos › Extensão › Ações de Extensão
`projetos/extensao/acoes/index.qmd`

**Título (aparece no banner):** Ações de Extensão

**Subtítulo:** Cursos, palestras, parcerias e atividades levadas à comunidade.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Atividades de extensão do Departamento de Estatística: cursos abertos,
> palestras em escolas, parcerias com instituições e ações de divulgação
> científica. As primeiras serão publicadas em breve.


### Projetos › Extensão › Editais
`projetos/extensao/editais/index.qmd`

**Título (aparece no banner):** Editais de Projetos de Extensão

**Subtítulo:** Chamadas e editais ligados aos projetos de extensão.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Editais e chamadas ligados aos projetos de extensão, do mais recente ao mais
> antigo.


### Ações › Revista Científica
`acoes/revista-cientifica/index.qmd`

**Título (aparece no banner):** Revista Científica

**Subtítulo:** Brazilian Journal of Biometrics, periódico científico ligado ao Departamento de Estatística da UFLA.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## Brazilian Journal of Biometrics
>
> O **Brazilian Journal of Biometrics (BJB)** é um periódico científico de
> acesso aberto que publica artigos originais sobre métodos estatísticos e
> suas aplicações em biometria, agricultura, biologia, saúde e áreas afins.
>
> - **Acesso aberto**: todos os artigos disponíveis gratuitamente;
> - **Revisão por pares**: avaliação criteriosa por especialistas;
> - **Escopo**: estatística aplicada, experimentação, modelagem e métodos
>   quantitativos nas ciências da vida.
>
> [Conhecer a revista](https://www.biometria.ufla.br/index.php/BBJ){target="_blank"}
>
> ## Como submeter
>
> Autores interessados encontram as normas de submissão e o sistema de envio
> no [site oficial do periódico](https://www.biometria.ufla.br/index.php/BBJ){target="_blank"}.


### Ações › Assessoria e Consultoria Estatística
`assessoria/index.qmd`

**Título (aparece no banner):** Assessoria e Consultoria Estatística

**Texto da página:**

> *(sem texto próprio — a página só exibe a listagem)*


### Ações › Eventos (arquivo)
`eventos/index.qmd`

**Título (aparece no banner):** Eventos

**Subtítulo:** Seminários, palestras, minicursos e defesas.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> *(sem texto próprio — a página só exibe a listagem)*


### Notícias (arquivo)
`noticias/index.qmd`

**Título (aparece no banner):** Notícias

**Subtítulo:** Manchetes e novidades do Departamento de Estatística.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> *(sem texto próprio — a página só exibe a listagem)*


### Oportunidades (arquivo)
`oportunidades/index.qmd`

**Título (aparece no banner):** Oportunidades

**Subtítulo:** Editais internos e oportunidades de estudo.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> *(sem texto próprio — a página só exibe a listagem)*


### Artigos & Colunas (arquivo)
`artigos/index.qmd`

**Título (aparece no banner):** Artigos & Colunas

**Subtítulo:** Textos de divulgação que aproximam a Estatística do público.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> *(sem texto próprio — a página só exibe a listagem)*


### Enviar conteúdo (formulário do site)
`enviar.qmd`

**Título (aparece no banner):** Enviar conteúdo

**Subtítulo:** Publique no ConectaStat: notícia, evento, edital, artigo, software, material, ação de extensão ou projeto de estudante.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## Como funciona
>
> Preencha o formulário abaixo **sem sair do site**. Ao enviar, o GitHub abre em
> outra aba com a submissão **já preenchida**: é só revisar, anexar os arquivos
> e confirmar. Basta estar logado no GitHub (a conta é gratuita).
>
> A partir daí o robô monta a página sozinho e a equipe do departamento revisa
> antes de publicar. Você recebe a resposta na própria submissão.
>
> Os **arquivos** são anexados na tela do GitHub que abre: a imagem de capa e o
> documento, em `.html` (compactado em `.zip`) ou `.pdf`. Basta arrastar cada um
> para o campo correspondente antes de clicar em *Create*. Qualquer seção aceita
> um documento, e quando ele vem a página o exibe inteiro, em vez de mostrar só
> um link. Havendo escolha, prefira `.html`: ele se integra à página, com índice
> na lateral, enquanto o `.pdf` fica dentro de uma moldura e não abre embutido em
> boa parte dos celulares.


---

## 5. Conteúdo datado (posts já publicados)


### Notícias — posts publicados (1)


#### ConectaStat entra no ar com novo visual
`noticias/posts/2026-07-06-conexao-estatistica-no-ar/index.qmd`

**Resumo (aparece no card):** A plataforma de popularização da ciência do Departamento de Estatística da UFLA ganha novo formato: Ciência, Estatística e Sociedade.

> O **ConectaStat** está no ar com novo visual e nova organização: seções
> dedicadas à área de Estatística, aos nossos cursos de graduação e
> pós-graduação, à assessoria e consultoria estatística e aos projetos e
> ações do departamento.
>
> Na página inicial você encontra as últimas notícias, oportunidades (editais
> internos e de estudo), eventos e a localização do prédio da Estatística no
> campus da UFLA, com rota direto para o seu GPS.


### Oportunidades — posts publicados (4)


#### Edital: Eleições para Chefe e Subchefe do DES (2026-2030)
`oportunidades/posts/2026-04-01-edital-eleicoes-des/index.qmd`

**Resumo (aparece no card):** Convocação do processo eleitoral para os cargos de Chefe e Subchefe do Departamento de Estatística do ICET/UFLA.

> A Chefia do Departamento de Estatística (DES) do Instituto de Ciências Exatas
> e Tecnológicas (ICET) da UFLA convoca a comunidade para o processo de eleição
> de Chefe e Subchefe do departamento, referente ao período 2026-2030.
>
> Consulte o edital completo, prazos e procedimentos na página oficial do DES:
>
> [Ler edital no site do DES/UFLA »](https://des.ufla.br/editais/138-edital-eleicoes-chefe-e-subchefe-do-des)

#### Edital Nº 003/2026: Seleção de monitores voluntários
`oportunidades/posts/2026-02-20-edital-003-monitores-voluntarios/index.qmd`

**Resumo (aparece no card):** Processo seletivo para monitores voluntários das disciplinas do Departamento de Estatística em 2026.

> O Departamento de Estatística da UFLA abre processo seletivo para monitores
> voluntários, conforme o Edital Nº 003/2026.
>
> [Ler edital no site do DES/UFLA »](https://des.ufla.br/editais/137-edital-n-003-2026-selecao-de-monitores-voluntarios-para-2026)

#### Edital Nº 002/2026: Seleção de monitores voluntários
`oportunidades/posts/2026-02-15-edital-002-monitores-voluntarios/index.qmd`

**Resumo (aparece no card):** Processo seletivo para monitores voluntários das disciplinas do Departamento de Estatística em 2026.

> O Departamento de Estatística da UFLA abre processo seletivo para monitores
> voluntários, conforme o Edital Nº 002/2026.
>
> [Ler edital no site do DES/UFLA »](https://des.ufla.br/editais/136-edital-n-002-2026-selecao-de-monitores-voluntarios-para-2026)

#### Edital Nº 001/2026: Docência Voluntária (DES, 1º sem/2026)
`oportunidades/posts/2026-02-01-edital-001-docencia-voluntaria/index.qmd`

**Resumo (aparece no card):** Seleção para atuação em regime de docência voluntária no Departamento de Estatística no 1º semestre de 2026.

> O Departamento de Estatística da UFLA divulga o Edital Nº 001/2026 para
> seleção de docência voluntária no 1º semestre de 2026.
>
> [Ler edital no site do DES/UFLA »](https://des.ufla.br/editais/134-edital-n-001-2026-docencia-voluntaria-des-1-sem-2026)


### Eventos — posts publicados (4)


#### XVII Programa de Verão DES-ICET/UFLA 2026
`eventos/posts/2026-01-15-programa-de-verao-2026/index.qmd`

**Resumo (aparece no card):** Edição 2026 do tradicional Programa de Verão do Departamento de Estatística, com disciplinas e atividades de formação.

> O Programa de Verão do DES-ICET/UFLA chega à sua XVII edição, oferecendo
> disciplinas e atividades de aperfeiçoamento em Estatística durante o período
> de verão.
>
> [Saiba mais no site do DES/UFLA »](https://des.ufla.br/eventos/135-xvii-programa-de-verao-des-icet-ufla-2026)

#### XVII Encontro Mineiro de Estatística (MGEST) 2025
`eventos/posts/2025-11-05-xvii-encontro-mineiro-estatistica/index.qmd`

**Resumo (aparece no card):** Evento bienal que, desde 1999, reúne profissionais, docentes e estudantes da área de Estatística de Minas Gerais e do Brasil.

> O Encontro Mineiro de Estatística (MGEST) é um evento bienal que, desde 1999,
> reúne profissionais, docentes e estudantes para a troca de conhecimento e a
> divulgação de pesquisas na área de Estatística.
>
> [Saiba mais no site do DES/UFLA »](https://des.ufla.br/eventos/xvii-mgest-2025)

#### V Workshop em Data Science
`eventos/posts/2025-05-20-v-workshop-data-science/index.qmd`

**Resumo (aparece no card):** Workshop voltado à Ciência de Dados, com palestras e atividades sobre métodos estatísticos e aplicações.

> O Workshop em Data Science promove discussões sobre métodos estatísticos,
> aprendizado de máquina e aplicações de Ciência de Dados.
>
> [Saiba mais no site do DES/UFLA »](https://des.ufla.br/eventos/v-workshop-em-data-science)

#### Curso de Extensão: Introdução ao Software R
`eventos/posts/2024-09-01-curso-introducao-software-r/index.qmd`

**Resumo (aparece no card):** Curso de extensão de introdução ao R, ambiente livre para análise estatística e visualização de dados.

> Curso de extensão de introdução ao **R**, ambiente livre e gratuito amplamente
> utilizado para análise estatística, modelagem e visualização de dados.
>
> [Saiba mais no site do DES/UFLA »](https://des.ufla.br/cursos-e-palestras/125-curso-de-extensao-introducao-ao-software-r)


### Artigos & Colunas — posts publicados (3)


#### Introdução ao crescimento de seres vivos: indivíduo ou população?
`artigos/posts/2021-09-03-palestra-crescimento-seres-vivos/index.qmd`

**Resumo (aparece no card):** Palestra do ciclo do DES/UFLA sobre modelagem do crescimento de seres vivos, no nível do indivíduo e da população.

> Palestra do ciclo de seminários do Departamento de Estatística da UFLA sobre
> a modelagem do crescimento de seres vivos, abordando as perspectivas do
> indivíduo e da população.
>
> [Ver no site do DES/UFLA »](https://des.ufla.br/cursos-e-palestras/90-palestra-03-09-2021-introducao-ao-crescimento-de-seres-vivos-individuo-ou-populacao)

#### Modelos da classe GLARMA(p,q): séries temporais de contagem
`artigos/posts/2020-11-16-palestra-modelos-glarma/index.qmd`

**Resumo (aparece no card):** Palestra sobre os modelos GLARMA(p,q) como alternativa para a análise de séries temporais de contagem.

> Palestra do Departamento de Estatística da UFLA sobre os modelos da classe
> **GLARMA(p,q)**, uma alternativa para a modelagem de séries temporais de
> contagem.
>
> [Ver no site do DES/UFLA »](https://des.ufla.br/cursos-e-palestras/81-palestra-16-11-2020-modelos-da-classe-glarma-p-q-uma-alternativa-para-series-temporais-de-contagem)

#### Polinômios de Hermite: definições, propriedades e aplicações
`artigos/posts/2019-12-05-palestra-polinomios-hermite/index.qmd`

**Resumo (aparece no card):** Palestra sobre os polinômios de Hermite, suas propriedades e aplicações na Estatística.

> Palestra do Departamento de Estatística da UFLA sobre os **polinômios de
> Hermite**, suas definições, propriedades e aplicações na Estatística.
>
> [Ver no site do DES/UFLA »](https://des.ufla.br/cursos-e-palestras/72-palestra-05-12-2019-polinomios-de-hermite-definicoes-propriedades-e-aplicacoes-na-estatistica)


### Organização e Apresentação de Dados — posts publicados (5)


#### Etanol × combustíveis fósseis: emissões veiculares no PBEV 2026 (INMETRO)
`projetos/ensino/organizacao-e-apresentacao-de-dados/posts/2026-06-30-inmetro-pbev-2026/index.qmd`

**Resumo (aparece no card):** EDA sobre as consequências ambientais das emissões de automóveis a combustão no Brasil, comparando a eficiência e o impacto do etanol frente aos combustíveis fósseis.

> Análise Exploratória de Dados com base no **Programa Brasileiro de Etiquetagem
> Veicular (PBEV 2026)**, mantido pelo INMETRO. O projeto investiga o impacto
> ambiental dos veículos a etanol frente às alternativas a gasolina e diesel:
> emissões de CO₂ (g/km), eficiência de consumo (km/l) e a quantidade de CO₂
> potencialmente evitada por ano em cada categoria de veículo, evidenciando a
> vantagem ecológica do ciclo fechado de carbono do etanol.

#### Crescimento populacional e PIB pelo mundo (2010-2025)
`projetos/ensino/organizacao-e-apresentacao-de-dados/posts/2026-06-22-populacao-e-pib/index.qmd`

**Resumo (aparece no card):** EDA em R sobre o crescimento da população e o PIB de diversos países em intervalos de 5 anos, com relatório e apresentação em Quarto.

> Análise exploratória do **crescimento populacional e do PIB** de vários países
> em intervalos de cinco anos, de 2010 a 2025. Desenvolvido em **R**, o projeto
> serve como introdução à linguagem e como modelo para análises futuras, com
> relatório detalhado e apresentação em HTML gerados a partir de arquivos Quarto.

#### Vigilância de fatores de risco: microdados do Vigitel (2019 × 2023)
`projetos/ensino/organizacao-e-apresentacao-de-dados/posts/2026-06-15-vigitel-2019-2023/index.qmd`

**Resumo (aparece no card):** Análise exploratória dos microdados do Vigitel (Ministério da Saúde), comparando os anos de 2019 e 2023.

> Projeto da disciplina **Organização e Apresentação de Dados** com microdados do
> **Vigitel** (Vigilância de Fatores de Risco e Proteção para Doenças Crônicas
> por Inquérito Telefônico), do Ministério da Saúde. A análise exploratória
> compara os anos de **2019 e 2023**, com documentos de análise em R/Quarto e
> relatório final em HTML.

#### World Economic Outlook: panorama econômico mundial
`projetos/ensino/organizacao-e-apresentacao-de-dados/posts/2026-05-20-world-economic-outlook/index.qmd`

**Resumo (aparece no card):** EDA com dados do World Economic Outlook (FMI), com apresentação e relatório final em HTML.

> Análise exploratória construída sobre dados do **World Economic Outlook**,
> com apresentação e relatório final publicados em HTML.

#### Portal da Transparência da AGU: gastos do Ministério da Educação
`projetos/ensino/organizacao-e-apresentacao-de-dados/posts/2026-04-14-transparencia-agu/index.qmd`

**Resumo (aparece no card):** EDA com dados do Portal da Transparência da Advocacia-Geral da União, em um recorte de 681 observações do Ministério da Educação.

> Análise exploratória de dados extraídos do **Portal da Transparência da
> Advocacia-Geral da União (AGU)**. Do conjunto original com 65.535 observações
> e 12 variáveis, o recorte analisado reúne **681 observações do Ministério da
> Educação**, com relatório publicado em HTML.



### Materiais — posts publicados (1)


#### eda teste
`projetos/ensino/materiais/posts/2026-07-06-eda-teste/index.qmd`

**Resumo (aparece no card):** eda 2

> eda 1111


