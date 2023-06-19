import mysql
from typing import Any, List, Dict
from services.ConfigService import ConfigService

from sqlalchemy.orm import Session
from sqlalchemy import Select, create_engine
from sqlalchemy import text
from sqlalchemy import Engine
from sqlalchemy import Connection
from sqlalchemy import CursorResult

# config = {
#     'user': custom_config['username'],
#     'password': custom_config['password'],
#     'host': '127.0.0.1',
#     'database': 'dnd',
#     'raise_on_warnings': True
# }

"""
Actual connection to the database and performing the queries.
Returns the data in a proper format.
"""


class Db:
    connected = False
    session: Session

    def __init__(self) -> None:
        dbConfig: dict[str, Any] = ConfigService().get_database_config()

        # https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine
        try:
            self.engine: Engine = create_engine(
                f"sqlite:///{dbConfig['path']}", echo=True
            )
            self.connection: Connection = self.engine.connect()
            print("Database connection is established.")
            self.connected = True
        except Exception as e:
            print(f"Could not make database connection: {e}")

    def fetch_single(self, query) -> Dict:
        # Always has a single item, so the first item of the cursor can be returned.
        return self._perform_query(query).first()

    def fetch_multiple(self, query) -> List[Dict]:
        # Convert the cursor stuff to a list of actual data.
        return self._perform_query(query).fetchall()

    def check_connection(self) -> bool:
        if not self.connected:
            raise Exception(
                "Can't connect to database, restart application and check your config."
            )
        return True

    # """Performs every textual and returns the cursor.
    # Note: Actually returns cursor stuff
    # """
    def _perform_query(self, query) -> CursorResult:
        if not self.check_connection():
            return

        try:
            with Session(self.engine) as session:
                result = session.execute(query)
                return result
            # return self.connection.execute(text(query))
        except Exception as e:
            print(f"Failed running query: {query} with error: {e}")

    def __enter__(self):
        # open session to database
        self.session = Session(self.engine)
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        # close session to database
        self.session.close()

    # """Closes the database connection.
    # """
    def close(self) -> None:
        self.connection.close()
        self.connected = False
        print("Database connection is closed.")
