from bson import ObjectId as BSON_ObjectId
from bson.errors import InvalidId


class ObjectId(BSON_ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(ObjectId(v)):
            raise InvalidId(f'Invalid object id, expected type ObjectId but received type {type(v)}({v})')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')
