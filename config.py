import os
from dotenv import load_dotenv

load_dotenv()

class Config:
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = "postgresql://flaskuser:flaskuser1234@db:5432/flask_jwt_db"
=======
    SQLALCHEMY_DATABASE_URI = "postgresql://poridhi:poridhi1234@db:5432/flask_jwt_db"
>>>>>>> b4c068ab1ec9864399f65ed7d5c8f3135b78a87a
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "supersecretkey"
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']
