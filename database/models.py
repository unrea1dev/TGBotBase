
from .base import connection, cursor
from .base import BaseModel

def create_tables():
    cursor.execute("CREATE TABLE IF NOT EXISTS `users` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user_id INTEGER UNIQUE)")

    connection.commit()

class User(BaseModel):
    id : int = 0
    user_id : int

    def __str__(self) -> str:
        return str(self.__dict__)

    def create(self):
        cursor.execute("INSERT INTO `users` (`user_id`) VALUES(?)", (self.user_id,))
        connection.commit()

        self.id = cursor.lastrowid

    def get(user_id : int):
        cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,))
        row = cursor.fetchone()

        if row == None:
            return None

        return User.parse_obj(row)
