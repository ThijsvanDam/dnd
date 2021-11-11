

class CharacterService:

    def __init__(self, character_repo):
        self._character_repo = character_repo

    def get_all_characters(self):
        return self._character_repo.get_all_characters()

    def get_character_with_id(self, id):
        return self._character_repo.get_character_with_id(id)

    def get_character_with_player_id(self, player_id):
        return self._character_repo.get_character_with_player_id(player_id=player_id)
