class CharacterRepo:

    def __init__(self, db):
        self.db = db

    def get_all_characters(self):
        return self.db.run_query(f'select * from `character`')

    def get_character_with_player_id(self, player_id):
        return self.db.run_query(f'select * from `character` where `id` in '
                                 f'(select `character_id` from character_player where `player_id` = {player_id})')
