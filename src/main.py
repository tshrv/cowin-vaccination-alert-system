from fastapi import APIRouter, FastAPI
from src.routers import v1


app = FastAPI(title='iCVAS')

app.include_router(
    v1.router,
    prefix='/v1',
)
