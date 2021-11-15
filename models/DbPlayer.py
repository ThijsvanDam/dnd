from dataclasses import dataclass

from .DbModel import DbModel

"""Player as its stored in the database.
"""
@dataclass
class DbPlayer(DbModel):
    name: str
    password: str
    role: str
