# Questionário de Síntese - Semântica e Vetores

Responda as questões abaixo para consolidar a transição entre o código e a arquitetura de sistemas de linguagem:

**1. Diferenciação de Pesos:**
No TF-IDF (Aula 06), o peso de um termo é punido por sua onipresença global na coleção. No Word2Vec, como a frequência global de uma palavra impacta (ou não) sua posição no espaço vetorial em comparação com sua vizinhança imediata?

Ao contrário do TF-IDF, o Word2Vec não pune palavras muito frequentes. A posição do vetor foca mais no contexto local (as palavras vizinhas). A frequência global só é usada nos bastidores (como no subsampling) para ignorar stopwords e equilibrar o treinamento.

**2. Análise de Similaridade e Ironia:**
Se a similaridade de cosseno entre "entrega" e "atraso" for 0.98, mas o seu classificador de sentimentos indicar polaridade positiva em 40% desses casos, como o Word2Vec ajuda a identificar a ocorrência de ironia ou sarcasmo (tema da Aula 14)?

Se 'entrega' e 'atraso' aparecem muito juntas, o Word2Vec dá vetores parecidos para elas. Como 'atraso' é ruim, mas a frase deu 'positivo', isso gera uma contradição. O Word2Vec não entende ironia sozinho, mas os vetores que ele cria ajudam o classificador a perceber que a frase está sendo sarcástica.

**3. Compensação Dimensional:**
Explique a relação entre o `vector_size` definido no treinamento e a eficácia do parâmetro `perplexity` no t-SNE. O que ocorre com a "nitidez" dos clusters se o tamanho do vetor for subdimensionado para um corpus muito vasto?

O `vector_size` é o tamanho do vetor. Se for muito pequeno para um texto muito grande, palavras diferentes vão acabar caindo no mesmo lugar. Aí, quando tentarmos usar o t-SNE para visualizar, os clusters vão ficar todos borrados e misturados. Nem ajustando o parâmetro `perplexity` vai resolver, porque o vetor original já não tem espaço suficiente.
