from typing import Text
from enum import Enum
from ..ConfigService import ConfigService
import requests

"""
Provide functionality for actually fetching dndb data.
"""
class DndbDataFetchService:

    _DNDB_BASE_URL = "https://character-service.dndbeyond.com/character"

    _DNDB_CHARACTER_DIR = f"character/"

    configService = None

    def __init__(self) -> None:
        self.configService = ConfigService()

    def get_character(self, character_id) -> Text:
        version = str(self.configService.getVersion())
        character_id = str(character_id)

        response = requests.get(f"${self._DNDB_BASE_URL}/${version}/${self._DNDB_CHARACTER_DIR}/${character_id}")
        return response.content
