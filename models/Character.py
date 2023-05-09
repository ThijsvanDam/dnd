from pydantic import BaseModel, Field

from .Stats import Stats
from .Class import Class
from .Saves import Saves


class Decorations(BaseModel):
    avatar_url: str = Field(alias="avatarUrl")


class Character(BaseModel):
    """Character model with all data that is supported by the frontend."""

    name: str
    page_url: str = Field(alias="readonlyUrl")
    stats: list[Stats]

    base_hp: int = Field(alias="baseHitPoints")
    bonus_hp: int | None = Field(None, alias="bonusHitPoints")
    removed_hp: int = Field(alias="removedHitPoints")
    temp_hp: int = Field(alias="temporaryHitPoints")

    saves: Saves = Field(alias="deathSaves")

    decorations: Decorations
    classes: list[Class]

    @property
    def level(self):
        return sum(c.level for c in self.classes)

    @property
    def avatar_url(self):
        return self.decorations.avatar_url

    @property
    def total_hp(self):
        return self.base_hp + (self.bonus_hp or 0) - self.removed_hp + self.temp_hp

    @property
    def strength(self):
        return self.stats[0]

    @property
    def dexterity(self):
        return self.stats[1]

    @property
    def constitution(self):
        return self.stats[2]

    @property
    def intelligence(self):
        return self.stats[3]

    @property
    def wisdom(self):
        return self.stats[4]

    @property
    def charisma(self):
        return self.stats[5]
