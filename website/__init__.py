from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path 


db = SQLAlchemy()
DB_NAME = 'hospital.db'


def create_app():
    app = Flask(__name__)
    app.config["SECRET KEY"] ="gate@2022"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .models import Prescripion, Patient, Room, Medicine
    create_database(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")
    return app



def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
