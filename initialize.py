from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


from models.Base import Base
from models.Player import Player
from models.Character import Character

# Let's read the following: https://medium.com/@sandyjtech/creating-a-database-using-python-and-sqlalchemy-422b7ba39d7e



engine = create_engine("sqlite:///test.db", echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

# with Session(engine) as session:

players = [
    Player(
        name="Thijs",
        password="test123",
        role="Admin",
    ),
    Player(
        name="Alex",
        password="vlimvlom",
        role="Nerd"
    ),
]

session.add_all(players)


session.commit()
