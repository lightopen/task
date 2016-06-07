from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.bootstrap import Bootstrap
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    bootstrap.init_app(app)

    # blueprint
    from .homepage import homepage
    app.register_blueprint(homepage)
    from .upload import upload
    app.register_blueprint(upload, url_prefix='/upload')
    from .spider import spider
    app.register_blueprint(spider, url_prefix="/spider" )

    return app