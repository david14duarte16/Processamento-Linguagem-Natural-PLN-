import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer

# 1. Escolha do Dataset:
df = pd.read_csv("04 (Aula 5) - Representação Numérica/olist_order_reviews_dataset.csv", nrows=5000)

print("Primeiras linhas do dataset:")
print(df.head())

############################################################

# 2. Carga e Limpeza:
coluna_texto = "review_comment_message"

# Remover valores nulos
df = df.dropna(subset=[coluna_texto])

print(f"\nTotal de reviews após limpeza de nulos: {len(df)}")

def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'<.*?>', '', texto)       # remove HTML
    texto = re.sub(r'http\S+', '', texto)     # remove URLs
    texto = re.sub(r'[^\w\s]', '', texto)     # remove símbolos
    return texto

df["texto_limpo"] = df[coluna_texto].apply(limpar_texto)

print("\nExemplo de texto original:")
print(df[coluna_texto].iloc[0])

print("\nExemplo de texto limpo:")
print(df["texto_limpo"].iloc[0])

############################################################

# 3. Vetorização
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(df["texto_limpo"])

print("\nFormato da matriz (documentos x palavras):", X.shape)

############################################################

# 4. Análise de Stress

# Memória esparsa
memoria_esparsa = X.data.nbytes + X.indptr.nbytes + X.indices.nbytes

# Tentativa de converter para denso
try:
    X_denso = X.toarray()
    memoria_densa = X_denso.nbytes
    erro_memoria = False
except:
    print("\nNão foi possível converter para denso (memória insuficiente)")
    memoria_densa = None
    erro_memoria = True

# Converter para MB
memoria_esparsa_mb = memoria_esparsa / (1024 * 1024)

print(f"\nMemória (esparsa): {memoria_esparsa_mb:.4f} MB")

if not erro_memoria:
    memoria_densa_mb = memoria_densa / (1024 * 1024)
    economia = memoria_densa_mb - memoria_esparsa_mb

    print(f"Memória (densa): {memoria_densa_mb:.4f} MB")
    print(f"Economia de memória: {economia:.4f} MB")

############################################################

# 5. Entregável
print("\n===== RELATÓRIO FINAL =====")

if not erro_memoria:
    print(f"""
Foi aplicada a técnica Bag-of-Words (BoW) utilizando o CountVectorizer
no dataset de reviews do Olist.

A matriz gerada é altamente esparsa, ou seja, possui muitos valores zero.

Memória utilizada (esparsa): {memoria_esparsa_mb:.4f} MB
Memória utilizada (densa): {memoria_densa_mb:.4f} MB

Economia de memória: {economia:.4f} MB

Conclusão:
O uso de matriz esparsa reduz significativamente o consumo de memória,
tornando o processamento mais eficiente e viável em ambientes de nuvem.
""")
else:
    print(f"""
Foi aplicada a técnica Bag-of-Words (BoW) utilizando o CountVectorizer
no dataset de reviews do Olist.

A matriz gerada é altamente esparsa.

A tentativa de conversão para matriz densa falhou devido ao alto consumo de memória.

Conclusão:
Isso demonstra que matrizes densas são inviáveis para grandes volumes de dados,
e reforça a importância do uso de matrizes esparsas para otimizar recursos
em ambientes de nuvem.
""")