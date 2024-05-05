import requests

from models.saves import Saves
from models.stats import Stats
from models.health import Health
from services.data.api_model import CharacterData, Character as ApiCharacter
from models.character import Character as Character


class DndbDataFetchService:
    """
    Provide functionality for actually fetching dndb data.
    """

    _DNDB_BASE_URL = "https://character-service.dndbeyond.com/character"
    _DNDB_CHARACTER_DIR = "character"
    api_version = "v5"

    @classmethod
    def get_character(cls, character_id: str) -> ApiCharacter:
        url = f"{cls._DNDB_BASE_URL}/{cls.api_version}/{cls._DNDB_CHARACTER_DIR}/{character_id}"
        response = requests.get(url)

        # Dump to json for debug
        with open("response.json", "w") as f:
            f.write(response.content.decode("utf-8"))

        return CharacterData.model_validate_json(response.content).data

    @staticmethod
    def calculate_total_hp(character_data: ApiCharacter) -> int:
        return (
            character_data.base_hit_points
            + (character_data.bonus_hit_points or 0)
            - character_data.removed_hit_points
            + character_data.temporary_hit_points
        )