from flask import render_template, request
from saleapp import app, dao

@app.route("/")
def index():
    categories = dao.load_json()
    products = dao.load_products(categori_id= request.args.get('category_id'))
    return render_template("index.html", cate = categories, product = products)

if __name__ == '__main__':
    app.run(debug=True)