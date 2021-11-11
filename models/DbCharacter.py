from dataclasses import dataclass

from .DbModel import DbModel

@dataclass
class DbCharacter(DbModel):
    name: str
    dndb_id: int

    def __init__(self, id, name, dndb_id):
        super().__init__(id)
        self.name = name
        self.dndb_id = dndb_id


