# Criar seu primeiro dashboard do zero

> [!TODO] Esqueleto — o conteúdo ainda precisa ser escrito e validado com quem mantém dashboards no GovHub hoje.

Ao final deste tutorial você vai ter um dashboard funcionando no Superset, ligado a uma tabela real do GovHub, com pelo menos dois gráficos e um filtro.

Este é um **tutorial**: o caminho é guiado e o resultado é garantido. Não explica todas as opções — para isso veja [Tipos de gráfico e quando usar cada um](#doc/dash-05-tipos-de-grafico).

## Antes de começar

- Ambiente local rodando (veja **Instalação**), com o Superset em `http://localhost:8088`
- Credenciais de acesso ao Superset
- Pelo menos uma tabela `gold` disponível no Postgres

## 1. Entrar no Superset

*A escrever: login, o que a tela inicial mostra, onde ficam Datasets / Charts / Dashboards.*

## 2. Registrar o dataset

*A escrever: Data → Datasets → + Dataset, escolher o schema e a tabela, salvar.*

## 3. Criar o primeiro gráfico

*A escrever: a partir do dataset, escolher tipo de gráfico, definir métrica e dimensão, rodar a query, salvar com nome.*

## 4. Criar o segundo gráfico

*A escrever: repetir com um recorte diferente (ex: série temporal) para ter dois ângulos do mesmo dado.*

## 5. Montar o dashboard

*A escrever: Dashboards → + Dashboard, arrastar os dois gráficos, ajustar o layout, salvar.*

## 6. Adicionar um filtro

*A escrever: filtro nativo por uma coluna, aplicar aos dois gráficos, testar.*

## O que você construiu

*A escrever: recapitular a cadeia tabela → dataset → gráfico → dashboard, e por que essa separação existe.*

## Próximos passos

- [Conectar um dashboard a um novo dataset](#doc/dash-03-conectar-dataset)
- [Adicionar filtros e drill-down](#doc/dash-04-filtros-drill-down)
- [Manter um dashboard existente](#doc/dash-06-manter-dashboard)
