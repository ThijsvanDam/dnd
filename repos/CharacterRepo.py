from typing import List

from sqlalchemy import select

from db.Db import Db
from models.Character import Character


class CharacterRepo:
    def __init__(self, db: Db):
        self.db: Db = db

    def get_all_characters(self) -> List[Character]:
        stmt = select(Character)
        return self.db.session.scalars(stmt).all()

    def get_character_with_id(self, character_id: int) -> Character | None:
        stmt = select(Character).where(Character.id == character_id)
        return self.db.session.scalars(stmt).first()

    def get_character_with_player_id(self, player_id: int) -> Character | None:
        stmt = select(Character).where(Character.player_id == player_id)
        return self.db.session.scalars(stmt).first()
