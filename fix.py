import json

path = r"c:\Users\paulo\.gemini\antigravity-ide\scratch\Processamento-Linguagem-Natural-PLN-\06 (Aula 9) - Semântica e Vetores\Exemplos.ipynb"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for cell in data['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        
        if "/root/.cache" in source:
            source = source.replace(
                r'product_reviews = r"/root/.cache/kagglehub/datasets/asadullahcreative/e-commerce-product-reviews/versions/1/ecommerce-product-reviews.csv"',
                'import os\n    product_reviews = os.path.join(path, "ecommerce-product-reviews.csv")'
            )
            
        if "from google.colab" in source:
            source = """try:
    from google.colab import drive
    drive.mount('/content/drive')
    from gensim.models import KeyedVectors
    glove_path = '/content/drive/MyDrive/FATEC/[2025.2][6] PLN/2 Atividades/glove.2024.wikigiga.50d.txt'
    glove_model = KeyedVectors.load_word2vec_format(glove_path, binary=False, no_header=True)
    similaridade = glove_model.similarity('king', 'queen')
    print("Similaridade entre 'king' e 'queen': ", similaridade)
    palavras_proximas = glove_model.most_similar('king')
    print("Palavras próximas de 'king': ", palavras_proximas)
except ModuleNotFoundError:
    print("Ambiente Colab não detectado. Pulando execução deste bloco.")
"""
        
        # split back to list of lines keeping \n
        lines = [line + '\n' for line in source.split('\n')]
        # remove last \n if original source didn't have it at the end (split adds an empty string)
        if lines:
            lines[-1] = lines[-1].replace('\n', '')
            if not lines[-1]:
                lines.pop()
        
        cell['source'] = lines

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1)
