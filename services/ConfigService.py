import json
from .Singleton import Singleton

custom_config = json.load(open('./config.json'))

class ConfigService(Singleton):
    
    def get_api_version(self) -> int:
        return int(custom_config['app']['dndB']['apiVersion'])

    def get_database_config(self):
        return {
          'user': custom_config['database']['username'],
          'password': custom_config['database']['password'],
          'host': '127.0.0.1',
          'database': 'dnd',
          'raise_on_warnings': True
        }