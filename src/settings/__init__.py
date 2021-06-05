from decouple import config
from src.utils.environments import Environment

environment = config('ENVIRONMENT')

if environment == Environment.DEVELOPMENT.value:
    from .development import *
else:
    from .production import *
