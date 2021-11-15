from dataclasses import dataclass
from abc import ABC

"""Abstract to provide database models an id.
"""
@dataclass
class DbModel(ABC):
    id: int