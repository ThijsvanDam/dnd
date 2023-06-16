from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from models.Player import Player
from models.Character import Character

engine: Engine = create_engine("sqlite:///dnd.db", echo=True)

Player.metadata.create_all(engine)
Character.metadata.create_all(engine)


# future:
# from models.Campaign import Campaign
# campaigns_tuples: list = [
# 	(1,'IYKWIM',1938481)
# ]
#
# campaigns: list[Campaign] = campaigns_tuples.map(lambda x: Campaign(
#     id=x[0],
#     name=x[1],
#     dndb_id=x[2]
# ))

players_tuples: list = [
    (1, "Aehyam", "test123", "Admin"),
    (2, "Lex", "vlimvlom", "Admin"),
    (3, "Rolo", "Roomboter", "Nerd"),
    (4, "Gudd", "ILikeVlimvlomNerd", "Nerd"),
]

characters_tuples: list = [
    (1, "Aehyam Weesarth", 48841293),
    (2, "Sarscov", 48841603),
    (3, "Eluniss", 48853773),
    (4, "Henk", 48845859),
    (5, "Johno", 54055260),
    (6, "Pjotr Vladimir", 48850684),
    (7, "Paloma Pigéon", 48842849),
    (8, "Takata Wakanda", 48846746),
]


with Session(engine) as session:
    players: list[Player] = [
        Player(id=id, name=name, password=password, role=role)
        for id, name, password, role in players_tuples
    ]
    characters: list[Character] = [
        Character(id=id, name=name, dndb_id=dndb_id)
        for id, name, dndb_id in characters_tuples
    ]

    session.add_all(players)
    session.add_all(characters)

    session.commit()
