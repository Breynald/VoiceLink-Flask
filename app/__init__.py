from flask import Flask
from flask_cors import CORS
from .mysqlconfig import Config
import pymysql

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

mysql = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB'],
    autocommit=True
)


# other config...
# app.config['SECRET_KEY'] = 'voicelinkflask'
