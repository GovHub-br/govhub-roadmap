# Manter um dashboard existente

> [!TODO] Esqueleto — o conteúdo ainda precisa ser escrito e validado com quem mantém dashboards no GovHub hoje.

O que fazer quando um dashboard que funcionava para de funcionar, ou quando o schema por baixo dele muda.

## Quando usar isto

- Um gráfico quebrou depois de uma alteração no pipeline
- Uma coluna foi renomeada ou removida em um modelo dbt
- O dashboard ficou lento

## Schema mudou: o que fazer

1. *A escrever: identificar quais datasets dependem da tabela alterada.*
2. *A escrever: sincronizar as colunas do dataset no Superset.*
3. *A escrever: corrigir métricas e colunas calculadas que referenciam o nome antigo.*
4. *A escrever: revalidar filtros.*

## Gráfico quebrado

*A escrever: como ler a mensagem de erro do Superset, onde ver a query gerada, como testar essa query direto no Postgres.*

## Dashboard lento

*A escrever: cache, limite de linhas, agregação prévia em modelo dbt em vez de agregar na hora.*

## Versionar mudanças

*A escrever: export/import de dashboard, o que entra no Git, e como registrar quem mudou o quê.*

## Prevenção

*A escrever: comunicar mudança de schema antes de aplicar; testes dbt que pegariam a quebra antes do dashboard.*

## Ver também

- [Conectar um dashboard a um novo dataset](#doc/dash-03-conectar-dataset)
