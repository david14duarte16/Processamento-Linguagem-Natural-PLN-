# Respostas e Diagnósticos das Atividades

## Discussão (Tarefa 3.4)

**Qual modelo foi mais preciso? Por quê? Pensem nas diferenças conceituais entre o Naive Bayes e o SVM.**

Resposta: O modelo SVM costuma se sair melhor com textos longos porque lida muito bem com várias colunas criadas na vetorização. O Naive Bayes é mais rápido, mas ele parte da ideia de que as palavras não têm relação nenhuma umas com as outras, o que nem sempre funciona bem em linguagem natural. Além disso, a função .fit() é exatamente o momento em que esses modelos leem os dados de treino e aprendem as regras.

## Exemplo 1 (Dataset Pequeno) - Diagnóstico

**Por que a acurácia e o F1-score estão tão baixos? O que a matriz de confusão nos diz sobre o que ele "aprendeu"?**

Resposta: Estão baixos porque nossa base de dados é muito pequena (só 9 frases). Olhando a matriz de confusão, dá pra ver que o modelo quase não aprendeu os padrões. Ele teve que "chutar" na maior parte das vezes, trocando as classificações e errando bastante.

## Exemplo 1 (Dataset Pequeno) - Otimização e Grid Search

**A pontuação média com Validação Cruzada é a mesma que a do primeiro passo? A pontuação final melhorou com o Grid Search?**

Resposta: A média da Validação Cruzada muda porque ela fatia os dados e faz testes em pedaços diferentes, o que é mais confiável. Com o Grid Search, a pontuação melhorou um pouco porque o algoritmo testou combinações automaticamente e achou configurações (hiperparâmetros) menos genéricas para os nossos dados.

## Exemplo 2 (Dataset Maior) - Diagnóstico

**Por que o modelo alcançou a perfeição logo de cara? O que a qualidade dos dados e o uso de n-grams têm a ver com isso?**

Resposta: Alcançou a "perfeição" porque simulamos um aumento de base multiplicando a mesma lista por 20 (* 20). Isso causou vazamento de dados (Data Leakage): as frases do teste eram cópias idênticas do treino, então o modelo só decorou o gabarito. Os n-grams ajudam a captar contextos e unir palavras, mas nesse cenário específico o bom resultado foi só ilusão da repetição.

## Exemplo 2 (Dataset Maior) - Validação e Grid Search

**O que os scores da validação nos dizem? O modelo está realmente robusto? A otimização melhorou a pontuação?**

Resposta: Os scores indicam 100% de acerto em todos os testes, mas o modelo não está robusto. Se passarmos uma frase totalmente nova, ele pode errar feio, pois só sabe classificar aquele bloco pequeno que repetimos. Por causa disso, o Grid Search não teve nenhum efeito real; a pontuação já estava no limite máximo desde o início.
