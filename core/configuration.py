from core.tools import AbstractConfiuration

class Bot(AbstractConfiuration):
    token : str = 'Bot token here'

class Api(AbstractConfiuration):
    host : str = 'localhost'
    port : int = 8443

    bot_webhook_path : str = '/webhook/'
    bot_webhook_url : str = 'https://{host}:{port}{webhook_path}'.format(host = host, port = port, webhook_path = bot_webhook_path)

class Database(AbstractConfiuration):
    database : str = 'sqlite://runtime/database.db'
    timezone : str = 'UTC'

class Logging(AbstractConfiuration):
    path : str = 'runtime/log.log'

class Configuration(AbstractConfiuration):
    bot : Bot = Bot()
    api : Api = Api()

    database : Database = Database()
    logging : Logging = Logging()