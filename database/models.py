from .base import BaseModel
from peewee import IntegerField

class User(BaseModel):
    user_id = IntegerField(unique = True)

    class Meta:
        db_table = 'users'

def initializator():
    User.create_table()