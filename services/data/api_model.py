from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field


class Stat(BaseModel):
    id: int
    name: Optional[str] = Field(default=None, alias="name")
    value: Optional[int] = Field(default=None, alias="value")


class Decorations(BaseModel):
    avatar_url: HttpUrl = Field(..., alias="avatarUrl")


class Race(BaseModel):
    is_sub_race: bool = Field(..., alias="isSubRace")
    base_race_name: str = Field(..., alias="baseRaceName")
    full_name: str = Field(..., alias="fullName")
    base_name: str = Field(..., alias="baseName")


class Currencies(BaseModel):
    cp: int
    sp: int
    gp: int
    ep: int
    pp: int


class ClassDefinition(BaseModel):
    name: str
    hit_dice: int = Field(..., alias="hitDice")


class CharacterClass(BaseModel):
    level: int
    is_starting_class: bool = Field(..., alias="isStartingClass")
    hit_dice_used: int = Field(..., alias="hitDiceUsed")
    definition: ClassDefinition


class DeathSaves(BaseModel):
    fail_count: Optional[int] = Field(default=None, alias="failCount")
    success_count: Optional[int] = Field(default=None, alias="successCount")
    is_stabilized: bool = Field(..., alias="isStabilized")


class Modifier(BaseModel):
    type: str
    sub_type: str = Field(..., alias="subType")
    value: Optional[int]


class Modifiers(BaseModel):
    race: List[Modifier]
    class_: List[Modifier] = Field(..., alias="class")
    background: List[Modifier]
    item: List[Modifier]
    feat: List[Modifier]
    condition: List[Modifier]

    @property
    def all_modifiers(self) -> List[Modifier]:
        return (
            self.race
            + self.class_
            + self.background
            + self.item
            + self.feat
            + self.condition
        )

    def get_bonus_score(self, stat: str) -> int:
        return sum(
            modifier.value or 0
            for modifier in self.all_modifiers
            if modifier.sub_type == f"{stat}-score"
        )


class Character(BaseModel):
    id: int
    user_id: int = Field(..., alias="userId")
    username: str
    is_assigned_to_player: bool = Field(..., alias="isAssignedToPlayer")
    readonly_url: HttpUrl = Field(..., alias="readonlyUrl")
    decorations: Decorations
    name: str
    inspiration: bool
    base_hit_points: int = Field(..., alias="baseHitPoints")
    bonus_hit_points: Optional[int] = Field(default=None, alias="bonusHitPoints")
    override_hit_points: Optional[int] = Field(default=None, alias="overrideHitPoints")
    removed_hit_points: int = Field(..., alias="removedHitPoints")
    temporary_hit_points: int = Field(..., alias="temporaryHitPoints")
    stats: List[Stat]
    bonus_stats: List[Stat] = Field(..., alias="bonusStats")
    override_stats: List[Stat] = Field(..., alias="overrideStats")
    race: Race
    currencies: Currencies
    classes: List[CharacterClass]
    conditions: List[str]
    death_saves: DeathSaves = Field(..., alias="deathSaves")
    modifiers: Modifiers

    # TODO filter instead of hard index
    @property
    def strength(self) -> int:
        mod = self.modifiers.get_bonus_score("strength")
        return (self.stats[0].value or 0) + mod

    @property
    def dexterity(self) -> int:
        mod = self.modifiers.get_bonus_score("dexterity")
        return (self.stats[1].value or 0) + mod

    @property
    def constitution(self) -> int:
        mod = self.modifiers.get_bonus_score("constitution")
        return (self.stats[2].value or 0) + mod

    @property
    def intelligence(self) -> int:
        mod = self.modifiers.get_bonus_score("intelligence")
        return (self.stats[3].value or 0) + mod

    @property
    def wisdom(self) -> int:
        mod = self.modifiers.get_bonus_score("wisdom")
        return (self.stats[4].value or 0) + mod

    @property
    def charisma(self) -> int:
        mod = self.modifiers.get_bonus_score("charisma")
        return (self.stats[5].value or 0) + mod


class CharacterData(BaseModel):
    data: Character
