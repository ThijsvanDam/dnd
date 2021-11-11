from dataclasses import dataclass

from .DbModel import DbModel

@dataclass
class DbPlayer(DbModel):
    name: str
    password: str
    role: str

    def __init__(self, id, name, password, role):
        super().__init__(id)
        self.name = name
        self.role = role
        self.password = password

