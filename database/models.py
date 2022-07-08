from pydantic import BaseModel
from .base import connection, cursor

def create_tables():
    cursor.execute("CREATE TABLE IF NOT EXISTS `users` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user_id INTEGER UNIQUE)")

    connection.commit()

class User(BaseModel):
    id : int = 0
    user_id : int

    def exists(user_id : int) -> bool:
        cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,))
        row = cursor.fetchone()

        return row != None

    def create(user_id : int):
        if not User.exists(user_id = user_id):
            cursor.execute("INSERT INTO `users` (`user_id`) VALUES(?)", (user_id,))
            connection.commit()

            id = cursor.lastrowid
            return User(id = id, user_id = user_id)
        else:
            return User.get(user_id = user_id)

    def get(user_id : int):
        if User.exists(user_id = user_id):
            cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,))
            row = cursor.fetchone()

            return User.parse_obj(row)