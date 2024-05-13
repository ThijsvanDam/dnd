from sqlmodel import Relationship, SQLModel, Field

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .character import Character


class Health(SQLModel, table=True):
    character_id: int = Field(foreign_key="character.id", primary_key=True)
    character: "Character" = Relationship(back_populates="health")

    base_hp: int
    bonus_hp: int
    removed_hp: int
    temp_hp: int

    @property
    def total_hp(self) -> int:
        return self.base_hp + self.bonus_hp + self.temp_hp

    @property
    def current_hp(self) -> int:
        return self.total_hp - self.removed_hp
