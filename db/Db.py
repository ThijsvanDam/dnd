
import mysql
import json
from typing import Any, List, Dict
from mysql.connector import (connection)

custom_config = json.load(open('./config.json'))['database']

config = {
    'user': custom_config['username'],
    'password': custom_config['password'],
    'host': '127.0.0.1',
    'database': 'dnd',
    'raise_on_warnings': True
}

"""
Actual connection to the database and performing the queries.
Returns the data in a proper format.
"""
class Db:
    connected = False

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(**config)
            self.cursor = self.connection.cursor()
            print("Database connection is established.")
            self.connected = True
        except Exception as e:
            print(f"Could not make database connection: {e}")
        

    def fetch_single(self, query) -> Dict:
        # Always has a single item, so the first item of the cursor can be returned.
        return self._perform_query(query).fetchone()
    
    def fetch_multiple(self, query) -> List[Dict]:
        # Convert the cursor stuff to a list of actual data.
        return list(self._perform_query(query))
    
    def check_connection(self) -> bool:
        if not self.connected:
            print("Can't connect to database, restart application and check your config.")
        return True

    """Performs every textual and returns the cursor.
    Note: Actually returns cursor stuff
    """
    def _perform_query(self, query) -> Any:
        if not self.check_connection(): return

        try:
            self.cursor.execute(query)
            # Cursor contains data baout the executed query
            return self.cursor

        except mysql.connector.Error as err:
            print(f"Failed running query: {err}")
            return

    """Closes the database connection.
    """
    def close(self):
        self.cursor.close()
        self.connection.close()
        self.connected = False
        print("Database connection is closed.")
