from .auth import auth
from .views import views
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def creat_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kfhbajefoebfobsfb'
    app.config['SQLALCHEMY_DATABSE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
