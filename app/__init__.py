"""
__init__.py

Application factory. Creating the app through a function (instead of
a single global object) keeps configuration flexible and makes the
app easier to test.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import Config

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    csrf.init_app(app)

    from app.routes import main, register_error_handlers
    app.register_blueprint(main)
    register_error_handlers(app)

    with app.app_context():
        db.create_all()

    return app
