import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'storage.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://filipelo_lorena:princes$linda@filipelopes.me/filipelo_site_casamento'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://filipelo_lorena:princes$linda@localhost/filipelo_site_casamento'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'um-nome-bem-seguro'
