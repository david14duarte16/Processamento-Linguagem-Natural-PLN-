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

############################################################

# Tarefa 1.5: Use um conjunto para remover palavras duplicadas.
tokens = ["o", "rato", "roeu", "a", "roupa", "do", "rei", "de", "Roma", "o", "rato"] 
print(f"Tokens originais: {tokens}")

# Converter a lista para um conjunto para obter itens únicos
vocabulario = set (tokens)
print(f"Vocabulário (itens únicos): {vocabulario}")

############################################################

# Tarefa 1.6: Mapeie termos de PLN com suas definições.
terminos_pln = {
    'corpus': 'Coleção de textos', 
    'token': 'Unidade de texto',
    'stopwords': 'Palavras comuns sem muito significado'
}

# Acessar um valor pela chave
print(f"Definição de 'token': {terminos_pln['token']}")

# Adicionar um novo item
terminos_pln['lematizacao'] = 'Redução de palavras ao seu lema' 
print(f"Dicionário atualizado: {terminos_pln}")

############################################################

#Tarefa 2.1: Pratique com if, elif e else.
ano_publicacao = 1985
if ano_publicacao < 1901:
    print("Romance anterior ao século XX.")
elif ano_publicacao >= 1901 and ano_publicacao < 2000:
    print("Romance do século XX.")
else:
    print("Romance do século XXI.")

# Testando inclusão com 'in'
frase_teste = "Python é a melhor linguagem." 
if 'Python' in frase_teste:
    print("A frase menciona Python.")

############################################################

# Tarefa 2.2: Use um loop for para iterar sobre uma lista de palavras. 
palavras_para_analise = ["computador", "dados", "linguagem"]
for palavra in palavras_para_analise:
    print (f"A palavra atual é: {palavra}")

############################################################

# Tarefa 2.3: Use um loop while para uma tarefa de contagem.
contador = 1
while contador <= 3:
    print (f"Execução número {contador}") 
    contador = contador + 1

############################################################

#Tarefa 3.1: Crie uma função nomeada.

# Usamos 'def' para definir uma função. Ela recebe um 'argumento' 
def contar_palavras (sentenca):
    """Conta o número de palavras em uma sentença."""
    # A função processa o argumento e retorna um valor
    palavras = sentenca.split() # Converte a string em uma lista de palavras 
    return len(palavras)

#Chamar a função com um texto
sentenca_exemplo = "o rato roeu a roupa do rei de Roma"
numero_de_palavras = contar_palavras (sentenca_exemplo)
print (f"O número de palavras na frase é: {numero_de_palavras}")

############################################################

#Tarefa 3.2: Entenda as Funções Anônimas (lambda).

# Funções lambda são pequenas funções de uma linha. 
# Elas são úteis para tarefas rápidas.
multiplicar = lambda x, y: x * y
resultado = multiplicar (5, 3)

print (f"o resultado da multiplicação é: {resultado}")

############################################################


# Tarefa 3.3: Filtre palavras que começam com a letra 'a'.

texto_completo = "A análise de sentimentos é uma das áreas mais aplicadas do PLN."
# Converta o texto para minúsculas e divida em uma lista de palavras
tokens_sujos = texto_completo.lower().split()
print (f"Tokens originais: {tokens_sujos}")

# Vamos criar uma lista para guardar o resultado 
palavras_filtradas = []

# Use um loop 'for' e uma condicional 'if' para filtrar
for palavra in tokens_sujos:
    if palavra.startswith('a'):
        palavras_filtradas.append(palavra)
        
print (f"Palavras que começam com 'a': {palavras_filtradas}")

############################################################

# Tarefa 3.4: 0 Desafio Pythonico - Use a Compreensão de Listas. 
# A mesma tarefa anterior pode ser feita de forma mais elegante e 
# concisa em Python usando uma compreensão de Listas.

# Mesmo resultado, em uma única linha! 
palavras_filtradas_compreensao = [palavra for palavra in tokens_sujos if palavra.startswith('a')] 
print(f"Resultado com Compreensão de Listas: {palavras_filtradas_compreensao}")