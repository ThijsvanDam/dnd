from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .character import Character


class SpellSlot(SQLModel, table=True):
    character_id: int = Field(primary_key=True, foreign_key="character.id")
    character: "Character" = Relationship(back_populates="spell_slots")

    level: int = Field(primary_key=True)
    max: int
    used: int
