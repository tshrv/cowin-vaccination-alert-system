from .base import *
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

MIDDLEWARES += [
    HTTPSRedirectMiddleware
]
