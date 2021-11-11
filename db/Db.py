
import mysql
import json
from mysql.connector import (connection)

custom_config = json.load(open('./db_config.json'))

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

    def run_query(self, query):
        try:
            result = self.cursor.execute(query)
            print(result)
            return result

        except mysql.connector.Error as err:
            print(f"Failed running query: {err}")
            return

    # def __del__(self):
    #     self.cursor.close()
    #     self.connection.close()
