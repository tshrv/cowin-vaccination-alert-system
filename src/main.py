from fastapi import FastAPI
from src.routers import v1, pages
from src import settings
from fastapi.staticfiles import StaticFiles
from src.middlewares import MiddlewareLoader

app = FastAPI(title='iCVAS')

# middlewares
middleware_loader = MiddlewareLoader(app)
middleware_loader.load()

# serve static files
app.mount(
    settings.STATIC_URL,
    StaticFiles(directory=settings.STATIC_DIR_PATH),
    name=settings.STATIC_DIR
)

app.include_router(v1.router, prefix='/v1')
app.include_router(pages.router, prefix='')
