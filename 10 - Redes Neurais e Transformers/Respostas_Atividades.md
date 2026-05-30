# DESAFIO: O Teste de Estresse Semântico em E-Commerce

## Contexto das Frases de Teste
- **Texto A:** "O atendimento da loja foi um espetáculo, mas o produto final é uma porcaria." 
- **Texto B:** "O produto final foi um espetáculo, mas o atendimento da loja é uma porcaria."   

## Passo 1: O Teste Clássico (Bag-of-Words / Naive Bayes)

**Análise Crítica:** O Naive Bayes atribui a mesma probabilidade para as duas frases porque ele usa Bag-of-Words (saco de palavras). Ele ignora completamente a ordem das palavras e o contexto. Ele apenas conta que "espetáculo" e "porcaria" aparecem uma vez em cada frase, resultando no mesmo peso exato para ambos os casos. A propriedade linguística ignorada aqui é a semântica e a sintaxe (ordem e conexão entre os termos).  

## Passo 2: O Teste com Memória Recorrente (SimpleRNN / LSTM)

**Análise Crítica:** A rede recorrente (RNN/LSTM) conseguiu diferenciar porque ela processa a frase palavra por palavra, em sequência, o que ajuda a manter a ordem das informações. O tempo do `.fit()` foi muito maior (mais lento) em comparação com o Naive Bayes, justamente porque as redes neurais calculam retropropagação e processamento sequencial. Se a reclamação tivesse 3 páginas, a SimpleRNN esqueceria o início do texto devido ao problema do "Vanishing Gradient" (desvanecimento do gradiente). Mesmo trocando para a célula LSTM, que tem portas de memória, um texto gigantesco de 3 páginas ainda prejudicaria bastante a performance.  

## Passo 3: A Era dos Transformers e Hugging Face

**Análise Crítica (Autoatenção/Self-Attention):** O Transformer não lê em sequência. Ele usa a matriz de "Self-Attention" para calcular o peso de conexão de cada palavra com todas as outras ao mesmo tempo. Matematicamente, ele cruzou a palavra "porcaria" com a frase toda e gerou um peso enorme de conexão para "produto" no Texto A, e para "atendimento" no Texto B. Ele entende quem é o alvo de quem.  

## Entregáveis Finais

### Tabela Comparativa: Acurácia Semântica vs. Custo de Treinamento

| Modelo | Acurácia Semântica | Custo de Treinamento |
| :--- | :--- | :--- |
| **Naive Bayes (TF-IDF)** | Ruim | Muito Baixo |
| **LSTM (Rede Recorrente)** | Boa | Alto (processamento sequencial) |
| **Transformers** | Excelente | Original Altíssimo (baixo usando pipeline Hugging Face) |

### Justificativa Técnica (Arquitetura e GPUs)
O mercado abandonou as LSTMs em favor dos Transformers por causa da arquitetura de hardware. Uma LSTM precisa processar a palavra 2 para só então processar a palavra 3, criando um gargalo. O Transformer processa todas as conexões simultaneamente através de mapeamento de matrizes (Autoatenção). Como as GPUs (Placas de Vídeo) são feitas especificamente para rodar cálculos de matrizes gigantes em paralelo, os Transformers escalam de forma absurdamente mais rápida que as redes recorrentes clássicas.
