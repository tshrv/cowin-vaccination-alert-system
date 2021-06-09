from datetime import datetime

from pydantic import BaseModel

from src.utils.validators import ObjectId


class SerializableBaseModel(BaseModel):
    class Config:
        use_enum_values = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
            ObjectId: str,
        }
