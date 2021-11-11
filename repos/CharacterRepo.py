from models import DbCharacter

class CharacterRepo:

    def __init__(self, db):
        self.db = db

    def get_all_characters(self):
        return map(lambda x: DbCharacter(*x), self.db.fetch_multiple(f'select * from `character`'))

    def get_character_with_id(self, character_id):
        fetch_data = self.db.fetch_single(f'select * from `character` where `id` = {character_id}')
        return DbCharacter(*fetch_data)

    def get_character_with_player_id(self, player_id):
        fetch_data = self.db.fetch_single(f'select * from `character` where `id` in '
                                 f'(select `character_id` from character_player where `player_id` = {player_id})')
        return DbCharacter(*fetch_data)
