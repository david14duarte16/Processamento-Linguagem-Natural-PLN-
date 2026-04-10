# Exemplo 1 – Aplicação do BoW
# importando a ferramenta que irá criar a representação numérica 
from sklearn.feature_extraction.text import CountVectorizer

# criando um corpus de documentos que será usado para criação do vocabulário 
documentos = [
    "gato e cachorro",
    "gato brinca com cachorro",
    "gato e rato",
    "Cachorro, gato e rato",
    "Gato",
    "Cachorro e rato"
]
# Criando um objeto para ser utilizado: transformar os documentos em vetores 
vectorizer = CountVectorizer()

# Criando a matriz de contagem
X = vectorizer.fit_transform(documentos)
    # fit >>> cria um vocabulário das palavras
    # transforme >>> conta a frequencia de cada palavra no corpus

# Imprimindo a Matriz e o Vocabulário gerado
print (f"Vocabulario: {vectorizer.vocabulary_}")
    # realiza o mapeamento do vocabulário para um índice da matriz

print("Matriz Bow:")
print (X.toarray())
    # mostra a frequencia de cada palavra dentro da matriz

############################################################

# Exemplo 2 – BoW com Soneto de Fidelidade
from sklearn.feature_extraction.text import CountVectorizer

# Poema dividido em estrofes, para simular documentos 
poema_estrofes = [
    "De tudo, ao meu amor serei atento antes",
    "E antes de mais nada, com tal zelo e sempre",
    "E sempre e tanto que em vossa presença sinta",
    "Que o vosso amor não tenha, o meu amor não tenha",
    "Diante de ti meu coração se fez, e meu corpo se fez, e minha alma se fez",
    "Em cada verso que escrevi para ti, em cada palavra que te disse"
]

# Criar o objeto para a representação Bow
vectorizer = CountVectorizer()

# Fit and transform no texto
matriz_bow = vectorizer.fit_transform(poema_estrofes)

print("--- Bag-of-Words (Bow) para o Soneto de Fidelidade ---") 
print (f"\nVocabulário (palavra: índice): {vectorizer.vocabulary_}\n") 
print("Matriz Bow (documentos x palavras):")
print(matriz_bow.toarray())

############################################################

# Problema da dimensionalidade
# Briefing do Problema (O Cenário)
import numpy as np 
import sys
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "o processamento de linguagem natural é incrível",
    "linguagem natural e inteligência artificial",
    "o processamento de linguagem e inteligência",
    "artificial incrível e natural",
    "inteligência é incrível"
]

############################################################

# Módulo 1: Construção Manual do Vocabulário (Hard Way)
def extrair_vocabulario(docs):
    """
    Transforma uma lista de frases em uma lista ordenada de termos únicos. 
    Foco: Normalização e Unicidade.
    """

    # 1. Normalização e Tokenização em uma única lista
    todos_os_tokens = []
    for frase in docs:
        tokens = frase.lower().split() # Tokenização bruta por espaço
        todos_os_tokens.extend(tokens)

    # 2. Garantia de Unicidade usando Set (Estrutura de Hash) 
    vocab_set = set (todos_os_tokens)

    # 3. Ordenação Alfabética para consistência de índices 
    vocab_ordenado = sorted(list (vocab_set))

    return vocab_ordenado

# Execução
vocabulario = extrair_vocabulario (corpus)
print (f"Vocabulário Ordenado ({len (vocabulario)} termos):") 
print (vocabulario)

############################################################

# Módulo 2: Matriz Termo-Documento e a "Explosão Dimensional"
def construir_matriz_densa(docs, vocab):
    """
    Cria uma Matriz Termo-Documento (D x V) usando NumPy. 
    Demonstra a alocação de memória para elementos nulos (zeros).
    """
    n_docs = len(docs)
    n_vocab = len(vocab)
    # Inicialização com zeros (8 bytes por célula usando int64) 
    matriz = np.zeros((n_docs, n_vocab), dtype=np.int64)
    
    for i, frase in enumerate(docs):
        tokens_frase = frase.lower().split() 
        for j, termo in enumerate (vocab):
            # Contagem de frequência
            matriz[i][j] = tokens_frase.count(termo)
    return matriz

matriz_final = construir_matriz_densa(corpus, vocabulario) 
print("Matriz Termo-Documento (Representação Densa NumPy):") 
print (matriz_final)

############################################################

# Módulo 3: O Problema da Esparsidade (The Pythonic Way)

# 1. Vetorização Profissional
vectorizer = CountVectorizer()
X_esparso = vectorizer.fit_transform(corpus)

# 2. Conversão para Denso apenas para fins de comparação didática
X_denso = X_esparso.toarray()

# 3. Prova Matemática de Desperdício (RAM)
# Para matrizes esparsas, somamos os arrays de dados, índices e ponteiros
memoria_esparsa = X_esparso.data.nbytes + X_esparso.indptr.nbytes + X_esparso.indices.nbytes 
memoria_densa = X_denso.nbytes

# 4. Cálculo de Esparsidade
total_celulas = X_denso.size
zeros = total_celulas - np.count_nonzero (X_denso)
percentual_zeros = (zeros / total_celulas) * 100

print (f" Relatório de Performance de Memória ---")
print (f"Memória RAM (Matriz Densa): {memoria_densa} bytes")
print (f"Memória RAM (Matriz Esparsa): {memoria_esparsa} bytes")
print (f"Eficiência de Memória: {((memoria_densa - memoria_esparsa) / memoria_densa) * 100:.2f}% de economia") 
print (f"Porcentagem de Esparsidade: {percentual_zeros: .2f}% de zeros na matriz")
