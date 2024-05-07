from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.character import Character
    from models.campaign import Campaign

class PlayerCampaignLink(SQLModel, table=True):
    player_id: int = Field(foreign_key="player.id", primary_key=True)
    campaign_id: int = Field(foreign_key="campaign.id", primary_key=True)


class Player(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str
    password: str
    role: str

    characters: list["Character"] = Relationship(back_populates="player")
    campaigns: list["Campaign"] = Relationship(back_populates="players", link_model=PlayerCampaignLink)