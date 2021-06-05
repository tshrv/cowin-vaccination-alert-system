from typing import List, Optional, Union

from pydantic import EmailStr

from .constants import AlertTaskStatus, Dose, Vaccine
from .base import SerializableBaseModel


class AlertTask(SerializableBaseModel):
    full_name: str
    email: EmailStr
    phone: str
    pin_code: Union[List[int], int]
    min_age_limit: Optional[int]
    vaccine: Optional[Vaccine]
    dose: Optional[Dose]
    status: Optional[AlertTaskStatus] = AlertTaskStatus.ACTIVE
