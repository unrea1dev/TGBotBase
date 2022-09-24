from utils import ConfigStructure

class Bot(ConfigStructure):
    token : str = 'Bot token here'

class Database(ConfigStructure):
    database : str = 'sqlite://database.db'

class Logs(ConfigStructure):
    path : str = 'log.log'

class Config(ConfigStructure):
    bot : Bot = Bot()
    database : Database = Database()
    logs : Logs = Logs()