import logging, os
from pydantic import BaseModel

from collections.abc import Mapping
from deepdiff import DeepDiff

from enum import Enum
import json, yaml, toml

class SaveAs(Enum):
    JSON = '.json'
    YAML = '.yaml'
    TOML = '.toml'

class Attributes:
    _path : str = None
    _save_as : SaveAs = SaveAs.JSON
    _schema : dict = {}

    @classmethod
    def create(cls, path : str, save_as : SaveAs, schema : dict) -> None:
        Attributes._path = path
        Attributes._save_as = save_as
        Attributes._schema = schema

class AbstractConfiuration(BaseModel):
    def create_config(self, name : str, save_as : SaveAs = SaveAs.JSON, skip_updates : bool = False): 
        Attributes.create(path = name + save_as.value, save_as = save_as, schema = self.model_dump())

        if not self._is_config_exists():
            config = self._overwrite(data = Attributes._schema)
            self._schema_updated_abort()
        else:
            readed_config = self._read_config()
            structure_updated = self._is_schema_updated(readed_config = readed_config)

            config = self._deep_update(source = Attributes._schema, overrides = readed_config)
            self._overwrite(data = config)

            if structure_updated and skip_updates == False:
                self._schema_updated_abort()

        config = self.__class__(**config)
        self.__dict__.update(config)
    
    def overwrite(self) -> None:
        self._overwrite(data = self.model_dump())

    def _overwrite(self, data : dict) -> None:
        with open(Attributes._path, 'w', encoding = 'utf-8') as configfile:
            save_as = Attributes._save_as

            if save_as == SaveAs.JSON:
                json.dump(data, configfile, ensure_ascii = False, indent = 4)
            elif save_as == SaveAs.YAML:
                yaml.dump(data, configfile, default_flow_style = False, allow_unicode = True)
            elif save_as == SaveAs.TOML:
                toml.dump(data, configfile)

        return data

    def _read_config(self) -> dict:
        with open(Attributes._path, 'r', encoding = 'utf-8') as configfile:
            save_as = Attributes._save_as

            if save_as == SaveAs.JSON:
                loads = json.load(configfile)
            elif save_as == SaveAs.YAML:
                loads = yaml.safe_load(configfile)
            elif save_as == SaveAs.TOML:
                loads = toml.load(configfile)

        return loads

    def _deep_update(self, source : dict, overrides : dict):
        source = source.copy()
        for key, value in overrides.items():
            if isinstance(value, Mapping) and value:
                returned = self._deep_update(source.get(key, {}), value)
                source[key] = returned
            else:
                source[key] = overrides[key]
        return source

    def _is_schema_updated(self, readed_config : dict) -> bool:
        deepDiff = DeepDiff(Attributes._schema, readed_config)
        return 'dictionary_item_removed' in deepDiff

    def _schema_updated_abort(self) -> None:
            logging.warn('{} schema updated, abort'.format(Attributes._path))
            os._exit(0)

    def _is_config_exists(self) -> bool:
        try:
            self._read_config()
            return True
        except FileNotFoundError:
            return False
        except (json.JSONDecodeError, yaml.error.YAMLError, toml.TomlDecodeError):
            raise Exception('{} decode error'.format(Attributes._path))