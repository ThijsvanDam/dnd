import requests

from models.beyond.Character import Character

from ..ConfigService import ConfigService


class DndbDataFetchService:
    """Provide functionality for actually fetching dndb data."""

    _DNDB_BASE_URL = "https://character-service.dndbeyond.com/character/v5/character"

    def __init__(self):
        self.configService = ConfigService()

    def get_character(self, character_id: int | str):
        response = requests.get(f"{self._DNDB_BASE_URL}/{character_id}")

        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch character with id {character_id} from dndbeyond."
            )

        return Character.parse_obj(response.json()["data"])
