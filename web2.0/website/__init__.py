from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_login import LoginManager
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    #EBNCRYPT_KEY FOR THE APP
    app.config['SECRET_KEY'] = 'adjadihadsiaisdoad'
    load_dotenv()
    app.config["MYSQL_HOST"] = os.getenv('MYSQL_HOST')
    app.config["MYSQL_USER"] = os.getenv('MYSQL_USER')
    app.config["MYSQL_PASSWORD"] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + os.getenv('MYSQL_USER') + ':' + os.getenv('MYSQL_PASSWORD') + '@' + os.getenv('MYSQL_HOST') + '/' + os.getenv('MYSQL_DB')
    
    db.init_app(app)
    #import blueprints
    from .views import views
    from .auth import auth

    #REGISTER BLUEPRINTS
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)
    #telling flask how to load a user
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    with app.app_context():
        if not os.path.exists('website/' + os.getenv('MYSQL_DB') + '.db'):
            db.create_all()
            print('Created Database!')
            db.session.commit()
        else:
            print('Database already exists!')