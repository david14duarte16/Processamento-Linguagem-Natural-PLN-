# 1. Escreva uma função que receba uma string e retorne uma nova string correspondente 
# à original invertida (de trás para frente). Para isso, crie um loop com while. 
# O resultado deve ser parecido com este:
# >>> inversa('abc')
# 'cba'

def inversa(texto):
    resultado = ""
    indice = len(texto) - 1
    
    while indice >= 0:
        resultado += texto[indice]
        indice -= 1
        
    return resultado

# Teste
print(inversa('abc'))  # cba

############################################################

# 2. Escreva uma função que receba uma sentença e retorne o número (inteiro) 
# de palavras que ela contém.
# >>> palavras('O rato roeu a roupa do rei de Roma')
# 9

def palavras(sentenca):
    lista_palavras = sentenca.split()
    return len(lista_palavras)

# Teste
print(palavras('O rato roeu a roupa do rei de Roma'))  # 9

############################################################

# 3. Escreva uma função que receba uma sentença e retorne uma lista das letras 
# iniciais de cada palavra em maiúsculas.
# >>> iniciais('O rato roeu a roupa do rei de Roma')
# ['O', 'R', 'R', 'A', 'R', 'D', 'R', 'D', 'R']

def iniciais(sentenca):
    lista_palavras = sentenca.split()
    resultado = []
    
    for palavra in lista_palavras:
        resultado.append(palavra[0].upper())
        
    return resultado

# Teste
print(iniciais('O rato roeu a roupa do rei de Roma'))
# ['O', 'R', 'R', 'A', 'R', 'D', 'R', 'D', 'R']

############################################################

# 4. Escreva uma função que receba uma string e retorne o conjunto das letras 
# que ela contém, ou seja, o “alfabeto” que a produziu. 
# Dica: você vai querer eliminar o espaço em branco do conjunto. 
# É mais fácil fazer isso depois de gerar o conjunto.
# >>> alfabeto('O rato roeu a roupa do rei de Roma')
# {'I', 'R', 'O', 'A', 'D', 'M', 'E', 'P', 'U', 'T'}

def alfabeto(texto):
    letras = set(texto.upper())
    
    # remover espaço em branco
    if ' ' in letras:
        letras.remove(' ')
        
    return letras

# Teste
print(alfabeto('O rato roeu a roupa do rei de Roma'))