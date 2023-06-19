from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .Base import Base

if TYPE_CHECKING:
    from .Character import Character


class Health(Base):
    __tablename__ = "health"

    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="health")

    base_hp: Mapped[int]
    bonus_hp: Mapped[int]
    removed_hp: Mapped[int]
    temp_hp: Mapped[int]
    total_hp: Mapped[int]
