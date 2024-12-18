from app.utils import *


mysql = read_yaml()['mysql']


class MysqlConfig:
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{mysql['username']}:{mysql['password']}@{mysql['host']}/{mysql['database']}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False