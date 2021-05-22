import os


APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(APP_DIR)

STATIC_DIR = 'static'
STATIC_DIR_PATH = os.path.join(APP_DIR, STATIC_DIR)
STATIC_URL = '/static'

TEMPLATES_DIR_NAME = "templates"
TEMPLATES_DIR_PATH = os.path.join(APP_DIR, TEMPLATES_DIR_NAME)
