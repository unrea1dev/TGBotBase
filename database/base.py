import sqlite3
from pydantic import BaseModel as PydancitBaseModel

from core import config


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect(config.database.path, check_same_thread = False)
connection.row_factory = dict_factory
cursor = connection.cursor()

class BaseModel(PydancitBaseModel):
    id : int
    
    def create(self):
        raise NotImplementedError()

    def get(self):
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()
