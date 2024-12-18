# 导入三方依赖
from flask import Flask
from flask_cors import CORS
# 导入配置类
from config import MysqlConfig
# 导入路由蓝图
from app.routes import *
# 导入数据库model
from app.models import *


def create_server():

    server = Flask(__name__)

    # 加载数据库配置
    server.config.from_object(MysqlConfig)

    # 初始化SQLAlchemy
    db.init_app(server)

    # 创建所有表
    with server.app_context():
        db.create_all()

    # 创建蓝图
    server.register_blueprint(user_bp)

    # 配置跨域
    CORS(server)

    return server