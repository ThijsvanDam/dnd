from sqlmodel import Relationship, SQLModel, Field

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .character import Character


class Health(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    base_hp: int
    bonus_hp: int
    removed_hp: int
    temp_hp: int

    character_id: int = Field(foreign_key="character.id")
    character: "Character" = Relationship(back_populates="health")

    @property
    def total_hp(self) -> int:
        return self.base_hp + self.bonus_hp - self.removed_hp + self.temp_hp