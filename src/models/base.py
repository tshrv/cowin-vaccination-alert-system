from pydantic import BaseModel


class SerializableBaseModel(BaseModel):
    class Config:
        use_enum_values = True

