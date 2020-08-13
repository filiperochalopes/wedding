from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
        },
        'file': {
            'class' : 'logging.handlers.RotatingFileHandler',
            'formatter': 'precise',
            'filename': 'app.log',
            'maxBytes': 1024,
            'backupCount': 3,
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask (__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app.models import tables, forms
from app.controllers import default