import requests


class DataFetcher:

    _DND_BASE_URL = "https://character-service.dndbeyond.com/character/v3"

    _CHARACTER_URL = f"{_DND_BASE_URL}/character/"

    def get_character(self, character_id):
        response = requests.get(self._CHARACTER_URL + str(character_id))
        return response.content
