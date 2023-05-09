from dataclasses import dataclass

from .Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey

@dataclass
class Saves(Base):
    __tablename__ = "saves"

    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))

    failCount: Mapped[int]
    successCount: Mapped[int]
    isStabilized: Mapped[bool]