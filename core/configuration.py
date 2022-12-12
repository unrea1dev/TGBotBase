from misc import AbstractConfiuration

class Bot(AbstractConfiuration):
    token : str = 'Bot token here'

class Database(AbstractConfiuration):
    database : str = 'sqlite://database.db'

class Logs(AbstractConfiuration):
    path : str = 'log.log'

class Config(AbstractConfiuration):
    bot : Bot = Bot()
    database : Database = Database()
    logs : Logs = Logs()