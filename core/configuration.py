from misc import AbstractConfiuration

class Bot(AbstractConfiuration):
    token : str = 'Bot token here'

class Database(AbstractConfiuration):
    database : str = 'sqlite://runtime/database.db'
    timezone : str = 'UTC'

class Logging(AbstractConfiuration):
    path : str = 'runtime/log.log'

class Config(AbstractConfiuration):
    bot : Bot = Bot()
    database : Database = Database()
    logging : Logging = Logging()