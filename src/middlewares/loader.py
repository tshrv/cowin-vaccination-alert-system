from src import settings
from fastapi import FastAPI
from src.utils.logging import logger


class MiddlewareLoader:
    def __init__(self, app: FastAPI):
        self.middlewares = settings.MIDDLEWARES
        self.app = app

    def load(self):
        for middleware in self.middlewares:
            try:
                self.app.add_middleware(middleware)
                logger.debug(f'{middleware} loaded successfully')
            except Exception as e:
                logger.critical(f'{middleware} loading failed : {e}')
