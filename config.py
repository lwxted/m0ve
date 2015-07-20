#!/usr/bin/env python
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  @classmethod
  def init_app(cls, app):
    pass

class DevelopmentConfig(Config):
  MYSQL_SERVER = 'localhost:8889'
  MYSQL_USERNAME = 'root'
  MYSQL_DB = 'm0ve'
  SQLALCHEMY_DATABASE_URI =\
    'mysql://' + MYSQL_USERNAME + '@' + MYSQL_SERVER + '/' + MYSQL_DB +\
    '?charset=utf8'
  DEBUG = True
  SECRET_KEY = 'insanely_secret_key'

  @classmethod
  def init_app(cls, app):
    # Setup logging
    import logging
    from logging.handlers import RotatingFileHandler
    log_dir = os.path.join(basedir, 'log')
    if not os.path.exists(log_dir):
      os.makedirs(log_dir)
    file_handler = RotatingFileHandler(\
      os.path.join(log_dir, 'error.log'),\
      maxBytes=1024 * 1024 * 100,\
      backupCount=20\
    )
    formatter = logging.Formatter(\
      '%(asctime)s - %(name)s - %(levelname)s - %(message)s'\
    )
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)


class ProductionConfig(Config):
  MYSQL_SERVER = 'localhost'
  MYSQL_USERNAME = 'root'
  MYSQL_PASSWORD = 'lwxted1204'
  MYSQL_DB = 'm0ve'
  SQLALCHEMY_DATABASE_URI =\
    'mysql://' + MYSQL_USERNAME + ':' + MYSQL_PASSWORD + '@' + MYSQL_SERVER +\
    '/' + MYSQL_DB + '?charset=utf8'
  SECRET_KEY = 'insanely_secret_key'

  @classmethod
  def init_app(cls, app):
    # Setup logging
    import logging
    from logging.handlers import RotatingFileHandler
    log_dir = os.path.join(basedir, 'log')
    if not os.path.exists(log_dir):
      os.makedirs(log_dir)
    file_handler = RotatingFileHandler(\
      os.path.join(log_dir, 'error.log'),\
      maxBytes=1024 * 1024 * 100,\
      backupCount=20\
    )
    formatter = logging.Formatter(\
      '%(asctime)s - %(name)s - %(levelname)s - %(message)s'\
    )
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig,
  'default': DevelopmentConfig
}
