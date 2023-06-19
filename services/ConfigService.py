import json
from .Singleton import Singleton

custom_config = json.load(open('./config.json'))

class ConfigService(Singleton):
    
    def get_api_version(self) -> int:
        return int(custom_config['app']['dndB']['apiVersion'])

    def get_database_config(self):
        return {
          'path': custom_config['database']['path'],
          # 'database': 'dnd',
          # 'raise_on_warnings': True
        }