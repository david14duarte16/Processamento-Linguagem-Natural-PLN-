import json

path = r"c:\Users\paulo\.gemini\antigravity-ide\scratch\Processamento-Linguagem-Natural-PLN-\06 (Aula 9) - Semântica e Vetores\Exemplos.ipynb"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for cell in data['cells']:
    if cell['cell_type'] == 'code':
        new_source = []
        is_colab = False
        for line in cell['source']:
            if "/root/.cache/kagglehub/datasets/asadullahcreative" in line:
                new_source.append("import os\n")
                new_source.append("product_reviews = os.path.join(path, \"ecommerce-product-reviews.csv\")\n")
            elif "from google.colab import drive" in line:
                is_colab = True
                new_source.append("try:\n")
                new_source.append("    from google.colab import drive\n")
            elif is_colab and line.strip() and not line.startswith("#"):
                new_source.append("    " + line)
            elif is_colab and line.startswith("#"):
                new_source.append("    " + line)
            else:
                new_source.append(line)
        
        if is_colab:
            new_source.append("except:\n")
            new_source.append("    print('Ambiente local, pulando Colab')\n")
        
        cell['source'] = new_source

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1)
