from dataclasses import dataclass
import json

from models import Saves, Stats, Health

"""Character model with all data that is supported by the frontend. 
"""
@dataclass
class Character:
    name: str
    level: int
    avatar_url: str
    page_url: str
    stats: Stats
    health: Health
    saves: Saves

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)