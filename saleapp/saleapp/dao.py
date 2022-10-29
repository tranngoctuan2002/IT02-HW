from saleapp.models import Category, Product

def load_category():
    return Category.query.all()

def load_products(category_id = None, kw = None):
    query = Product.query.filter(Product.active)

    if category_id:
        query = query.filter(Product.category_id.__eq__(category_id))
    if kw:
        query = query.filter(Product.name.contains(kw))

    return query.all()

def load_product_by_id(prodcut_id = None):
    return Product.query.get(prodcut_id)