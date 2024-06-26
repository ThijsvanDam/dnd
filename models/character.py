from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .campaign import Campaign
    from .health import Health
    from .player import Player
    from .saves import Saves
    from .spell_slot import SpellSlot
    from .stats import Stats


class Character(SQLModel, table=True):
    """Character model with all data that is supported by the frontend."""

    # Same as character ID from DnD Beyond
    id: int = Field(..., primary_key=True)

    # Character data
    name: str
    level: int
    avatar_url: str
    page_url: str

    # Db relations
    player_id: int | None = Field(default=None, foreign_key="player.id")
    player: "Player" = Relationship(back_populates="characters")

    health: "Health" = Relationship(
        back_populates="character",
        sa_relationship_kwargs={"cascade": "all, delete, delete-orphan"},
    )

    stats: "Stats" = Relationship(
        back_populates="character",
        sa_relationship_kwargs={"cascade": "all, delete, delete-orphan"},
    )

    saves: "Saves" = Relationship(
        back_populates="character",
        sa_relationship_kwargs={"cascade": "all, delete, delete-orphan"},
    )

    spell_slots: list["SpellSlot"] = Relationship(
        back_populates="character",
        sa_relationship_kwargs={"cascade": "all, delete, delete-orphan"},
    )

    campaign_id: int | None = Field(default=None, foreign_key="campaign.id")
    campaign: "Campaign" = Relationship(back_populates="characters")

    @property
    def total_spell_slots(self) -> int:
        return sum(spell_slot.max for spell_slot in self.spell_slots)