from typing_extensions import Self
from pydantic import BaseModel
import json
from collections.abc import Mapping

class Attributes:
    __path : str = None
    __structure : dict = {}

class ConfigStructure(BaseModel):
    def initialize_config(self, path : str = None) -> Self: 
        if not path:
            return

        Attributes.__path = path
        Attributes.__structure = self.dict()

        if not self.__config_exists():
            config = self.__overwrite(data = Attributes.__structure)
        else:
            config = self.__read_config()
            config = self.__deep_update(source = Attributes.__structure, overrides = config)

            self.overwrite(data = config)

        return self.__class__(**config)
    
    def overwrite(self) -> None:
        with open(Attributes.__path, 'w', encoding = 'utf-8') as configfile:
            json.dump(self.dict(), configfile, ensure_ascii = False, indent = 4)

    def __overwrite(self, data : dict) -> None:
        with open(Attributes.__path, 'w', encoding = 'utf-8') as configfile:
            json.dump(data, configfile, ensure_ascii = False, indent = 4)

        return data

    def __read_config(self) -> dict:
            with open(Attributes.__path, 'r', encoding = 'utf-8') as configfile:
                loads = json.load(configfile)
                return loads

    def __deep_update(self, source : dict, overrides : dict):
        for key, value in overrides.items():
            if isinstance(value, Mapping) and value:
                returned = self.__deep_update(source.get(key, {}), value)
                source[key] = returned
            else:
                source[key] = overrides[key]
        return source

    def __config_exists(self, ) -> bool:
        try:
            self.__read_config()
            return True
        except FileNotFoundError:
            return False
        except json.JSONDecodeError:
            raise Exception(f'{Attributes.__path} decode error')