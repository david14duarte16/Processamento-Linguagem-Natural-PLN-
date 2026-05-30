# Análise Prática: SVM vs Naive Bayes e Validação

### Naive Bayes vs SVM
O SVM se sai melhor com textos longos pois constrói fronteiras robustas (hiperplanos) para lidar com a alta dimensionalidade da vetorização. Já o Naive Bayes é rápido, mas ingênuo, assumindo falsamente que as palavras não têm relação entre si. O aprendizado dessas regras ocorre sempre na função `.fit()`.

### Datasets Minúsculos e Validação
No primeiro teste, com só 9 frases, o modelo foi péssimo. A matriz de confusão mostrou que ele teve que "chutar" por falta de volume de dados para aprender padrões reais.

Usar Validação Cruzada melhorou a análise por testar o modelo em pedaços diferentes (folds). O Grid Search elevou a pontuação ao automatizar a busca pelos melhores hiperparâmetros para aquela amostra em vez de usar os padrões da biblioteca.

### Data Leakage (A Ilusão da Perfeição)
No segundo teste, simulamos uma base maior multiplicando a mesma lista por 20. O modelo atingiu 100% de acerto. Isso não significa que ele é bom, mas que sofreu Data Leakage (Vazamento de Dados): ele decorou o gabarito porque as frases do teste eram cópias idênticas às do treino.

Usar n-grams ou Grid Search não adianta nada num cenário viciado como esse. O modelo não generaliza e erraria gravemente em frases inéditas.
