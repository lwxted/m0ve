from config import config
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
  # Initialize with config
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)

  # Initialize db
  db.init_app(app)

  # Jinja setups
  app.jinja_env.trim_blocks = True
  app.jinja_env.lstrip_blocks = True

  @app.route('/design/typography')
  def design_typography():
    return render_template('design/typography.html')

  @app.route('/design/article_view')
  def design_article_view():
    return render_template('design/article_view.html')

  return app
