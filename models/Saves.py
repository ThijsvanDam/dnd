from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .character import Character


class Saves(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    character_id: int = Field(foreign_key="character.id")
    character: "Character" = Relationship(back_populates="saves")

    fail_count: int
    succes_count: int
    is_stabilized: bool
