import json
from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Health import Health
from models.Saves import Saves
from models.Stats import Stats

from .Base import Base

if TYPE_CHECKING:
    from .Player import Player


class Character(Base):
    """Character model with all data that is supported by the frontend."""

    __tablename__ = "character"

    # Character data
    name: Mapped[str] = mapped_column(String(30))
    level: Mapped[int]
    avatar_url: Mapped[str]
    page_url: Mapped[str]

    # User data
    dndb_id: Mapped[int]

    # Db relations
    player_id: Mapped[int] = mapped_column(ForeignKey("player.id"))
    player: Mapped["Player"] = relationship(back_populates="characters")
    stats: Mapped[List["Stats"]] = relationship(
        back_populates="character", cascade="all, delete-orphan"
    )
    health: Mapped[List["Health"]] = relationship(
        back_populates="character", cascade="all, delete-orphan"
    )
    saves: Mapped[List["Saves"]] = relationship(
        back_populates="character", cascade="all, delete-orphan"
    )

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
