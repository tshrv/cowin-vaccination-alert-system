from typing import List

from fastapi import APIRouter, BackgroundTasks, Request

from src.models.alerts import AlertTask
from src.utils.logging import logger
from starlette import status
from src.crud.alerts import AlertTaskCRUD

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_alert(request: Request, background_tasks: BackgroundTasks,
                       alert_task: AlertTask):
    """
    create alert_task with status active
    :param request:
    :param background_tasks:
    :param alert_task:
    :return:
    """
    logger.info(f'Create Alert: {alert_task.full_name} {alert_task.email} {alert_task.phone}')
    alert_task_crud = AlertTaskCRUD()
    alert_task_crud.create(alert_task)
    return {}


@router.get('/', status_code=status.HTTP_200_OK)
async def get_alert(request: Request, background_tasks: BackgroundTasks,
                    email: str) -> List[AlertTask]:
    """
    get alerts by email
    :param request:
    :param background_tasks:
    :param email:
    :return:
    """
    logger.info(f'Get Alert: {email}')
    alert_task_crud = AlertTaskCRUD()
    alert_tasks = alert_task_crud.get(email=email)
    return alert_tasks
