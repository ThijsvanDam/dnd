from pydantic import BaseModel

stats_map = {1: "str", 2: "dex", 3: "con", 4: "int", 5: "wis", 6: "cha"}


class Stats(BaseModel):
    """Statistics"""

    id: int
    value: int

    @property
    def mod(self):
        return (self.value - 10) // 2

    @property
    def name(self):
        return stats_map[self.id]
