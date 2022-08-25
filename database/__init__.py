from . import models
from tortoise import Tortoise

async def create_connection(database : str) -> None:
    await Tortoise.init(db_url = database, modules = {'models' : ['database.models']})
    await Tortoise.generate_schemas()

async def close_connection() -> None:
    await Tortoise.close_connections()