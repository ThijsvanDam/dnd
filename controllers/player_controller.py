from sqlalchemy import select

from models.player import Player

from ..db.database import get_session


class PlayerRepo:
    def __init__(self):
        self.session = get_session()

    def get_player_with_id(self, player_id: int) -> Player | None:
        stmt = select(Player).where(Player.id == player_id)
        return self.session.scalars(stmt).first()
