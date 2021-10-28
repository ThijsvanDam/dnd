import requests


class DataFetcher:

    DND_BASE_URL = "https://character-service.dndbeyond.com/character/v3"

    CHARACTER_URL = f"{DND_BASE_URL}/character/"

    def get_character(self, character_id):
        response = requests.get(self.CHARACTER_URL + character_id)
        return response
