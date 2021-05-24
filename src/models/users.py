import enum
from typing import List, Optional, Union

from pydantic import BaseModel


class Vaccine(enum.Enum):
    COVISHIELD = 'COVISHIELD'
    COVAXIN = 'COVAXIN'


class Dose(enum.Enum):
    FIRST = 'available_capacity_dose1'
    SECOND = 'available_capacity_dose2'


class User(BaseModel):
    name: str
    phone: str
    pincode: Union[List[int], int]
    min_age_limit: Optional[int]
    vaccine: Optional[Vaccine]
    dose: Optional[Dose]
