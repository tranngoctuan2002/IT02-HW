import hashlib
from saleapp.models import Category, Product, User


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

def user_authetic(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()), User.password.__eq__(password)).first()

def load_user_by_id(user_id):
    return User.query.get(user_id)