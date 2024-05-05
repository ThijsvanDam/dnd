from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from .player import Player
    from .health import Health
    from .saves import Saves
    from .stats import Stats


class Character(SQLModel, table=True):
    """Character model with all data that is supported by the frontend."""

    id: int | None = Field(default=None, primary_key=True)

    # User data
    dndb_id: int

    # Character data
    name: str
    level: int
    avatar_url: str
    page_url: str

    # Db relations
    # player_id: int = Field(foreign_key="player.id")
    # player: "Player" = Relationship(back_populates="characters")
    health: "Health" = Relationship(
        back_populates="character",
        sa_relationship_kwargs={"cascade": "all, delete, delete-orphan"},
    )
    stats: "Stats" = Relationship(
        back_populates="character",
        sa_relationship_kwargs={"cascade": "all, delete, delete-orphan"},
    )
    saves: "Saves" = Relationship(
        back_populates="character",
        sa_relationship_kwargs={"cascade": "all, delete, delete-orphan"},
    )
