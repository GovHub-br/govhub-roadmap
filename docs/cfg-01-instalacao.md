# Instalação

> [!TODO] Estrutura e comandos vêm do roadmap visual desta página. Falta escrever o texto de cada passo, conferir as versões contra o `pyproject.toml` atual e validar num ambiente limpo.

Ao final deste tutorial você vai ter o ambiente local completo do GovHub rodando: Airflow, dbt, Postgres, Superset e Jupyter, todos no ar e conversando entre si.

Público: dev ou contribuidor. Este é um **tutorial** — o caminho é único e o resultado é garantido. Para consulta pontual de comandos, veja [Troubleshooting](#doc/cfg-07-troubleshooting).

> Esta página também existe em [formato roadmap visual](#instalacao), com cada etapa como um nó conectado.

## Antes de começar

| Ferramenta | Versão | Observação |
| --- | --- | --- |
| Git | — | *a escrever: assinatura de commits é obrigatória* |
| Docker | 24+ | com Compose 2 |
| Make | — | *a escrever* |
| Python | 3.11 | *a escrever: por que essa versão exata* |
| pipx | — | usado para instalar o Poetry isolado |
| Poetry | 1.8.5 | *a escrever: confirmar se a versão ainda é essa* |

## 1. Clonar o repositório

```bash
git clone <data-application-gov-hub>
cd data-application-gov-hub
```

*A escrever: URL real do repositório e como configurar a assinatura de commits antes do primeiro commit — veja [Git Workflow](#doc/cfg-06-git-workflow).*

## 2. Preparar o ambiente

```bash
make setup
```

Esse comando faz seis coisas:

1. Cria o `.env` a partir do `local.env`
2. Instala as dependências com Poetry
3. Configura os hooks do Git
4. Roda `build` e `up` do Docker Compose
5. Configura a conexão local do Airflow
6. Valida a configuração básica

*A escrever: o que fazer quando um desses passos falha, e quais variáveis do `.env` precisam ser preenchidas à mão.*

## 3. Verificar os serviços

| Serviço | Endereço | Como saber que subiu |
| --- | --- | --- |
| Airflow | `http://localhost:8080` | *a escrever* |
| Superset | `http://localhost:8088` | *a escrever* |
| Jupyter | `http://localhost:8888` | *a escrever* |
| PostgreSQL | `localhost:5432` | *a escrever* |

*A escrever: credenciais padrão de cada um e onde trocá-las.*

## Comandos do dia a dia

```bash
docker compose up -d      # sobe os serviços
docker compose logs -f    # acompanha os logs
docker compose down       # derruba tudo
make dev                  # ambiente de desenvolvimento
make dev-check            # verificações antes de commitar
make format               # formata o código
make lint                 # checa o estilo
make test                 # roda os testes
```

## O que você aprendeu

*A escrever: o ambiente local é uma réplica reduzida do stack em produção. Entender qual serviço faz o quê aqui é o que permite ler a arquitetura depois.*

## Próximos passos

- [Visão Geral da Arquitetura](#doc/arch-01-visao-geral)
- [Apache Airflow](#doc/data-08-apache-airflow)
- [dbt — Visão Geral](#doc/data-02-dbt-visao-geral)
- [Troubleshooting](#doc/cfg-07-troubleshooting)
