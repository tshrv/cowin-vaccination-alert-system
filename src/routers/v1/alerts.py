from fastapi import APIRouter, Request
from src.utils.logging import get_logger

logger = get_logger()
router = APIRouter()


@router.get('/')
async def set_alert(request: Request):
    logger.info(request)
    return {'message': 'Hello world!'}
