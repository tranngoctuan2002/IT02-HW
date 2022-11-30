import hashlib
from saleapp.models import Category, Product, User, Receipt, ReceiptDetails
from saleapp import db
from flask_login import current_user


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

def register(name, username, password, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name,username=username,password=password,avatar=avatar)
    db.session.add(u)
    db.session.commit()

def save_receipt(cart):
    if cart:
        r = Receipt(user=current_user)
        db.session.add(r)

        for c in cart.values():
            d = ReceiptDetails(quantity=c['quantity'], price=c['price'], receipt=r, product_id=c['id'])
            db.session.add(d)

        try:
            db.session.commit()
        except:
            return False
        else:
            return True
