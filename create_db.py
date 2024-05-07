from sqlmodel import SQLModel, create_engine

from controllers.character_controller import CharacterController
from db.database import init_session, sqlite_url
from services.data.dnd_beyond_fetch_service import DndbDataFetchService

from flask import Flask, g

app = Flask(__name__)
with app.app_context():
    # Create the engine
    engine = create_engine(sqlite_url, echo=True)
    g.session = next(init_session())

    # Create the tables
    SQLModel.metadata.create_all(engine)

    # The character API returns all characters in the campaign, so we only need to know one character id
    character_id = 48841293  # Aeyham

    character_controller = CharacterController()
    character = DndbDataFetchService.get_character(character_id)
    character_ids = [
        character.character_id for character in character.campaign.characters
    ]

    for character_id in character_ids:
        print(f"Fetching character with id {character_id}")
        dndb_character = DndbDataFetchService.get_character(character_id)
        _ = character_controller.create_character(dndb_character)
