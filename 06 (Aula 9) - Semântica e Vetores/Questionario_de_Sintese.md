# Questionário de Síntese - Semântica e Vetores

**1. Diferenciação de Pesos:**
No TF-IDF, o peso cai se a palavra é muito comum. E no Word2Vec?
Diferente do TF-IDF, o Word2Vec não pune palavras frequentes. Ele define o vetor da palavra baseado no contexto local (as palavras ao redor dela). A frequência global é usada só para ignorar stopwords e otimizar o treino (subsampling).

**2. Análise de Similaridade e Ironia:**
Como o Word2Vec ajuda a achar ironia se "entrega" e "atraso" tiverem similaridade de 0.98, mas o sentimento der positivo?
Se os vetores de "entrega" e "atraso" são parecidos, eles aparecem nos mesmos contextos. Se a frase for classificada como "positiva", há uma contradição (ex: "ótimo atraso na entrega"). O Word2Vec não detecta ironia sozinho, mas aproxima as palavras para que o classificador perceba o contraste e identifique o sarcasmo.

**3. Compensação Dimensional:**
Qual a relação entre o `vector_size` no treino e a `perplexity` no t-SNE?
O `vector_size` define o tamanho do vetor. Se for muito pequeno para textos grandes, palavras sem relação vão cair no mesmo vetor por falta de espaço. Ao tentar visualizar com t-SNE, o parâmetro `perplexity` (que foca nos vizinhos) não vai funcionar bem, e os clusters ficarão misturados e sem nitidez.
