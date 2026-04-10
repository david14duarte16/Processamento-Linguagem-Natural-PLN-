# Exemplo 1: Tokenização Manual

texto = 'casa, casa' 
palavras = texto.split() 
print (palavras)
texto_exemplo = "olá, mundo! Como vai você?" 
print (f"Texto original: '{texto_exemplo}'")

# A função .split() quebra a string em uma lista de strings 
tokens = texto_exemplo.split()
print (f"Tokens (divididos por espaço): {tokens}") 
print(len(tokens))

texto_com_pontuacao = "Olá, mundo! Como vai você?"
tokens_com_pontuacao = [] 
token_atual = ""

# Percorremos cada caractere do texto
for caractere in texto_com_pontuacao:
    # Verificamos se o caractere é uma letra ou um número 
    if caractere.isalnum():
        token_atual += caractere # Adiciona o caractere ao token atual
    else:
        # Se o caractere não for alfanumérico, é uma pontuação ou espaço 
        if token_atual:
            tokens_com_pontuacao.append(token_atual)
            token_atual = ""
        # Adiciona a pontuação como um token separado, se não for um espaço 
        if caractere.isspace() == False:
            tokens_com_pontuacao.append(caractere)

# Adiciona o último token após o loop
if token_atual:
    tokens_com_pontuacao.append(token_atual)

print (f"Tokens com pontuação separada: {tokens_com_pontuacao}") 
print (len(tokens_com_pontuacao))

############################################################

# Exemplo 2: Tokenização Manual

import unicodedata

texto_acentuado = "Vocês já pensaram na água do Oceano? É fascinante!" 
print (f"Texto original: '{texto_acentuado}'")

# Normaliza a string para a forma 'NFD' (Normalized Form Decomposition) 
# que separa o caractere base (ex: 'e') do acento (ex: ''') 
texto_normalizado = unicodedata.normalize('NFD', texto_acentuado)

# Filtra a string para manter apenas os caracteres sem acento 
texto_sem_acentos = ''.join(
    [char for char in texto_normalizado if char.isalnum() or char.isspace()]
)   

print (f"Texto sem acentos: '{texto_sem_acentos}'")

import re

# Adicione esta função para tokenizar e limpar o texto de forma completa 
def tokenizar_e_limpar (texto):
    # 1. Converte o texto para minúsculas 
    texto = texto.lower()
    
    # 2. Normaliza para remover acentos
    texto_normalizado = unicodedata.normalize('NFD', texto)

    # 3. Usa uma expressão regular para remover pontuação e caracteres não-alfanuméricos 
    # 0 [^\w\s] remove qualquer coisa que não seja letra, número ou espaço
    texto_limpo = re.sub (r'[^\w\s]', '', texto_normalizado, re.UNICODE)
    
    # 4. Quebra o texto em tokens (palavras)
    tokens = texto_limpo.split()
    return tokens

# Usamos a função para processar o texto original 
tokens_finais = tokenizar_e_limpar (texto_acentuado)
print (f"Tokens finais (limpos e sem acentos): {tokens_finais}")

############################################################

# Exemplo 3: Identificando Padrões Simples

import re

# Exemplo de comentário sujo de e-commerce
comentario_bruto = "O produto é excelente!!!!!! Mas a entrega... atrasou. :( "

# Removendo pontuação excessiva com Regex
# O padrão [^\w\s] significa: "pegue tudo que NÃO for letra, número ou espaço" 
comentario_limpo = re.sub (r'[^\w\s]', '', comentario_bruto)

print (f"Bruto: {comentario_bruto}") 
print(f"Limpo: {comentario_limpo}")

############################################################

# Exemplo 4: Removendo Lixo da Web

def faxina_web(texto):
    # Remove tags HTML (ex: <p>)
    texto = re.sub (r'<.*?>', '', texto)
    # Remove URLs (http/https)
    texto = re.sub (r'http\S+', '', texto)
    return texto.strip()

print(faxina_web ("<p>Confira a oferta em: https://loja.com/promo</p>"))

############################################################

# Exemplo 5: Tokens vs. Types

import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

frase = "O preço é R$ 3.500,00, ok?"
tokens = word_tokenize(frase.lower()) # Normalizando para minúsculas

print(f"Tokens: {tokens}")
print(f"Total de Tokens: {len(tokens)}")
print(f"Total de Types (Vocabulário Único): {len(set(tokens))}") # Usando sets