from db.Db import Db
from models.Player import Player
from sqlalchemy import select


class PlayerRepo:
    def __init__(self, db: Db):
        self.db: Db = db

    def get_player_with_id(self, player_id: int) -> Player | None:
        stmt = select(Player).where(Player.id == player_id)
        return self.db.session.scalars(stmt).first()
