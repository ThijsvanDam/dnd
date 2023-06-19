from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .Base import Base

if TYPE_CHECKING:
    from .Character import Character


class Saves(Base):
    __tablename__ = "saves"

    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="saves")

    failCount: Mapped[int]
    successCount: Mapped[int]
    isStabilized: Mapped[bool]
