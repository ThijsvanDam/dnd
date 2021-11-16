

from typing import List
from models.Character import Character
from repos.CharacterRepo import CharacterRepo


class CharacterService:

    def __init__(self, character_repo: CharacterRepo):
        self._character_repo: CharacterRepo = character_repo

    def get_all_characters(self) -> List[Character]:
        return self._character_repo.get_all_characters()

    def get_character_with_id(self, id: int) -> Character:
        return self._character_repo.get_character_with_id(id)

    def get_character_with_player_id(self, player_id: int) -> Character:
        return self._character_repo.get_character_with_player_id(player_id=player_id)
