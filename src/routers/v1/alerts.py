import asyncio
from datetime import datetime

from fastapi import APIRouter, BackgroundTasks, Request

from src.models.users import User
from src.utils.logging import logger

router = APIRouter()


async def monitor_slot(task_uid: int, user: User):
    while True:
        await check_slot_availability(task_uid, user)
        await asyncio.sleep(5)


async def check_slot_availability(task_uid, user):
    try:
        logger.info(f'uid_{task_uid} Checking availability for {user.name}')
        raise Exception('Some error occurred')
    except Exception as e:
        logger.exception(e)


@router.post('/')
async def set_alert(request: Request, background_tasks: BackgroundTasks,
                    user: User):
    """
    :param request:
    :param background_tasks:
    :param user:
    :return:
    """

    # task uid be epoch timestamp
    task_uid = int(datetime.now().timestamp())
    background_tasks.add_task(monitor_slot, task_uid=task_uid, user=user)

    return {'message': f'Hi {user.name}! Your request has been received'}

