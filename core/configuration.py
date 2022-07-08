from utils.config_builder import AbstractConfig

class Config(AbstractConfig):
    def __init__(self) -> None:
        super().__init__(path = 'configuration.json')

        self.bot = self.Bot(config = self)
        self.database = self.Database(config = self)

    class Bot:
        def __init__(self, config : AbstractConfig) -> None:
            self.token = config.config_field(key = 'token', layer = 'bot', default = 'Bot token')

    class Database:
        def __init__(self, config : AbstractConfig) -> None:
            self.path = config.config_field(key = 'path', layer = 'database', default = 'database.db')