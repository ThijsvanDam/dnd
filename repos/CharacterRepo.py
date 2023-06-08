from db.Db import Db
from models.Character import Character
from typing import List

class CharacterRepo:

    def __init__(self, db: Db):
        self.db: Db = db

    def get_all_characters(self) -> List[Character]:
        # return [None]
        return map(lambda x: Character(*x), self.db.fetch_multiple(f'select * from `character`'))

    # def get_character_with_id(self, character_id: int) -> Character:
    #     return None
    #     # fetch_data = self.db.fetch_single(f'select * from `character` where `id` = {character_id}')
    #     # return Character(*fetch_data)

    # def get_character_with_player_id(self, player_id: int) -> Character:
    #     return None
    #     # fetch_data = self.db.fetch_single(f'select * from `character` where `id` in '
    #     #                          f'(select `character_id` from character_player where `player_id` = {player_id})')
    #     # return Character(*fetch_data)
