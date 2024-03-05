from flask import Flask
from flask_cors import CORS
from .appconfig import Config
from flask_jwt_extended import JWTManager
import pymysql
# import os

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)
CORS(app, supports_credentials=True)


mysql = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB'],
    autocommit=True
)
