import os
import logging


APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# /path/to/cvas/src

ROOT_DIR = os.path.dirname(APP_DIR)
# /path/to/cvas

STATIC_DIR = 'static'
STATIC_DIR_PATH = os.path.join(APP_DIR, STATIC_DIR)
STATIC_URL = '/static'

TEMPLATES_DIR_NAME = "templates"
TEMPLATES_DIR_PATH = os.path.join(APP_DIR, TEMPLATES_DIR_NAME)

LOG_FILE_NAME = 'app.log'
LOG_FILE_PATH = os.path.join(ROOT_DIR, LOG_FILE_NAME)
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(asctime)s - %(message)s'
LOG_STREAM_HANDLER_ENABLED = False

MIDDLEWARES = []

# Database
DB_CONNECTION_STRING = 'mongodb://localhost:27017'
DB_NAME = 'cvas'
