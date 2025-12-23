from flask import Flask
from .config import Config
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()


def create_app(config_class=Config):
    """Application Factory"""

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init extensions
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    # Register Blueprints / Namespaces later
    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix="/api/v1")

    return app
