import hashlib
from saleapp.models import Category, Product, User, Receipt, ReceiptDetails,Comments
from saleapp import db
from flask_login import current_user
from sqlalchemy import func


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

def count_product_by_cate():
    return db.session.query(Category.id, Category.name, func.count(Product.id))\
                            .join(Product, Product.category_id.__eq__(Category.id))\
                            .group_by(Category.id).order_by(Category.id).all()

def stats_revenue(kw=None, from_date=None, to_date=None):
    query = db.session.query(Product.id, Product.name, func.sum(ReceiptDetails.quantity*ReceiptDetails.price))\
                            .join(ReceiptDetails, ReceiptDetails.product_id.__eq__(Product.id))\
                            .join(Receipt, ReceiptDetails.receipt_id.__eq__(Receipt.id))

    if kw:
        query = query.filter(Product.name.contains(kw))

    if from_date:
        query =  query.filter(Receipt.created_date.__ge__(from_date))

    if to_date:
        query = query.filter(Receipt.created_date.__le__(to_date))

    return query.group_by(Product.id).all()

def load_comments(product_id):
    return Comments.query.filter(Comments.product_id.__eq__(product_id)).order_by(-Comments.id).all()


if __name__ == "__main__":
    from saleapp import app
    with app.app_context():
        print(stats_revenue('Galaxy'))