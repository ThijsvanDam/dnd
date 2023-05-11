import math

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .Base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Character import Character


class Stats(Base):
    """Statistics"""

    __tablename__ = "stats"

    strength: Mapped[int]
    dexterity: Mapped[int]
    constitution: Mapped[int]
    intelligence: Mapped[int]
    wisdom: Mapped[int]
    charisma: Mapped[int]

    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="stats")

    def __init__(
        self,
        strength: int,
        dexterity: int,
        constitution: int,
        intelligence: int,
        wisdom: int,
        charisma: int,
    ) -> None:
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        self.strMod: int = Stats.calculate_mod(self.strength)
        self.dexMod: int = Stats.calculate_mod(self.dexterity)
        self.conMod: int = Stats.calculate_mod(self.constitution)
        self.intMod: int = Stats.calculate_mod(self.intelligence)
        self.wisMod: int = Stats.calculate_mod(self.wisdom)
        self.chaMod: int = Stats.calculate_mod(self.charisma)

    @staticmethod
    def calculate_mod(stat: int) -> int:
        return math.floor((stat - 10) / 2)
