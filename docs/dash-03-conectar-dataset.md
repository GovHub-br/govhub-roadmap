# Conectar um dashboard a um novo dataset

> [!TODO] Esqueleto — o conteúdo ainda precisa ser escrito e validado com quem mantém dashboards no GovHub hoje.

Como apontar um dashboard que já existe para uma nova tabela ou view, sem recriar os gráficos do zero.

## Quando usar isto

- Uma tabela `gold` foi substituída por outra com nome diferente
- Você quer reaproveitar o layout de um dashboard para outro recorte (outro órgão, outro ano)
- O dataset atual virou lento e existe uma versão materializada

## Pré-requisitos

- Permissão de edição no dashboard (veja [Permissões e papéis](#doc/dash-08-permissoes-papeis))
- A nova tabela já disponível no Postgres e visível para o Superset

## Passos

1. *A escrever: registrar o novo dataset.*
2. *A escrever: conferir se as colunas usadas pelos gráficos existem com o mesmo nome e tipo.*
3. *A escrever: trocar o dataset em cada gráfico (ou usar "Swap dataset", se disponível na versão em uso).*
4. *A escrever: revisar métricas calculadas e colunas derivadas, que não migram sozinhas.*
5. *A escrever: salvar e recarregar o dashboard.*

## Verificar se deu certo

*A escrever: o que conferir — totais batem com a fonte, filtros ainda aplicam, nenhum gráfico com erro.*

## Problemas comuns

| Sintoma | Causa provável | O que fazer |
| --- | --- | --- |
| Gráfico vazio depois da troca | Coluna renomeada na nova tabela | *a escrever* |
| Erro de tipo na métrica | Coluna mudou de `text` para `numeric` (ou o inverso) | *a escrever* |
| Filtro parou de aplicar | Filtro nativo ainda aponta pro dataset antigo | *a escrever* |

## Ver também

- [Manter um dashboard existente](#doc/dash-06-manter-dashboard)
