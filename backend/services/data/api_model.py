from typing import Any, List, Optional
from pydantic import BaseModel, HttpUrl, Field


class Stat(BaseModel):
    id: int
    # NOTE: "Name" is available in the response, but this is never set by the API
    name: Optional[str] = Field(default=None, alias="name")
    value: Optional[int] = Field(default=None, alias="value")

    def model_post_init(self, __context: Any):
        # Set the name of the stat based on the ID
        self.name = [
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
        ][self.id - 1]


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


class SpellRules(BaseModel):
    level_cantrips_known_maxes: List[int] = Field(..., alias="levelCantripsKnownMaxes")
    level_spell_slots: List[List[int]] = Field(..., alias="levelSpellSlots")


class ClassDefinition(BaseModel):
    name: str
    hit_dice: int = Field(..., alias="hitDice")
    spell_rules: Optional[SpellRules] = Field(default=None, alias="spellRules")


class CharacterClass(BaseModel):
    level: int
    is_starting_class: bool = Field(..., alias="isStartingClass")
    hit_dice_used: int = Field(..., alias="hitDiceUsed")
    definition: ClassDefinition

    @property
    def cantrips_known_max(self) -> int:
        if self.definition.spell_rules is None:
            return 0

        return self.definition.spell_rules.level_cantrips_known_maxes[self.level]

    @property
    def spell_slots(self) -> List[int]:
        if self.definition.spell_rules is None:
            return [0] * 9

        return self.definition.spell_rules.level_spell_slots[self.level]


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


class CampaignCharacter(BaseModel):
    username: str
    character_id: int = Field(..., alias="characterId")
    character_name: str = Field(..., alias="characterName")
    is_assigned_to_player: bool = Field(..., alias="isAssigned")


class Campaign(BaseModel):
    id: int
    name: str
    description: str
    characters: List[CampaignCharacter] = Field(..., alias="characters")


class SpellSlot(BaseModel):
    level: int
    used: int
    # NOTE: "Available" is available in the response, but this is never set by the API
    available: int

    @property
    def max(self) -> int:
        return self.available + self.used


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
    # conditions: List[str] This is incorrect, API returns list[dict] with an ID for the condition
    death_saves: DeathSaves = Field(..., alias="deathSaves")
    modifiers: Modifiers
    campaign: Campaign
    spell_slots: List[SpellSlot] = Field(..., alias="spellSlots")

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

    def model_post_init(self, __context: Any):
        # Calculate the available spell slots because the API does not provide this
        for spell_slot in self.spell_slots:
            spell_slot.available = 0

            for class_ in self.classes:
                # NOTE
                # There is a bug(?) in DnD Beyond where it returns a default array of spell slots if the class doesn't have any
                # We assume if the class has no spell slots by level 2, then it's the default array and we set it to 0
                if (
                    class_.level >= 2
                    and class_.definition.spell_rules is not None
                    and sum(class_.definition.spell_rules.level_spell_slots[2]) == 0
                ):
                    continue

                spell_slot.available += class_.spell_slots[spell_slot.level - 1]


class CharacterData(BaseModel):
    data: Character
