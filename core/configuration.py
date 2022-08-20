from utils.config_builder import ConfigStructure

class Bot(ConfigStructure):
    token : str = 'Bot token here'

class Database(ConfigStructure):
    database : str = 'database.db'

class Config(ConfigStructure):
    bot : Bot = Bot()
    database : Database = Database()