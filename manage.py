#!/usr/bin/env python
import os

from app import create_app, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('M0VE_CONFIG_DEV_ENV') or 'default')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
