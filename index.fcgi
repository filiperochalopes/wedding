#!/home1/filipelo/.venv-filipeelore.love/bin/python

import sys
sys.path.insert(0, "/home1/filipelo/filipeelore.love")

from flup.server.fcgi import WSGIServer
from app import app

class ScriptNameStripper(object):
   def __init__(self, app):
       self.app = app

   def __call__(self, environ, start_response):
       environ['SCRIPT_NAME'] = ''
       return self.app(environ, start_response)

app = ScriptNameStripper(app)

# https://flask.palletsprojects.com/en/1.1.x/deploying/fastcgi/
# os.environ['DJANGO_SETTINGS_MODULE'] = "mydjango.settings"
# WSGIServer(get_wsgi_application()).run()

if __name__ == '__main__':
    WSGIServer(app).run()