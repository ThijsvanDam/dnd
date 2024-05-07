import requests

from models.character import Character as Character
from models.health import Health
from models.player import Player
from models.saves import Saves
from models.stats import Stats
from services.data.api_model import Character as ApiCharacter
from services.data.api_model import CharacterData


class DndbDataFetchService:
    """
    Provide functionality for actually fetching dndb data.
    """

    _DNDB_BASE_URL = "https://character-service.dndbeyond.com/character"
    _DNDB_CHARACTER_DIR = "character"
    api_version = "v5"

    @classmethod
    def get_character(cls, character_id: int) -> ApiCharacter:
        url = f"{cls._DNDB_BASE_URL}/{cls.api_version}/{cls._DNDB_CHARACTER_DIR}/{character_id}"
        response = requests.get(url)

        # Dump to json for debug
        with open("response.json", "w") as f:
            f.write(response.content.decode("utf-8"))

        return CharacterData.model_validate_json(response.content).data
