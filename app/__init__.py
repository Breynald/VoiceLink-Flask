from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import pymysql
from dbutils.pooled_db import PooledDB
from .appconfig import Config
import time
import threading
from flask_socketio import SocketIO
import os

# dao and service
from .dal.user_dao import UserDAO
from .dal.server_dao import ServerDAO
from .services.user_service import UserService
from .services.server_service import ServerService


app = Flask(__name__)
app.config.from_object(Config)
app.static_folder = '../static'
jwt = JWTManager(app)
CORS(app, supports_credentials=True)
socketio = SocketIO(app, cors_allowed_origins='*')

pool = PooledDB(
    creator=pymysql,
    maxconnections=50,
    mincached=5,
    maxcached=10,
    maxusage=None,
    blocking=True,
    setsession=[],
    ping=1,
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB'],
    autocommit=True
)


user_dao = UserDAO(pool)
server_dao = ServerDAO(pool)
user_service = UserService(user_dao)
server_service = ServerService(server_dao)


def keep_connection():
    while True:
        conn = pool.connection()
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.close()
        conn.close()
        time.sleep(180)  

# 启动心跳线程
threading.Thread(target=keep_connection, daemon=True).start()