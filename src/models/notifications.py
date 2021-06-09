from datetime import datetime
from typing import Optional

from pydantic import EmailStr

from .base import SerializableBaseModel


class Notification(SerializableBaseModel):
    email: EmailStr
    message: str
    sent: Optional[bool] = False
    created_at: datetime = datetime.now()
