from dataclasses import dataclass

from .DbModel import DbModel

"""Character as how it's stored in the database.
"""
@dataclass
class DbCharacter(DbModel):
    name: str
    dndb_id: int