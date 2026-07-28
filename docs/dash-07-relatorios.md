# Gerar e agendar relatórios

> [!TODO] Esqueleto — confirmar o que já está configurado no ambiente (SMTP, worker de agendamento) antes de escrever os passos.

Como tirar um recorte estático de um dashboard e como fazer isso acontecer sozinho, em intervalo fixo.

## Quando usar isto

- Um gestor precisa receber o número toda segunda-feira sem abrir o Superset
- É preciso anexar um recorte a um processo ou ofício

## Exportar sob demanda

*A escrever: exportar dashboard em PDF, gráfico em imagem, dados em CSV — onde fica cada opção e as limitações de cada formato.*

## Agendar envio recorrente

### Pré-requisitos de infraestrutura

*A escrever: confirmar se estão ativos no ambiente — SMTP configurado, Celery beat / worker, e o serviço de captura de imagem.*

### Configurar

1. *A escrever: criar o agendamento a partir do dashboard.*
2. *A escrever: definir periodicidade (cron), destinatários e formato.*
3. *A escrever: testar o envio antes de deixar rodando.*

## Alertas

*A escrever: diferença entre relatório recorrente e alerta condicional; quando um alerta é melhor que um relatório.*

## Problemas comuns

| Sintoma | Causa provável | O que fazer |
| --- | --- | --- |
| Relatório chega em branco | Serviço de captura sem acesso ao dashboard | *a escrever* |
| E-mail não chega | SMTP não configurado | *a escrever* |
| Agendamento nunca dispara | Worker de agendamento parado | *a escrever* |

## Ver também

- [Dashboard vivo vs. relatório estático](#doc/dash-09-dashboard-vs-relatorio)
