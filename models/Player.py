from dataclasses import dataclass


@dataclass
class Player:
    name: str
    password: str
    role: str

    def __init__(self, name, password, role):
        self.name = name
        self.role = role
        self.password = password

