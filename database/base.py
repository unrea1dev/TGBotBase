from peewee import SqliteDatabase, Model, PrimaryKeyField
from core import config

database = SqliteDatabase(database = config.database.database)

class BaseModel(Model):
    id = PrimaryKeyField(unique = True)

    class Meta:
        database = database
        order_by = 'id' 