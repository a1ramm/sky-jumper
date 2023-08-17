import os
import random
import string
from datetime import timedelta

path = os.path.dirname(f"{os.path.abspath(__file__)}")
db_file = os.path.join(f"{path}/app/db", "database.db")

DEBUG = True
JWT_SECRET_KEY = "secret"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)

SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_file}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_FOLDER = f"{os.getcwd()}/upload"