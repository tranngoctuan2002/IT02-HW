import cloudinary.uploader
from flask import render_template, request, redirect
from saleapp import app, dao, admin, login
from flask_login import login_user, logout_user
from saleapp.decorators import anonymous_user
@app.route("/")
def index():
    products = dao.load_products(category_id= request.args.get('category_id'), kw=request.args.get('keyword'))
    return render_template("index.html", product = products)

@app.route("/product/<int:product_id>")
def prodcut_deltail(product_id):
    pd = dao.load_product_by_id(product_id)
    return render_template("detail.html", product=pd)

@app.route("/login-admin", methods=['post'])
def login_admin():
    username = request.form['username']
    password = request.form['password']

    user = dao.user_authetic(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')

@app.route('/login', methods=['get', 'post'])
@anonymous_user
def login_my_user():
    if request.method.__eq__("POST"):
        username = request.form['username']
        password = request.form['password']
        user = dao.user_authetic(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect('/')

    return render_template("login.html")

@app.route('/register', methods=['get', 'post'])
def register():
    err_msg = ''
    if request.method == 'POST':
        password = request.form['password']
        confirm = request.form['confirm']

        if password.__eq__(confirm):
            avatar = '...'
            if request.files:
                res = cloudinary.uploader.upload(request.files['avatar'])
                avatar = res['secure_url']

                try:
                    dao.register(name=request.form['name'],
                                 username=request.form['username'],
                                 password=password,
                                 avatar=avatar)
                    return redirect('/login')
                except:
                    err_msg = "Lỗi rồi bới làng nước ơi!!!"
        else:
            err_msg = 'Mật khẩu không khớp!!'

    return render_template('register.html', err_msg=err_msg)

@app.route('/logout')
def logout_my_user():
    logout_user()
    return redirect('/login')

@login.user_loader
def load_user(user_id):
    return dao.load_user_by_id(user_id=user_id)

@app.context_processor
def commit_attr():
    categories = dao.load_category()
    return {
        'cate': categories
    }

if __name__ == '__main__':
    app.run(debug=True)