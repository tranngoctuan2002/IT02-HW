import cloudinary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
from flask_babelex import Babel

app = Flask(__name__)
app.secret_key = "Nhatquynhimathubahoctro"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/it02sqlalchemy?charset=utf8mb4" % quote("Admin@123")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['CART_KEY'] = 'cart'
cloudinary.config(cloud_name='de0pt2lzw', api_key='269448242686499',api_secret='36ckrJAaSBk2wrWeU3kU9ICwTOM')

db = SQLAlchemy(app=app)

login = LoginManager(app=app)

babel = Babel(app=app)

@babel.localeselector
def get_locale():
    return 'vi'
