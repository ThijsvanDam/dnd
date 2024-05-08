from typing import Sequence

from sqlmodel import select

from db.database import get_session
from models.character import Character
from models.health import Health
from models.saves import Saves
from models.stats import Stats
from services.data.api_model import Character as ApiCharacter


class CharacterController:
    def __init__(self):
        self.session = get_session()

    def get_all_characters(self) -> Sequence[Character]:
        stmt = select(Character)
        return self.session.exec(stmt).all()

    def get_character_with_id(self, character_id: int) -> Character | None:
        stmt = select(Character).where(Character.id == character_id)
        return self.session.exec(stmt).first()

    def get_character_with_dndb_id(self, dndb_id: int) -> Character | None:
        stmt = select(Character).where(Character.dndb_id == dndb_id)
        return self.session.exec(stmt).first()

    def get_characters_with_player_id(self, player_id: int) -> Sequence[Character]:
        stmt = select(Character).where(Character.player_id == player_id)
        return self.session.exec(stmt).all()

    def create_character_from_api(self, character_data: ApiCharacter) -> Character:
        character = Character(
            dndb_id=character_data.id,
            name=character_data.name,
            level=sum(c.level for c in character_data.classes),
            avatar_url=str(character_data.decorations.avatar_url),
            page_url=str(character_data.readonly_url),
        )

        self.session.add(character)
        self.session.commit()
        self.session.refresh(character)

        self.create_health_from_api(character_data, character)
        self.create_stats_from_api(character_data, character)
        self.create_saves_from_api(character_data, character)

        return character

    def create_health_from_api(
        self, character_data: ApiCharacter, character: Character
    ):
        if character.id is None:
            raise ValueError("Character must have an ID to create saves")

        health = Health(
            character_id=character.id,
            base_hp=character_data.base_hit_points,
            bonus_hp=character_data.bonus_hit_points or 0,
            removed_hp=character_data.removed_hit_points,
            temp_hp=character_data.temporary_hit_points,
        )
        self.session.add(health)
        self.session.commit()

    def create_stats_from_api(self, character_data: ApiCharacter, character: Character):
        if character.id is None:
            raise ValueError("Character must have an ID to create saves")

        stats = Stats(
            character_id=character.id,
            strength=character_data.strength,
            dexterity=character_data.dexterity,
            constitution=character_data.constitution,
            intelligence=character_data.intelligence,
            wisdom=character_data.wisdom,
            charisma=character_data.charisma,
        )
        self.session.add(stats)
        self.session.commit()

    def create_saves_from_api(self, character_data: ApiCharacter, character: Character):
        if character.id is None:
            raise ValueError("Character must have an ID to create saves")

        saves = Saves(
            character_id=character.id,
            fail_count=character_data.death_saves.fail_count or 0,
            success_count=character_data.death_saves.success_count or 0,
            is_stabilized=character_data.death_saves.is_stabilized,
        )
        self.session.add(saves)
        self.session.commit()

    def update_character_from_api(
        self, character: Character, character_data: ApiCharacter
    ) -> Character:
        character.name = character_data.name
        character.level = sum(c.level for c in character_data.classes)
        character.avatar_url = str(character_data.decorations.avatar_url)
        character.page_url = str(character_data.readonly_url)

        health = self.session.get(Health, character.id)
        if health is None:
            health = self.create_health_from_api(character_data, character)
        else:
            health.base_hp = character_data.base_hit_points
            health.bonus_hp = character_data.bonus_hit_points or 0
            health.removed_hp = character_data.removed_hit_points
            health.temp_hp = character_data.temporary_hit_points

        stats = self.session.get(Stats, character.id)
        if stats is None:
            stats = self.create_stats_from_api(character_data, character)
        else:
            stats.strength = character_data.strength
            stats.dexterity = character_data.dexterity
            stats.constitution = character_data.constitution
            stats.intelligence = character_data.intelligence
            stats.wisdom = character_data.wisdom
            stats.charisma = character_data.charisma

        saves = self.session.get(Saves, character.id)
        if saves is None:
            saves = self.create_saves_from_api(character_data, character)
        else:
            saves.fail_count = character_data.death_saves.fail_count or 0
            saves.success_count = character_data.death_saves.success_count or 0
            saves.is_stabilized = character_data.death_saves.is_stabilized

        self.session.commit()
        self.session.refresh(character)

        return character
