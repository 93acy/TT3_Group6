import os

from version import VERSION


basedir = os.path.abspath(os.path.dirname(__file__))

c = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'database': 'socialmedia'
}

db_user = c.get('user')
db_pwd = c.get('password')
db_host = c.get('host')
db_port = c.get('port')
db_name = c.get('database')


class Config(object):
    APP_NAME = 'techtrek-tt3-backend'
    VERSION = VERSION
    SECRET = os.environ.get('SECRET')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/socialmedia"
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}@{db_host}:{db_port}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False