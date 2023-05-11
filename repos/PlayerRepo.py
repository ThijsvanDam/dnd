from db.Db import Db
from models.Player import Player


class PlayerRepo:

    def __init__(self, db: Db):
        self.db: Db = db

    def get_player_with_id(self, player_id: int) -> Player:
        fetch_data = self.db.fetch_single(f'select * from player where id = {player_id}')
        return fetch_data