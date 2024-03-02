from flask import Flask
from flask_session import Session
from flask_cors import CORS
from .appconfig import Config
import pymysql
# import os

app = Flask(__name__)
app.config.from_object(Config)

Session(app)
CORS(app)


mysql = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB'],
    autocommit=True
)
