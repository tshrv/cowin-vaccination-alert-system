from fastapi import APIRouter
from .home import router as home_router


router = APIRouter()

router.include_router(home_router, prefix='', tags=['Home'])
