# Os quatro modelos

Cada documento serve a **uma** necessidade. O que define o tipo não é o assunto,
é a situação do leitor no momento em que abre a página.

| Tipo | O leitor está | Precisa de | Não quer |
|---|---|---|---|
| tutorial | aprendendo | um caminho único que funciona | opções, justificativas |
| guia | trabalhando | resolver um problema concreto | ser ensinado do zero |
| referência | consultando | achar um dado rápido | narrativa |
| explicação | estudando | entender o porquê | passo a passo |

Distribuição atual do repositório: 20 referências, 13 explicações, 10 guias e
**4 tutoriais**. O buraco é claro — falta material de aprender fazendo.

---

## tutorial

Ensina fazendo. Caminho único, resultado garantido. Se o leitor precisar decidir
algo, o tutorial falhou: decida por ele e explique a alternativa em outro lugar.

```markdown
# <Título>

> [!TODO] <o que ainda falta>

Ao final deste tutorial você vai ter <resultado concreto e verificável>.

Público: <quem>. Este é um **tutorial**: o caminho é único e o resultado é
garantido. Para consulta pontual, veja <link para a referência>.

## Antes de começar

- <pré-requisito com link>

## 1. <Primeira ação>

<o comando, e o que ele faz>

## 2. <Segunda ação>

## 3. <Terceira ação>

## Verificar que funcionou

<o sinal concreto: uma tela, uma saída, um status>

## O que você aprendeu

<o modelo mental, não os comandos>

## Próximos passos

- <link>
```

Regras: numere os passos. Todo comando vem com o que esperar de saída. Nunca
escreva "você pode também" — isso é guia.

---

## guia

Resolve **um** problema para quem já tem o básico. Começa pelo problema, não
pelo conceito.

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

Regras: o título costuma começar com "Como". Pressupõe o tutorial. Pode oferecer
alternativas — diferente do tutorial.

---

## referência

Descreve o que existe. O leitor já sabe o que procura e quer achar rápido.
Tabela primeiro, prosa depois.

```markdown
# <Título>

> [!TODO] <o que ainda falta>

<uma frase: o que este documento cataloga e quando consultar>

## <Tabela principal>

| Item | Descrição | Observações |
|---|---|---|
| | | |

## Notas

<o que não cabe na tabela: limites, valores padrão, pegadinhas>

## Ver também

- <link>
```

Regras: estrutura espelha a do sistema descrito, não uma ordem didática. Sem
"primeiro… depois…". Se der vontade de explicar o porquê, isso é explicação.

---

## explicação

Dá contexto. O leitor quer entender uma decisão, não executá-la.

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

Regras: pode ter opinião e história. **Não** tem passo a passo nem tabela de
parâmetros. A seção de limites é o que diferencia explicação de material de
divulgação — não a corte.

---

## Sinais de que o tipo está errado

| Você percebeu que… | O tipo real é |
|---|---|
| está numerando passos numa referência | guia ou tutorial |
| está justificando uma decisão num tutorial | explicação (extraia) |
| está ensinando o básico num guia | tutorial (linke, não repita) |
| está listando parâmetros numa explicação | referência (extraia) |
| o documento tem duas seções que não conversam | são dois documentos |

Quando extrair conteúdo para outro documento, crie o box correspondente no
roadmap. Documento sem box fica invisível — e `verificar.py` acusa.
