# Os quatro tipos: teoria e modelos

Documentação técnica falha quase sempre pelo mesmo motivo: uma página tenta
ensinar, resolver, catalogar e justificar ao mesmo tempo. O leitor chega com
**uma** necessidade e precisa atravessar as outras três para achar a dele.

O Diátaxis separa por necessidade, não por assunto. "Airflow" não é um documento
— são quatro, e cada um serve a alguém em situação diferente.

| Tipo | O leitor está | Precisa de | Não quer |
|---|---|---|---|
| tutorial | aprendendo | um caminho único que funciona | opções, justificativas |
| guia | trabalhando | resolver um problema concreto | ser ensinado do zero |
| referência | consultando | achar um dado rápido | narrativa |
| explicação | estudando | entender o porquê | passo a passo |

Distribuição atual do repositório: 20 referências, 13 explicações, 10 guias e
**4 tutoriais**. O buraco é claro — falta material de aprender fazendo.

## Onde o conteúdo pertence

```
É sobre FAZER alguma coisa?
├── SIM: o leitor está APRENDENDO ou EXECUTANDO?
│   ├── aprendendo   → tutorial
│   └── executando   → guia
└── NÃO: ele quer FATOS ou ENTENDIMENTO?
    ├── fatos        → referência
    └── entendimento → explicação
```

O eixo que as pessoas erram é o primeiro. "Como configurar o Superset" parece
tutorial e quase sempre é guia: quem procura isso já sabe o que quer, só não
sabe os passos.

---

## tutorial — orientado a aprender

O leitor não sabe o que não sabe. Você o leva pela mão até um resultado que
funciona. O objetivo não é resolver o problema dele: é dar competência.

| | |
|---|---|
| **Forma** | passos numerados, do início ao fim |
| **Tom** | segunda pessoa, imperativo: "rode", "abra", "confira" |
| **Comandos** | exatos, prontos para colar, com a saída esperada |
| **Escolhas** | nenhuma — um caminho só |
| **Explicação** | mínima; linke a explicação para o porquê |

O erro fatal é oferecer alternativas. "Você pode usar Docker ou instalar
localmente" trava o iniciante, que não tem base para escolher. Escolha por ele e
mande o resto para um guia.

Todo passo precisa de um sinal observável de que deu certo. Sem isso o leitor não
sabe se pode seguir.

```markdown
# <Título>

> [!TODO] <o que ainda falta>

Ao final deste tutorial você vai ter <resultado concreto e verificável>.

Público: <quem>. Este é um **tutorial**: o caminho é único e o resultado é
garantido. Para consulta pontual, veja <link para a referência>.

## Antes de começar

- <pré-requisito com link>

## 1. <Primeira ação>

<o comando, e o que esperar de saída>

## 2. <Segunda ação>

## 3. <Terceira ação>

## Verificar que funcionou

<o sinal concreto: uma tela, uma saída, um status>

## O que você aprendeu

<o modelo mental, não os comandos>

## Próximos passos

- <link>
```

---

## guia — orientado a resolver

O leitor sabe o que quer e tem o básico. Está no meio de um trabalho e precisa de
uma sequência que resolva **um** problema.

| | |
|---|---|
| **Forma** | passos numerados, precedidos do objetivo |
| **Título** | costuma começar com "Como" |
| **Abertura** | o problema, não o conceito |
| **Pré-requisitos** | listados e linkados, nunca ensinados de novo |
| **Alternativas** | permitidas — diferente do tutorial |
| **Fecho** | como verificar, e os problemas comuns |

O erro comum é ensinar do zero. Isso duplica o tutorial e passa a envelhecer em
dois lugares. Pressuponha e linke.

```markdown
# <Como fazer X>

> [!TODO] <o que ainda falta>

<uma frase dizendo qual problema isto resolve>

## Quando usar isto

- <situação concreta>

## Pré-requisitos

- <o que precisa estar pronto, com link>

## Passos

1. <ação>
2. <ação>

## Verificar se deu certo

<como saber>

## Problemas comuns

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| | | |

## Ver também

- <link>
```

---

## referência — orientada a consultar

O leitor sabe exatamente o que procura. Quer achar e sair. Ninguém lê referência
de ponta a ponta.

