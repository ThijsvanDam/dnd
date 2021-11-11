from dataclasses import dataclass
import json

from .Stats import Stats

@dataclass
class Character:
    name: str
    level: int
    avatar_url: str
    stats: Stats
    base_hp: int
    bonus_hp: int
    removed_hp: int
    temp_hp: int

    def __init__(self, name, level, avatar_url, stats, base_hp, bonus_hp, removed_hp, temp_hp):
        self.name = name
        self.level = level
        self.avatar_url = avatar_url
        self.stats = stats
        self.base_hp = base_hp
        self.bonus_hp = bonus_hp
        self.removed_hp = removed_hp
        self.temp_hp = temp_hp

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)