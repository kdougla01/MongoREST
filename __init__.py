from flask import Flask
from flask_login import LoginManager
from flask_pymongo import PyMongo

# configured Flask-PyMongo connector
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"
mongo = PyMongo(app)

app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views