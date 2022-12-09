from tortoise import Tortoise
from tortoise.models import Model
from tortoise.fields import IntField

class BaseModel(Model):
    id = IntField(pk = True)

    class Meta:
        abstract = True
        ordering = 'created_at'

    def __str__(self) -> str:
        values = {}
        key_values = [key for key in self.__dict__ if not key.startswith('_')]

        for key in key_values: values[key] = self.__dict__[key]
        return str(values)

    def __repr__(self) -> str:
        return '<{}{}>'.format(self.__class__.__name__, self.__str__())


async def create_connection(url : str) -> None:
    await Tortoise.init(db_url = url, modules = {'models' : ['database.models']})
    await Tortoise.generate_schemas()

async def close_connection() -> None:
    await Tortoise.close_connections()