| | |
|---|---|
| **Forma** | tabelas primeiro, prosa só nas notas |
| **Tom** | austero e neutro; sem narrativa, sem opinião |
| **Estrutura** | espelha o sistema descrito, não uma ordem didática |
| **Cobertura** | **todas** as opções, não só as comuns |
| **Cada item** | tipo, valor padrão, restrições |

Duas tentações a resistir: numerar passos (isso é guia) e explicar por que o
padrão é aquele (isso é explicação). Referência descreve o que **é**.

A completude é o valor aqui. Uma referência que cobre 80% das opções manda o
leitor para o código-fonte — e aí ele não volta.

```markdown
# <Título>

> [!TODO] <o que ainda falta>

<uma frase: o que este documento cataloga e quando consultar>

## <Tabela principal>

| Item | Tipo | Padrão | Descrição |
|---|---|---|---|
| | | | |

## Notas

<o que não cabe na tabela: limites, pegadinhas>

## Ver também

- <link>
```

---

## explicação — orientada a entender

O leitor não está executando nada. Quer entender uma decisão, um conceito, o
motivo de as coisas serem como são. Pode estar lendo no ônibus.

| | |
|---|---|
| **Forma** | texto corrido, discursivo |
| **Conteúdo** | contexto, história, alternativas consideradas |
| **Opinião** | permitida e desejável |
| **Diagramas** | úteis para conceitos com muitas partes |
| **Passo a passo** | nenhum |

A seção mais valiosa é a dos **limites**: onde a abordagem não serve. É o que
separa explicação de material de divulgação. Não corte.

```markdown
# <Título>

> [!TODO] <o que ainda falta>

<uma frase situando o assunto>

## O contexto

<qual problema existia antes desta peça>

## Como funciona

<o modelo mental, sem virar passo a passo>

## Por que essa escolha

<as alternativas consideradas e por que esta venceu>

## Limites e quando não se aplica

<onde a abordagem não serve — ser honesto aqui é o valor do documento>

## Ver também

- <link>
```

---

## Erros que aparecem em toda revisão

| Erro | Por que dói | Correção |
|---|---|---|
| Misturar tipos na mesma página | O leitor atravessa três necessidades alheias | Divida em documentos; linke |
| Tutorial que oferece escolhas | Trava quem não tem base para escolher | Um caminho; alternativas viram guia |
| Guia que ensina do zero | Duplica o tutorial e envelhece em dobro | Pressuponha e linke |
| Referência incompleta | Manda o leitor pro código-fonte | Documente todas as opções |
| Referência com narrativa | O dado some no meio do texto | Tabela primeiro |
| Explicação com comandos | Vira tutorial ruim | Tire os comandos |
| Explicação sem limites | Vira peça de marketing | Diga onde não serve |

## Diagnosticar o tipo errado

Se ao escrever você perceber que…

| …está | o tipo real é |
|---|---|
| numerando passos numa referência | guia ou tutorial |
| justificando uma decisão num tutorial | explicação (extraia) |
| ensinando o básico num guia | tutorial (linke, não repita) |
| listando parâmetros numa explicação | referência (extraia) |
| com duas seções que não conversam | dois documentos |

Teste rápido: se a página tem passo a passo **e** tabela de parâmetros, são dois
documentos. Passo a passo **e** justificativa de arquitetura, idem.

Quando extrair conteúdo para outro documento, crie o box correspondente no
roadmap. Documento sem box fica invisível — e `verificar.py` acusa.

---

## Créditos

A caracterização dos quatro quadrantes é adaptada de
[`docs-diataxis`](https://github.com/neo4j-labs/agent-memory/blob/main/.claude/skills/docs-diataxis/SKILL.md),
do projeto [neo4j-labs/agent-memory](https://github.com/neo4j-labs/agent-memory),
sob licença Apache 2.0.

Mudanças em relação ao original: removidas as partes específicas daquele projeto
(caminhos `docs/tutorials/`, sintaxe AsciiDoc e `xref:`, comandos `npm run`,
exemplos do modelo POLE+O); traduzido para português; tutoriais convertidos para
segunda pessoa, em vez do "we will" do original, acompanhando a convenção da
documentação do GovHub; acrescentados os modelos em Markdown e as tabelas de
diagnóstico.

O framework Diátaxis é de Daniele Procida — <https://diataxis.fr>.
