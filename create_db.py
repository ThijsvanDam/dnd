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

    # Seed the database with known characters
    character_ids = [
        48841293,  # Aeyham
        48841603,  # Sarscov
        48853773,  # Eluniss
        48845859,  # Henk
        54055260,  # Johno
        48850684,  # Pjotr Vladimir
        48842849,  # Paloma Pigéon
        48846746,  # Takata Wakanda
    ]

    character_controller = CharacterController()
    for character_id in character_ids:
        dndb_character = DndbDataFetchService.get_character(character_id)
        _ = character_controller.create_character(dndb_character)
