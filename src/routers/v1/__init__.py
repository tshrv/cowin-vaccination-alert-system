from .alerts import router as alert_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(router=alert_router, prefix='/alerts', tags=['Alerts'])
