from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk = True)
    user_id = fields.IntField(unique = True)

    class Meta:
        table = 'users'

    def __str__(self) -> str:
        return str(self.__dict__)