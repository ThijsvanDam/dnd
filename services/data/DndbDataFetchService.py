from typing import Text
import requests

"""
Provide functionality for actually fetching dndb data.
"""
class DndbDataFetchService:

    _DNDB_BASE_URL = "https://character-service.dndbeyond.com/character/v5"

    _DNDB_CHARACTER_URL = f"{_DNDB_BASE_URL}/character/"

    def get_character(self, character_id) -> Text:
        response = requests.get(self._DNDB_CHARACTER_URL + str(character_id))
        return response.content
