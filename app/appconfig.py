from datetime import timedelta
import os

class Config:
    # MySQL数据库配置
    MYSQL_HOST = '39.100.181.101'
    MYSQL_USER = 'breynald'
    MYSQL_PASSWORD = 'Qwerdf1314...'
    MYSQL_DB = 'VoiceLink'

    #others
    SECRET_KEY = 'breynald'
    JWT_SECRET_KEY = 'breynald'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
