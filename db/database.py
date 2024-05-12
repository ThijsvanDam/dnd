from flask import g
from sqlmodel import Session, SQLModel, create_engine

sqlite_file_name = "dnd.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def init_session():
    with Session(engine) as session:
        yield session


def get_session() -> Session:
    return g.session
