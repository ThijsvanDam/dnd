from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .character import Character


class Campaign(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    dndb_id: int

    name: str
    description: str
    page_url: str

    characters: list["Character"] = Relationship(
        back_populates="campaign",
        sa_relationship_kwargs={"cascade": "all, delete, delete-orphan"},
    )
