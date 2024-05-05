from typing import Sequence
from sqlmodel import select
from models.character import Character
from ..db.database import get_session
from ..services.data.api_model import Character as ApiCharacter
from models.health import Health
from models.stats import Stats
from models.saves import Saves


class CharacterRepo:
    def __init__(self):
        self.session = get_session()

    def get_all_characters(self) -> Sequence[Character]:
        stmt = select(Character)
        return self.session.exec(stmt).all()

    def get_character_with_id(self, character_id: int) -> Character | None:
        stmt = select(Character).where(Character.dndb_id == character_id)
        return self.session.exec(stmt).first()

    def get_characters_with_player_id(self, player_id: int) -> Sequence[Character]:
        stmt = select(Character).where(Character.player_id == player_id)
        return self.session.exec(stmt).all()

    def create_character(self, character_data: ApiCharacter) -> Character:
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

        if character.id is None:
            raise ValueError("Character id is None after creation")

        health = Health(
            character_id=character.id,
            base_hp=character_data.base_hit_points,
            bonus_hp=character_data.bonus_hit_points or 0,
            removed_hp=character_data.removed_hit_points,
            temp_hp=character_data.temporary_hit_points,
        )
        stats = [
            Stats(stat_id=stat.id, value=stat.value) for stat in character_data.stats
        ]
        saves = [
            Saves(
                stat_id=save.id,
                value=save.value,
                proficiency=save.proficiency,
                character=character,
            )
            for save in character_data.saves
        ]

        self.session.add(character)
        self.session.commit()
        self.session.refresh(character)
        return character
