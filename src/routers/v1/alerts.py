from fastapi import APIRouter, BackgroundTasks, Query, Request
from src.utils.logging import get_logger
import asyncio

logger = get_logger()
router = APIRouter()


async def initiate_background_task(name):
    for i in range(5):
        logger.info(f'attempt {i} | user {name}')
        await asyncio.sleep(5)


@router.get('/')
async def set_alert(request: Request, background_tasks: BackgroundTasks,
                    name: str = Query(...)):
    background_tasks.add_task(initiate_background_task, name=name)
    return {'message': f'Hi {name}! Your request has been received'}
