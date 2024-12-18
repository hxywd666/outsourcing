from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/login', methods=['POST'])
def login():
    return '登录'

@user_bp.route('/register', methods=['POST'])
def register():
    return '注册'