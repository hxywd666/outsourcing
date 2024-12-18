class MysqlConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/grade_manager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False