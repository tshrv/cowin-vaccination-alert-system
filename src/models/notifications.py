from datetime import datetime
from typing import Optional

from pydantic import EmailStr

from src import settings
from .base import SerializableBaseModel


class Notification(SerializableBaseModel):
    email: EmailStr
    phone: str
    message: str
    sent: Optional[bool] = False
    created_at: datetime = datetime.now(settings.TIMEZONE)
