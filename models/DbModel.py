from dataclasses import dataclass

@dataclass
class DbModel:
    id: int

    def __init__(self, id):
        self.id = id
