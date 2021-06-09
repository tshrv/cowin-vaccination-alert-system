from typing import List

from fastapi import APIRouter, BackgroundTasks, Request

from src.models.alerts import Alert, AlertIn
from src.utils.logging import logger
from starlette import status
from src.crud.alerts import AlertCRUD

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_alert(request: Request, background_tasks: BackgroundTasks,
                       alert: AlertIn):
    """
    create alert with status active
    :param request:
    :param background_tasks:
    :param alert:
    :return:
    """
    logger.info(f'create-alert: {alert.full_name} {alert.email} {alert.phone}')
    alert_crud = AlertCRUD()
    alert_crud.create(alert)
    return {}


@router.get('/', status_code=status.HTTP_200_OK)
async def get_alert(request: Request, background_tasks: BackgroundTasks,
                    email: str) -> List[Alert]:
    """
    get alerts by email
    :param request:
    :param background_tasks:
    :param email:
    :return:
    """
    logger.info(f'get-alert: {email}')
    alert_crud = AlertCRUD()
    alerts = alert_crud.get(email=email)
    return alerts
