from flask import render_template, request
from saleapp import app, dao

@app.route("/")
def index():
    categories = dao.load_category()
    products = dao.load_products(category_id= request.args.get('category_id'), kw=request.args.get('keyword'))
    return render_template("index.html", cate = categories, product = products)

@app.route("/product/<int:product_id>")
def prodcut_deltail(product_id):
    pd = dao.load_product_by_id(product_id)
    return render_template("detail.html", product=pd)

if __name__ == '__main__':
    app.run(debug=True)