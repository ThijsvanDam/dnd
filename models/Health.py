from dataclasses import dataclass

@dataclass
class Health:
    base_hp: int
    bonus_hp: int
    removed_hp: int
    temp_hp: int
    total_hp: int