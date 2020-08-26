from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss
from flask_migrate import Migrate

app = Flask (__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)

Scss(app, static_dir='app/static', asset_dir='app/assets/scss')

from app.models import tables, forms
from app.controllers import default