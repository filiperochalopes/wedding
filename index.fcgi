#!/usr/bin/scl enable python35 -- /home1/filipelo/.venv-filipeelore.love

import os, sys
from flup.server.fcgi import WSGIServer
from app import app

sys.path.insert(0, "/home1/filipelo/filipeelore.love")
# os.environ['DJANGO_SETTINGS_MODULE'] = "mydjango.settings"

# WSGIServer(get_wsgi_application()).run()
if __name__ == '__main__':
    WSGIServer(app).run()