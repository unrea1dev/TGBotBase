from tortoise.models import Model
from tortoise.fields import IntField

class BaseModel(Model):
    id = IntField(pk = True)

    class Meta:
        abstract = True

    def __repr__(self) -> str:
        return '<{}{}>'.format(self.__class__.__name__, self.__str__())