from flask import render_template, request, redirect
from saleapp import app, dao, admin, login
from flask_login import login_user
@app.route("/")
def index():
    categories = dao.load_category()
    products = dao.load_products(category_id= request.args.get('category_id'), kw=request.args.get('keyword'))
    return render_template("index.html", cate = categories, product = products)

@app.route("/product/<int:product_id>")
def prodcut_deltail(product_id):
    pd = dao.load_product_by_id(product_id)
    return render_template("detail.html", product=pd)

@app.route("/admin", methods=['post'])
def login_admin(username, password):
    username = request.form['username']
    password = request.form['password']

    user = dao.user_authetic(username=username,password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')

@login.user_loader()
def load_user(user_id):
    return dao.load_user_by_id(user_id=user_id)

if __name__ == '__main__':
    app.run(debug=True)