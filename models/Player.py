
from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# from models.Character import Character

from .Base import Base

class Player(Base):
  __tablename__ = "player"

  # characters: Mapped[List["Character"]] = relationship(
  #   back_populates="player", cascade="all, delete-orphan"
  # )

  name: Mapped[str]
  password: Mapped[str]
  role: Mapped[str]