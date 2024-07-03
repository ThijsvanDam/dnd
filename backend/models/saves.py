from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .character import Character


class Saves(SQLModel, table=True):
    character_id: int = Field(foreign_key="character.id", primary_key=True)
    character: "Character" = Relationship(back_populates="saves")

    fail_count: int
    success_count: int
    is_stabilized: bool
