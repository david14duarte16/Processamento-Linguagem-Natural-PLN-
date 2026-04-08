# Tarefa 1.1: Crie uma nova célula no Google Colab e pratique com números.

# Integers (int) - para contagens, IDs, etc.
quantidade_livros = 100
print (f"Número de livros: {quantidade_livros}")

# Floats (float) - para médias, percentuais, etc.
media_avaliacoes = 4.5
print (f"Média das avaliações: {media_avaliacoes}") 
# Expressões matemáticas básicas
resultado = (5*2.5) + 3
print (f"Resultado da expressão: {resultado}")

############################################################

#Tarefa 1.2: Manipulando Strings.

# Strings são sequências de caracteres 
frase = "A linguística computacional é fascinante." 
print(f"A frase inteira: {frase}")

# Acesso por índice (o índice começa em 0) 
print(f"Primeiro caractere: {frase[0]}") 
print(f"Último caractere: {frase[-1]}")

# Acessando um trecho (slice)
print(f"Primeiras 12 letras: {frase[:12]}")

# Métodos de strings
print(f"Frase em maiúsculas: {frase.upper()}") 
print(f"Frase em minúsculas: {frase.lower()}")

############################################################

# Tarefa 1.3: Explorando Listas (mutáveis).

#Listas são coleções ordenadas e mutáveis (podem ser alteradas) 
palavras_chave = ["python", "pln", "dados"]
print (f"Lista original: {palavras_chave}")

# Adicionar um item
palavras_chave.append("linguagem")
print (f"Lista após adicionar: {palavras_chave}")

# Alterar um item
palavras_chave[0] = "programacao"
print(f"Lista após alteração: {palavras_chave}")

############################################################

# Tarefa 1.4: Explorando Tuplas (imutáveis).

# Tuplas são coleções ordenadas, mas imutáveis 
dados_livro = ("Título do Livro", "Autor", 2023) 
print (f"Dados do livro: {dados_livro}")

# Tentar alterar um item irá gerar um erro! 
# dados_livro [0] = "Novo Título"