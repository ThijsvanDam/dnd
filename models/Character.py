from dataclasses import dataclass
import json

from .Stats import Stats

"""Character model with all data that is supported by the frontend. 
"""
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
    page_url: str

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)