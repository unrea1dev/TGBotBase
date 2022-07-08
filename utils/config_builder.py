import json, os
from datetime import datetime

class AbstractConfig:
    NEW_LAYER_SYMBOL = '/'

    def __init__(self, path : str) -> None:
        self.path = path

        if not self.config_exists():
            self.config = {'created_in' : str(datetime.now())}
            self.save_config()

        else:
            self.config = self.load_config()

    def config_field(self, key : str, layer : str = None, default = None) -> object:
        if layer:
            layers = list(filter(None, layer.split(self.NEW_LAYER_SYMBOL)))

            config_copy = self.config

            for i in layers:
                if i not in config_copy:
                    config_copy[i] = {}
                config_copy = config_copy[i]

            if not config_copy.get(key):
                config_copy[key] = default
                self.save_config()

                return default
            else:
                return config_copy.get(key)

        else:
            if not self.config.get(key):
                self.config[key] = default
                self.save_config()

                return default
            else:
                return self.config.get(key)
                
    def save_config(self) -> None:
        with open(self.path, 'w', encoding = 'utf-8') as file:
            json.dump(self.config, file, ensure_ascii = False, indent = 4)

    def load_config(self) -> dict:
        with open(self.path, 'r', encoding = 'utf-8') as file:
            return json.load(file)

    def config_exists(self):
        if not os.path.exists(path = self.path):
            return False

        with open(self.path, 'r') as file:
            if file.read() == '':
                return False

        return True