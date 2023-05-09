from dataclasses import dataclass
from .Base import Base
import math
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


"""Statistics 
"""
class Stats(Base):
    __tablename__ = "stats"

    str: Mapped[int]
    dex: Mapped[int]
    con: Mapped[int]
    int: Mapped[int]
    wis: Mapped[int]
    cha: Mapped[int]

    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    

    def __init__(self, str: int, dex: int, con: int, int: int, wis: int, cha: int) -> None:
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.strMod: int = Stats.calculate_mod(self.str)
        self.dexMod: int = Stats.calculate_mod(self.dex)
        self.conMod: int = Stats.calculate_mod(self.con)
        self.intMod: int = Stats.calculate_mod(self.int)
        self.wisMod: int = Stats.calculate_mod(self.wis)
        self.chaMod: int = Stats.calculate_mod(self.cha)
    
    @staticmethod
    def calculate_mod(stat: int) -> int:
        return math.floor((stat - 10) / 2)