from . import models
from . import base
from tortoise import Tortoise

async def create_connection(url : str) -> None:
    await Tortoise.init(db_url = url, modules = {'models' : ['database.models']})
    await Tortoise.generate_schemas()

async def close_connection() -> None:
    await Tortoise.close_connections()