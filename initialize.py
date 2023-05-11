from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models.Player import Player

engine = create_engine("sqlite:///test.db", echo=True)

Player.metadata.create_all(engine)

with Session(engine) as session:
    players = [
        Player(
            name="Aehyam",
            password="test123",
            role="Admin",
        ),
        # Player(
        #     name="Lex",
        #     password="vlimvlom",
        #     role="Nerd"
        # ),
    ]

    session.add_all(players)

    session.commit()
