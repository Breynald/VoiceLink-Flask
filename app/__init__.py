from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import pymysql
from .appconfig import Config

# dao and service
from .dal.user_dao import UserDAO
from .dal.server_dao import ServerDAO
from .services.user_service import UserService
from .services.server_service import ServerService


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

user_dao = UserDAO(db=mysql)
server_dao = ServerDAO(db=mysql)
user_service = UserService(user_dao)
server_service = ServerService(server_dao)

