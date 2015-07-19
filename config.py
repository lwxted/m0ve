class Config(object):
  pass

class DevelopmentConfig(config):
  MYSQL_SERVER = 'localhost:8889'
  MYSQL_USERNAME = 'root'
  MYSQL_DB = 'm0ve'
  SQLALCHEMY_DATABASE_URI =\
    'mysql://' + MYSQL_USERNAME + '@' + MYSQL_SERVER + '/' + MYSQL_DB +\
    '?charset=utf8
  DEBUG = True
  SECRET_KEY = 'insanely_secret_key'

class ProductionConfig(Config):
  MYSQL_SERVER = 'localhost'
  MYSQL_USERNAME = 'root'
  MYSQL_PASSWORD = 'lwxted1204'
  MYSQL_DB = 'm0ve'
  SQLALCHEMY_DATABASE_URI =\
    'mysql://' + MYSQL_USERNAME + ':' + MYSQL_PASSWORD + '@' + MYSQL_SERVER +\
    '/' + MYSQL_DB + '?charset=utf8'
  SECRET_KEY = 'insanely_secret_key'

config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig,
  'default': DevelopmentConfig
}
