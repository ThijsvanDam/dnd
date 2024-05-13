from typing import Sequence

from sqlmodel import select

from db.database import get_session
from models.character import Character
from models.health import Health
from models.saves import Saves
from models.spell_slot import SpellSlot
from models.stats import Stats
from services.data.api_model import Character as ApiCharacter


class CharacterController:
    def __init__(self):
        self.session = get_session()

    def get_all_characters(self) -> Sequence[Character]:
        stmt = select(Character)
        return self.session.exec(stmt).all()

    def get_character_with_id(self, character_id: int) -> Character | None:
        return self.session.get(Character, character_id)

    def get_characters_with_player_id(self, player_id: int) -> Sequence[Character]:
        stmt = select(Character).where(Character.player_id == player_id)
        return self.session.exec(stmt).all()

    def create_or_update_character_from_api(
        self, character_data: ApiCharacter
    ) -> Character:
        character = self.get_character_with_id(character_data.id)

        if character is None:
            character = Character(
                id=character_data.id,
                name=character_data.name,
                level=sum(c.level for c in character_data.classes),
                avatar_url=str(character_data.decorations.avatar_url),
                page_url=str(character_data.readonly_url),
            )
            self.session.add(character)
        else:
            character.name = character_data.name
            character.level = sum(c.level for c in character_data.classes)
            character.avatar_url = str(character_data.decorations.avatar_url)
            character.page_url = str(character_data.readonly_url)

        self.session.commit()
        self.session.refresh(character)

        self.create_or_update_health_from_api(character_data)
        self.create_or_update_stats_from_api(character_data)
        self.create_or_update_saves_from_api(character_data)
        self.create_or_update_spell_slots_from_api(character_data)

        return character

    def create_or_update_health_from_api(self, character_data: ApiCharacter):
        health = self.session.get(Health, character_data.id)

        if health is None:
            health = Health(
                character_id=character_data.id,
                base_hp=character_data.base_hit_points,
                bonus_hp=character_data.bonus_hit_points or 0,
                removed_hp=character_data.removed_hit_points,
                temp_hp=character_data.temporary_hit_points,
            )
            self.session.add(health)
        else:
            health.base_hp = character_data.base_hit_points
            health.bonus_hp = character_data.bonus_hit_points or 0
            health.removed_hp = character_data.removed_hit_points
            health.temp_hp = character_data.temporary_hit_points

        self.session.commit()

    def create_or_update_stats_from_api(self, character_data: ApiCharacter):
        stats = self.session.get(Stats, character_data.id)

        if stats is None:
            stats = Stats(
                character_id=character_data.id,
                strength=character_data.strength,
                dexterity=character_data.dexterity,
                constitution=character_data.constitution,
                intelligence=character_data.intelligence,
                wisdom=character_data.wisdom,
                charisma=character_data.charisma,
            )
            self.session.add(stats)
        else:
            stats.strength = character_data.strength
            stats.dexterity = character_data.dexterity
            stats.constitution = character_data.constitution
            stats.intelligence = character_data.intelligence
            stats.wisdom = character_data.wisdom
            stats.charisma = character_data.charisma

        self.session.commit()

    def create_or_update_saves_from_api(self, character_data: ApiCharacter):
        saves = self.session.get(Saves, character_data.id)

        if saves is None:
            saves = Saves(
                character_id=character_data.id,
                fail_count=character_data.death_saves.fail_count or 0,
                success_count=character_data.death_saves.success_count or 0,
                is_stabilized=character_data.death_saves.is_stabilized,
            )
            self.session.add(saves)
        else:
            saves.fail_count = character_data.death_saves.fail_count or 0
            saves.success_count = character_data.death_saves.success_count or 0
            saves.is_stabilized = character_data.death_saves.is_stabilized

        self.session.commit()

    def create_or_update_spell_slots_from_api(self, character_data: ApiCharacter):
        existing_spell_slots = self.session.exec(
            select(SpellSlot).where(SpellSlot.character_id == character_data.id)
        ).all()
        existing_spell_slot_levels = set(
            spell_slot.level for spell_slot in existing_spell_slots
        )

        for spell_slot in character_data.spell_slots:
            if spell_slot.level in existing_spell_slot_levels:
                # Update existing spell slot
                existing_spell_slot = next(
                    (s for s in existing_spell_slots if s.level == spell_slot.level),
                    None,
                )
                if existing_spell_slot:
                    existing_spell_slot.used = spell_slot.used
                    existing_spell_slot.max = spell_slot.max
            else:
                # Create new spell slot
                self.create_spell_slot_from_api(character_data, spell_slot.level)

        self.session.commit()

    def create_spell_slot_from_api(self, character_data: ApiCharacter, level: int):
        spell_slot = next((s for s in character_data.spell_slots if s.level == level))
        self.session.add(
            SpellSlot(
                character_id=character_data.id,
                level=spell_slot.level,
                max=spell_slot.max,
                used=spell_slot.used,
            )
        )
        self.session.commit()
