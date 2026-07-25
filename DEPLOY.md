# Conexão Estatística: guia de implantação no servidor

Este documento resume o que a equipe do servidor precisa saber para hospedar
o **Conexão Estatística** (site do Departamento de Estatística da UFLA, construído
com [Quarto](https://quarto.org)).

Há dois cenários possíveis. Na dúvida, o **Cenário 1** é o recomendado:
é o mais simples e o que o fluxo atual do projeto já pratica.

---

## Cenário 1: o servidor apenas hospeda o site pronto (recomendado)

O site é renderizado na máquina de quem edita e o resultado fica na pasta
**`docs/`** (definida em `output-dir`, no `_quarto.yml`): apenas HTML, CSS,
JavaScript e imagens **estáticos**.

**Requisitos no servidor:**

- Qualquer servidor web capaz de servir arquivos estáticos (Apache, Nginx,
  IIS…) com **HTTPS**;
- Nenhum software adicional: **não** é preciso Quarto, Python, R, Chrome ou
  banco de dados.

### Serviços externos consumidos pelo navegador do visitante

O servidor não faz nenhuma chamada externa, mas as páginas carregam recursos
de terceiros **no navegador de quem visita**. Se houver filtragem de saída ou
política de domínios na rede institucional, estes são os domínios usados:

| Domínio | Onde / para quê |
|---|---|
| `fonts.googleapis.com`, `fonts.gstatic.com` | fonte Inter (todas as páginas) |
| `unpkg.com` | biblioteca Leaflet (mapa de rota da página inicial) |
| `tile.openstreetmap.org` | imagens (tiles) do mapa de rota |
| `router.project-osrm.org` | cálculo de rota até o DES na página inicial |
| `nominatim.openstreetmap.org` | busca do endereço digitado pelo visitante |
| `www.google.com/maps` | mapa institucional (My Maps) embutido na página inicial |
| `www.youtube.com` | vídeo embutido na página "Estatística" |
| `github.com` | formulário "Envie seu projeto" (issues) e links de código |
| `des.ufla.br`, `biometria.ufla.br` | links institucionais |

**Observações para avaliação da TI:**

1. **OSRM e Nominatim** são serviços públicos de demonstração da comunidade
   OpenStreetMap, sem garantia de disponibilidade e com limite de uso
   (~1 requisição/s). Para o tráfego esperado do site é adequado; se a
   instituição preferir, o recurso de rota pode ser removido ou apontado
   para uma instância própria.
2. **Cookies de terceiros**: os embeds de YouTube e Google Maps definem
   cookies. Se houver exigência institucional (LGPD), o vídeo pode ser
   trocado para `youtube-nocookie.com` com ajuste mínimo.
3. **CDNs**: se a política proibir CDNs externos, a fonte Inter e o Leaflet
   podem ser embutidos no próprio site (mudança pequena no código).
4. **Endereço final**: o `_quarto.yml` define `site-url: https://des.ufla.br/`.
   Se o site for publicado em outro domínio ou subcaminho
   (ex.: `des.ufla.br/conectastat/`), esse valor deve ser atualizado para o
   sitemap e as prévias de link (Open Graph) saírem corretos.

---

## Cenário 2: o servidor renderiza o site (CI/CD ou tarefa agendada)

Só se aplica se o próprio servidor executar `quarto render` (por exemplo, um
pipeline que renderiza a cada commit). Requisitos:

1. **Quarto** instalado (versão 1.4 ou superior);
2. **Python 3** com os pacotes `selenium` e `pillow`, instalados **no mesmo
   Python que o Quarto usa**. Em servidores com múltiplas versões de Python,
   defina a variável de ambiente `QUARTO_PYTHON` apontando para o
   interpretador correto (essa divergência é a causa mais comum de falha);
3. **Chromium/Chrome** instalado, para uso *headless* (sem interface gráfica;
   não é necessário X/xvfb; o script usa `--headless=new`);
4. **Saída para a internet durante o build** (na primeira execução, o
   Selenium baixa automaticamente o chromedriver compatível). Em servidor
   sem acesso externo, pré-instale o chromedriver; depois do primeiro uso,
   o cache local basta;
5. **Memória**: o Chrome headless consome de 300 a 500 MB enquanto gera capas,
   e só é aberto quando existe post sem capa;
6. **Escrita no diretório de trabalho**: o gerador de capas cria o
   `thumbnail.png` dentro da pasta de cada post e preenche o campo `image:`
   no `.qmd` correspondente.
   Em CI com checkout descartável, essas mudanças não voltam ao repositório:
   ou o pipeline faz commit delas, ou (mais simples) as capas são geradas
   localmente pelo editor antes do push; nesse caso o passo automático não
   encontra nada a fazer e é praticamente instantâneo.

**O que o servidor NÃO precisa em nenhum cenário:** R, Jupyter ou LaTeX.
Os posts do site são markdown puro e os relatórios dos estudantes chegam
como HTML pronto: nada de código é executado durante a renderização.

---

## Automação de capas (thumbnails)

O projeto tem um passo automático registrado como `pre-render` no
`_quarto.yml`: a cada `quarto render` completo, o script
`scripts/gerar_thumbnails.py` verifica os posts sem `image:` e gera a capa
sozinho (o gráfico/mapa mais colorido do relatório, nos projetos dos
estudantes; uma figura colorida do corpo ou a "foto do título", nas demais
seções). O recorte é 16:9 (1200×675) e o `image:` do post é preenchido
automaticamente.

**Comportamento à prova de falhas:** se faltar Chrome, Python ou biblioteca,
o script apenas registra um aviso no log e a renderização do site **segue
normalmente** (o post fica sem capa até a próxima execução). A publicação
nunca é bloqueada por causa das capas.

Uso manual, quando necessário:

```bash
python scripts/gerar_thumbnails.py            # gera capas de quem não tem
python scripts/gerar_thumbnails.py --force    # regenera todas
python scripts/gerar_thumbnails.py <slug>     # apenas posts específicos
```

---

## Fluxo de publicação recomendado

1. Editor cria/edita posts (`.qmd`) na máquina local;
2. `quarto render` (as capas que faltam são geradas automaticamente);
3. Commit (incluindo `docs/`, os `.qmd` atualizados e as thumbnails);
4. O servidor recebe/serve o conteúdo de `docs/` como arquivos estáticos.
