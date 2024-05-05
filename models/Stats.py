import math
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .character import Character


class Stats(SQLModel, table=True):
    """Statistics"""

    id: int | None = Field(default=None, primary_key=True)

    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    character_id: int = Field(foreign_key="character.id")
    character: "Character" = Relationship(back_populates="stats")

    @staticmethod
    def calculate_mod(stat: int) -> int:
        return math.floor((stat - 10) / 2)

    @property
    def strength_mod(self) -> int:
        return self.calculate_mod(self.strength)

    @property
    def dexterity_mod(self) -> int:
        return self.calculate_mod(self.dexterity)

    @property
    def consitution_mod(self) -> int:
        return self.calculate_mod(self.constitution)

    @property
    def intelligence_mod(self) -> int:
        return self.calculate_mod(self.intelligence)

    @property
    def wisdom_mod(self) -> int:
        return self.calculate_mod(self.wisdom)

    @property
    def charisma_mod(self) -> int:
        return self.calculate_mod(self.charisma)
