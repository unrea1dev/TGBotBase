from tortoise.models import Model
from tortoise.fields import IntField

class BaseModel(Model):
    id = IntField(pk = True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        values = {}
        key_values = [key for key in self.__dict__ if not key.startswith('_')]

        for key in key_values: values[key] = self.__dict__[key]
        return str(values)

    def __repr__(self) -> str:
        return '<{}{}>'.format(self.__class__.__name__, self.__str__())