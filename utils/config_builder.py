import logging, os
from pydantic import BaseModel

from typing_extensions import Self
from collections.abc import Mapping
from deepdiff import DeepDiff

from enum import Enum
import json, yaml, toml

class SaveAs(Enum):
    JSON = '.json'
    YAML = '.yaml'
    TOML = '.toml'

class Attributes:
    __path : str = None
    __save_as : SaveAs = SaveAs.JSON
    __structure : dict = {}

class ConfigStructure(BaseModel):
    def create_config(self, name : str = None, save_as : SaveAs = SaveAs.JSON, skip_updates : bool = False) -> Self: 
        if not name:
            return

        Attributes.__path = name + save_as.value
        Attributes.__save_as = save_as
        Attributes.__structure = self.dict()

        if not self.__is_config_exists():
            config = self.__overwrite(data = Attributes.__structure)
        else:
            readed_config = self.__read_config()
            structure_updated = self.__is_structure_updated(readed_config = readed_config)

            config = self.__deep_update(source = Attributes.__structure, overrides = readed_config)
            self.__overwrite(data = config)

            if structure_updated and skip_updates == False:
                logging.warn('Configuration structure updated, abort')
                os._exit(0)

        return self.__class__(**config)
    
    def overwrite(self) -> None:
        self.__overwrite(data = self.dict())

    def __overwrite(self, data : dict) -> None:
        with open(Attributes.__path, 'w', encoding = 'utf-8') as configfile:
            save_as = Attributes.__save_as

            if save_as == SaveAs.JSON:
                json.dump(data, configfile, ensure_ascii = False, indent = 4)
            elif save_as == SaveAs.YAML:
                yaml.dump(data, configfile, default_flow_style = False, allow_unicode = True)
            elif save_as == SaveAs.TOML:
                toml.dump(data, configfile)

        return data

    def __read_config(self) -> dict:
        with open(Attributes.__path, 'r', encoding = 'utf-8') as configfile:
            save_as = Attributes.__save_as

            if save_as == SaveAs.JSON:
                loads = json.load(configfile)
            elif save_as == SaveAs.YAML:
                loads = yaml.safe_load(configfile)
            elif save_as == SaveAs.TOML:
                loads = toml.load(configfile)

        return loads

    def __deep_update(self, source : dict, overrides : dict):
        for key, value in overrides.items():
            if isinstance(value, Mapping) and value:
                returned = self.__deep_update(source.get(key, {}), value)
                source[key] = returned
            else:
                source[key] = overrides[key]
        return source

    def __is_structure_updated(self, readed_config : dict) -> bool:
        deepDiff = DeepDiff(Attributes.__structure, readed_config)
        return 'dictionary_item_removed' in deepDiff

    def __is_config_exists(self) -> bool:
        try:
            self.__read_config()
            return True
        except FileNotFoundError:
            return False
        except json.JSONDecodeError:
            raise Exception(f'{Attributes.__path} decode error')
        except yaml.error.YAMLError:
            raise Exception(f'{Attributes.__path} decode error')
        except toml.TomlDecodeError:
            raise Exception(f'{Attributes.__path} decode error')