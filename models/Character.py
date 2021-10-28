from dataclasses import dataclass


@dataclass
class Character:
    name: str
    dndb_id: int

    def __init__(self, name, dndb_id):
        self.name = name
        self.dndb_id = dndb_id


