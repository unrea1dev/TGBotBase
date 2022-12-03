from tortoise import fields
from database.base import BaseModel

class User(BaseModel):
    user_id = fields.IntField(unique = True)

    class Meta:
        table = 'users'