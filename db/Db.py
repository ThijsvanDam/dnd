
import mysql
from mysql.connector import (connection)


config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'dnd',
    'raise_on_warnings': True
}


class Db:
    def __init__(self):
        self.connection = mysql.connector.connection.MySQLConnection(**config)
        self.cursor = self.connection.cursor()

    def run_query(self, query):
        try:
            return self.cursor.execute(query)

        except mysql.connector.Error as err:
            print(f"Failed running query: {err}")
            return

    def __del__(self):
        self.cursor.close()
        self.connection.close()
