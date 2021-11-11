
import mysql
import json
from mysql.connector import (connection)

custom_config = json.load(open('./config.json'))['database']

config = {
    'user': custom_config['username'],
    'password': custom_config['password'],
    'host': '127.0.0.1',
    'database': 'dnd',
    'raise_on_warnings': True
}


class Db:
    def __init__(self):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def fetch_single(self, query):
        return self._perform_query(query).fetchone()
    
    def fetch_multiple(self, query):
        return list(self._perform_query(query))
    
    def _perform_query(self, query):
        try:
            result = self.cursor.execute(query)
            return self.cursor

        except mysql.connector.Error as err:
            print(f"Failed running query: {err}")
            return

    def close(self):
        self.cursor.close()
        self.connection.close()
