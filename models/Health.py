from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey

from .Base import Base

class Health(Base):
    __tablename__ = "health"

    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))

    base_hp: Mapped[int]
    bonus_hp: Mapped[int]
    removed_hp: Mapped[int]
    temp_hp: Mapped[int]
    total_hp: Mapped[int]