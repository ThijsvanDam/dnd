from dataclasses import dataclass

@dataclass
class Stats:
    str: int
    dex: int
    con: int
    int: int
    wis: int
    cha: int

    def __init__(self, str, dex, con, int, wis, cha):
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
