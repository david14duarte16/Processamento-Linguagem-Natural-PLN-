# Exemplo 1: Briefing do Problema (O Cenário)
#Dataset de Trabalho:
corpus = [
    "o processamento de linguagem natural é incrível", 
    "linguagem natural e inteligência artificial",
    "o processamento de linguagem e inteligência",
    "artificial incrível e natural",
    "inteligência é incrível"
]

# Módulo 1: Entendendo o Componente TF (Term Frequency)
from sklearn.feature_extraction.text import CountVectorizer 
import pandas as pd

vectorizer = CountVectorizer()
tf_matrix = vectorizer.fit_transform(corpus)

# Visualizando como DataFrame para análise
df_tf = pd.DataFrame(tf_matrix.toarray(), columns = vectorizer.get_feature_names_out()) 
print("Matriz de Frequência Bruta (TF):")
display(df_tf)

# Módulo 2: 0 Peso do Mundo (Inverse Document FrequencyIDF)
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
# Mapeando termos aos seus pesos IDF
df_idf = pd.DataFrame(tfidf_vectorizer.idf_, index=tfidf_vectorizer.get_feature_names_out(), columns=["Peso IDF"])
print("Pesos IDF (Quanto maior, mais rara/importante é a palavra no contexto global):") 
display(df_idf.sort_values (by="Peso IDF", ascending=False))

# Módulo 3: Construindo a Matriz TF-IDF Final
df_tfidf_final = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out()) 
print("Matriz TF-IDF Final (Normalizada):")
display(df_tfidf_final)

############################################################

# Exemplo 2 - Soneto de Fidelidade
from sklearn.feature_extraction.text import TfidfVectorizer
# Poema dividido em estrofes
poema_estrofes = [
    "De tudo, ao meu amor serei atento antes",
    "E antes de mais nada, com tal zelo e sempre",
    "E sempre e tanto que em vossa presença sinta",
    "Que o vosso amor não tenha, o meu amor não tenha",
    "Diante de ti meu coração se fez, e meu corpo se fez, e minha alma se fez",
    "Em cada verso que escrevi para ti, em cada palavra que te disse"
]

# Criar o objeto para a representação TF-IDF
vectorizer_tfidf = TfidfVectorizer()

# Fit and transform no texto
matriz_tfidf = vectorizer_tfidf.fit_transform(poema_estrofes)

print("--- TF-IDF para o Soneto de Fidelidade ---")
print (f"\nVocabulário (palavra: índice): {vectorizer_tfidf.vocabulary_}\n") 
print("Matriz TF-IDF (documentos x palavras):") 
print(matriz_tfidf.toarray())

############################################################

# Exemplo 3 – Pipeline completa com análise de livros

# Etapa 1 – Importação do Corpus
import nltk
from nltk.corpus import machado
nltk.download('machado')

# Etapa 2 – Abertura de arquivos
import zipfile 
import os

caminho_do_zip = '/root/nltk_data/corpora/machado.zip'
arquivo_zip = zipfile.ZipFile(caminho_do_zip, 'r')

pasta_destino = '/root/nltk_data/corpora/' 
os.makedirs(pasta_destino, exist_ok=True)
arquivo_zip.extractall(pasta_destino) # Onde você quer extrair

print (f"Arquivo {caminho_do_zip} extraído com sucesso para {pasta_destino}")

# Etapa 3 – Criação das coleção de documentos
# Função para ler e copiar o conteúdo de um arquivo (documento)
def ler(nome_arquivo):
    arquivo = open(nome_arquivo, 'r', encoding='iso-8859-1') # codificacao latin-1 
    conteudo_arq = arquivo.read()
    arquivo.close()
    return conteudo_arq

# Função para fazer a limpeza do texto
def limpar (lista):
    lixo = '., :;?!" ~~`^~( ) [ ] { }/\|@#$% ̈&*- '
    quase_limpo = [x.strip (lixo).lower() for x in lista]
    return [x for x in quase_limpo if x.isalpha() or '-' not in x]

# Geração dos endereços dos arquivos
obras = []

for i in range(1,10):
    obras.append('/root/nltk_data/corpora/machado/romance/marm' + str(i) + '.txt')

print (obras)
colecao = []
for obra in obras:
    texto = ler (obra)
    print (texto)
    palavras = limpar (texto.lower().split())
    colecao.append(palavras)

# Etapa 4 – Cálculo do TF-IDF
import math
def tf(termo, doc):
    return colecao [doc].count(termo) / len(colecao[doc])

def df (termo):
    return len([d for d in colecao if termo in d])

def idf(termo):
    return math.log10(len(colecao) / df (termo))

def tf_idf(termo, doc):
    return tf(termo, doc) * idf(termo)

tf('capitu',7)
#tf(termo, documento)

idf('capitu') 
#tf(termo)

tf_idf('capitu',7)
#tf(termo, documento)

# Função para listagem de ordenação pela relevância das palavras 
def mais_relevantes (doc):
    lista_total = [(tf_idf(p, doc), p) for p in set (colecao [doc])]

    return sorted(lista_total, reverse=True) [:50]

# Escolha do romance 
mr = mais_relevantes(7)
mr

############################################################

