import json
from saleapp import app

def load_json():
    with open(f'{app.root_path}/data/categories.json', encoding='utf-8') as f:
        return json.load(f)

def load_products(categori_id = None):
    with open(f'{app.root_path}/data/products.json', encoding='utf-8') as f:
        products = json.load(f)

    if categori_id:
        products = [p for p in products if p['category_id'] == int(categori_id)]

    return products