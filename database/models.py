from tortoise import fields
from database.base import BaseModel

class User(BaseModel):
    user_id = fields.IntField(unique = True)
    created_at = fields.DatetimeField(auto_now_add = True)

    class Meta:
        table = 'users'