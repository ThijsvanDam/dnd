from sqlmodel import SQLModel, create_engine

from db.database import sqlite_url
from models.character import Character
from models.player import Player
from models.saves import Saves
from models.stats import Stats

# Create the engine
engine = create_engine(sqlite_url, echo=True)

# Create the tables
SQLModel.metadata.create_all(engine)
