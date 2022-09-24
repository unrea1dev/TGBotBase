from tortoise.models import Model
from tortoise import fields

class BaseModel(Model):
    id = fields.IntField(pk = True)

    def __repr__(self) -> str:
        return '<{}{}>'.format(self.__class__.__name__, self.__str__())

class User(BaseModel):
    user_id = fields.IntField(unique = True)

    class Meta:
        table = 'users'

    def __str__(self) -> str:
        return str(
            {
                'id' : self.id,
                'user_id' : self.user_id
            }
        )