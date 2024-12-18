"""
将数据库实例抽离出来 解决循环依赖的问题
"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()