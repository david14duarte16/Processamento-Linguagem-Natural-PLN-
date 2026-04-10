# 4. Desafio Final: O Desafio do E-commerce (PBL)

# Agora é a hora de aplicar tudo no seu projeto semestral. Siga os passos abaixo com o seu Squad:

# Escolha do texto: Use um texto que contenha pelo menos três frases, com símbolos, e caracteres variados.
# Implementação do Pipeline: Crie uma função chamada pipeline_limpeza que realize:
# Conversão para minúsculas.
# Remoção de tags HTML e URLs.
# Remoção de caracteres especiais (mantendo apenas o texto).
# Tokenização via NLTK.
# Relatório de Impacto: Calcule o tamanho do vocabulário (Types) antes e depois da limpeza.

#Justifique para o "cliente" quanto de "lixo" foi removido e como isso otimiza o processamento em nuvem.

############################################################

# 1. Escolha do Texto:
texto = "<p>Entrega atrasou :( Produto ok!!! Veja detalhes em https://teste.com Melhorar suporte!!!</p>"

############################################################

# 2. Implementação do Pipeline:
import re
import unicodedata
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

def pipeline_limpeza(texto):
    
    # 1. Minúsculas
    texto = texto.lower()
    
    # 2. Remover HTML
    texto = re.sub(r'<.*?>', '', texto)
    
    # 3. Remover URLs
    texto = re.sub(r'http\S+', '', texto)
    
    # 4. Remover acentos
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join([c for c in texto if unicodedata.category(c) != 'Mn'])
    
    # 5. Remover caracteres especiais
    texto = re.sub(r'[^\w\s]', '', texto)
    
    # 6. Tokenização
    tokens = word_tokenize(texto)
    
    return tokens

############################################################

# 3. Relatório de Impacto:
# Antes (texto bruto)
tokens_antes = word_tokenize(texto.lower())
types_antes = len(set(tokens_antes))

# Depois (limpo)
tokens_depois = pipeline_limpeza(texto)
types_depois = len(set(tokens_depois))

print("Tokens antes:", tokens_antes)
print("Types antes:", types_antes)

print("Tokens depois:", tokens_depois)
print("Types depois:", types_depois)

############################################################

# 4. Justificativa para o Cliente:
print("\nJustificativa para o Cliente:")
print(f"Antes da limpeza, tínhamos {types_antes} types, incluindo muitos caracteres especiais e URLs que não agregam valor para a análise.")
print(f"Após a limpeza, reduzimos para {types_depois} types, focando apenas no conteúdo relevante. Isso otimiza o processamento em nuvem, pois reduz a quantidade de dados desnecessários, economizando recursos e melhorando a eficiência dos modelos de NLP que serão aplicados posteriormente.")