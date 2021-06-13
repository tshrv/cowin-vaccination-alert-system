from datetime import datetime
from typing import List, Optional, Union

from pydantic import EmailStr, Field

from src.utils.validators import ObjectId
from .base import SerializableBaseModel
from .constants import AlertStatus, Dose, Vaccine


class AlertIn(SerializableBaseModel):
    full_name: str
    email: EmailStr
    phone: str
    pin_code: Union[List[int], int]
    min_age_limit: Optional[int] = None
    vaccine: Optional[Vaccine] = None
    dose: Optional[Dose] = None


class Alert(AlertIn):
    id: ObjectId = Field(..., alias='_id')
    created_at: datetime
    status: Optional[AlertStatus] = AlertStatus.ACTIVE

