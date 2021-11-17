from dataclasses import dataclass
import math
"""Statistics 
"""
@dataclass
class Stats:
    str: int
    dex: int
    con: int
    int: int
    wis: int
    cha: int
    

    def __init__(self, str: int, dex: int, con: int, int: int, wis: int, cha) -> None:
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.strMod: int = self.call_calculate_mod(self.str)
        self.dexMod: int = self.call_calculate_mod(self.dex)
        self.conMod: int = self.call_calculate_mod(self.con)
        self.intMod: int = self.call_calculate_mod(self.int)
        self.wisMod: int = self.call_calculate_mod(self.wis)
        self.chaMod: int = self.call_calculate_mod(self.cha)
    
    @staticmethod
    def calculate_mod(stat: int) -> int:
        return math.floor((stat - 10) / 2)

    def call_calculate_mod(self, stat: int) -> int:
        return self.__class__.calculate_mod(stat)