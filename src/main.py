from fastapi import FastAPI

from src.jobs.scheduler import bootstrap_schedulers
from src.routers import v1, pages
from src import settings
from fastapi.staticfiles import StaticFiles
from src.middlewares import MiddlewareLoader
from src.utils.logging import logger

app = FastAPI(
    title='CVAS',
    description="This is a hobby project, Cowin Vaccination Alerts System, with auto docs for the API and everything",
    version="0.1.0",
)

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


@app.on_event('startup')
async def app_startup():
    logger.info('app_startup triggered')
    await bootstrap_schedulers()

#
# @app.on_event('shutdown')
# async def app_shutdown():
#     """
#     perform closing tasks and then gracefully stop the execution
#     :return:
#     """
#     logger.info('app_shutdown triggered')
