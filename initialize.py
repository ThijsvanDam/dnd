from sqlalchemy import create_engine
from models.Base import Base
# from models.Health import Health
# from models.Character import Character
from models.Player import Player
# from models.Saves import Saves
# from models.Stats import Stats


engine = create_engine("sqlite:///./test.db", echo=True)

Player.metadata.create_all(engine)

# Base.metadata.create_all(engine, tables=[Health])

with Session(engine) as session:

    players = [Player(
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