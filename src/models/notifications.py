from datetime import datetime
from typing import Optional

from pydantic import EmailStr

from .base import SerializableBaseModel


class NotificationIn(SerializableBaseModel):
    email: EmailStr
    phone: str
    message: str
    sent: Optional[bool] = False


class Notification(NotificationIn):
    created_at: datetime
