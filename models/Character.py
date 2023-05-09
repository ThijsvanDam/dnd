# import json

# from dataclasses import dataclass
# from typing import List
# from .Base import Base

# from models.Stats import Stats
# from models.Health import Health
# from models.Saves import Saves

# from sqlalchemy import String
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationship

# """Character model with all data that is supported by the frontend. 
# """
# class Character(Base):
#     __tablename__ = "character"

#     # Character data
#     name: Mapped[str] = mapped_column(String(30))
#     level: Mapped[int]
#     avatar_url: Mapped[str]
#     page_url: Mapped[str]

#     # User data
#     dndb_id: Mapped[int]

    
#     # Db relations
#     player_id: Mapped[int] = mapped_column(ForeignKey("player.id"))
#     stats: Mapped[List["Stats"]] = relationship(
#         back_populates="character", cascade="all, delete-orphan"
#     )
#     health: Mapped[List["Health"]] = relationship(
#         back_populates="character", cascade="all, delete-orphan"
#     )
#     saves: Mapped[List["Saves"]] = relationship(
#         back_populates="character", cascade="all, delete-orphan"
#     )

#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, 
#             sort_keys=True, indent=4)