'''
Main module for starting the dashboard application service. Imports required 
modules from Flask (including DB and auth modules), 
and sets up logging.
'''

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

# Logging when in production:
import os
import sys
from config import TMPDIR
import logging
from logging.handlers import RotatingFileHandler
#from logging import StreamHandler



if not app.debug:
    file_handler = RotatingFileHandler(os.path.join(TMPDIR, 'dashboard.log.txt'), 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    #app.logger = logging.getLogger(__name__)
    app.logger.setLevel(logging.DEBUG)
    #file_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)
    app.logger.info('Dashboard Start Up...')    

#     file_handler_debug = RotatingFileHandler(os.path.join(TMPDIR, 'dashboard-debug.log.txt'), 'a', 1 * 1024 * 1024, 10)
#     file_handler_debug.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
#     #file_handler_debug.setLevel(logging.DEBUG)
#     file_handler_debug.setLevel(logging.DEBUG)
#     app.logger.addHandler(file_handler_debug)
#     app.logger.info('Dashboard Start Up - Debugging')
else:
    pass


    
from app import views, controller
