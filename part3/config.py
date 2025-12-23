import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        "sqlite:///hbnb.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
