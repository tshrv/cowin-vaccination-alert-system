import enum
from src.cowin.constants import Vaccine, Dose


class AlertTaskStatus(enum.Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
