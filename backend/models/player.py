from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.character import Character


class Player(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str
    password: str
    role: str

    characters: list["Character"] = Relationship(back_populates="player")
