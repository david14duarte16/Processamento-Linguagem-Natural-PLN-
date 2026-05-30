# Teste de Estresse Semântico (Transformers vs RNNs)

- **Texto A:** "O atendimento da loja foi um espetáculo, mas o produto final é uma porcaria." 
- **Texto B:** "O produto final foi um espetáculo, mas o atendimento da loja é uma porcaria."

### Abordagem Estatística (Naive Bayes)
O Naive Bayes não sabe qual adjetivo é para qual sujeito porque o Bag-of-Words perde toda a ordem das palavras. Como as frequências de "espetáculo" e "porcaria" são iguais em ambas as frases, a classificação empata.

### Abordagem Sequencial (LSTMs)
A LSTM processa as palavras uma a uma, guardando o contexto temporal. Ela sabe diferenciar as duas frases. O problema é que o treino sequencial (`.fit()`) é muito lento e o modelo ainda corre o risco de esquecer o início de textos muito longos (Vanishing Gradient).

### A Era dos Transformers
Os Transformers leem tudo de uma vez. O mecanismo de *Self-Attention* cruza matematicamente a palavra "porcaria" com a frase toda e gera um peso forte de conexão com "produto" no Texto A e com "atendimento" no Texto B, resolvendo a ambiguidade instantaneamente.

---

### Trade-off Técnico: Acurácia vs Custo Computacional

| Arquitetura | Acurácia Semântica | Custo Computacional |
| :--- | :--- | :--- |
| **Naive Bayes (TF-IDF)** | Baixa (Perde o contexto) | Muito Baixo e rápido |
| **LSTMs** | Boa (Processamento sequencial) | Alto (Lento) |
| **Transformers** | Excelente (Atenção bidirecional) | Baixo via fine-tuning (Hugging Face) |

### Justificativa de Hardware (Por que abandonar LSTMs?)
LSTMs calculam uma palavra só depois da outra, criando um gargalo sequencial. Os Transformers calculam tudo ao mesmo tempo multiplicando matrizes (Autoatenção). O mercado trocou as LSTMs pelos Transformers porque as GPUs atuais são desenhadas para executar milhões de cálculos matriciais em paralelo, acelerando absurdamente o treinamento.
