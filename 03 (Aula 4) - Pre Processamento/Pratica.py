# 1. Normalização de Texto e Remoção de Ruído:
# importa a biblioteca para trabalhar com expressões regulares 
import re
original = "Olá!!! Este é um exemplo de texto, com várias PONTUAÇÕES, símbolos #especiais, e LETRAS maiúsculas."
texto_limpo = re.sub(r'[^A-Za-zÀ-ÿ\s]', '',original)

#re.sub() função que realiza substituição
# r'[^A-Za-zÀ-ÿ\s]'>>> expressão regular que define um conjunto de caracteres a serem removidos
# [A-Za-zÀ-ÿ\s] >>> define um conjunto de caracteres de A até Z, a até z e acentos e espaços # ^faz a negação de uma expressão regular
#'' substitui a expressão regular por uma string vazia

texto_normalizado = texto_limpo.lower()

print(f'Texto original: {original}')
print(f'\nTexto limpo: {texto_limpo}')
print(f'\nTexto normalizado: {texto_normalizado}')

############################################################

# 2. Tokenização:
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
tokens = word_tokenize(texto_normalizado)
print (f'Texto original: {original}') 
print(f'\n\nTexto limpo: {texto_limpo}') 
print (f'\n\nTexto normalizado: {texto_normalizado}') 
print (f'\n\nTokens extraidos: {tokens}\n')

############################################################

# 3. Remoção de Stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
stopwords_pt = set(stopwords.words('portuguese'))
print(stopwords_pt)
tokens_sem_stopwords = [palavra for palavra in tokens if palavra.lower() not in stopwords_pt]
print(f'\n\nTokens extraidos: {tokens} + \n quantidade de tokens: {len(tokens)}')
print (f'\n\nTokens extraidos: {tokens_sem_stopwords} + \n quantidade de tokens: {len (tokens_sem_stopwords)}\n')

############################################################

# 4. Stemming e Lematização
from nltk.stem import RSLPStemmer
nltk.download('rslp')
stemmer = RSLPStemmer()
stemming = [stemmer.stem (palavra) for palavra in tokens_sem_stopwords] 
print(f'\n\nTokens extraidos: {tokens_sem_stopwords}')
print(f'\n\nTokens radicais: {stemming}\n\n\n')

# Lematização
# !pip install -U spacy
# !python -m spacy download pt_core_news_sm
import spacy
nlp = spacy.load("pt_core_news_sm")

# Juntamos os tokens em uma única string para o spacy processar 
texto_para_lematizar = " ".join(tokens_sem_stopwords)
doc = nlp(texto_para_lematizar)
tokens_lematizados = [token.lemma_ for token in doc]
print (f'Tokens sem stopwords: {tokens_sem_stopwords}') 
print (f'\nLemas gerados (lematização): {tokens_lematizados}')

############################################################

# 5. Estrutura de Pré Processamento de texto Completo

import re 
import spacy
import nltk
from nltk.corpus import stopwords
import string

# Baixar stopwords do NLTK (se necessário)
nltk.download('stopwords')
nltk.download('punkt_tab') 
nltk.download('wordnet')
nltk.download('rslp')

# Carregar modelo do spacy (português como exemplo, pode trocar para 'en_core_web_sm' se for inglês) 
nlp = spacy.load("pt_core_news_sm")

# Texto de exemplo (pode ser uma review ou trecho de notícia)
texto = "O Processamento de Linguagem Natural (PLN) é uma área essencial da inteligência artificial! Confira mais em: https://exemplo.com"

# 1. Normalização (remover acentos, transformar em minúsculas, etc.) 
def normalizar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'https?://\S+|www\.\S+', '', texto) # Remover URLs
    texto = re.sub(r'[^a-zA-Zá-úÁ-Úç¢ ]', '', texto) # Remover caracteres especiais (ajuste para outros idiomas)
    return texto

texto_normalizado = normalizar_texto(texto)

# 2. Tokenização (nltk)
tokens = nltk.word_tokenize(texto_normalizado, language='portuguese')
                            
# 3. Remoção de stopwords (nltk)
stopwords_pt = set(stopwords.words('portuguese'))
tokens_sem_stopwords = [token for token in tokens if token not in stopwords_pt]

# 4. Stemming (nltk)
stemmer = nltk. RSLPStemmer()
tokens_stem = [stemmer.stem(token) for token in tokens_sem_stopwords]

# 5. Lematização (spacy)
def lematizar_com_spacy (tokens):
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]

tokens_lematizados = lematizar_com_spacy(tokens_sem_stopwords)

# 6. Comparação
print("Texto Original: \n", texto)
print("\nTexto Normalizado: \n", texto_normalizado)
print("\nTokens: \n", tokens)
print("\nTokens Sem Stopwords: \n", tokens_sem_stopwords)
print("\nStemming: \n", tokens_stem)
print("\nLematização: \n", tokens_lematizados)