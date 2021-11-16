from models.Character import Character
from models.Stats import Stats
import json

"""
Parsing dndb json character data to the known Character model.
"""
class DndbDataParseService:

    def parse_character_data(self, data) -> Character:
        """
        This method parses all character data and returns a usable dictionary
        :param data:
        :return:
        """
        parsed_data = json.loads(data)

        gathered_data = {
            'name': parsed_data['data']['name'],
            'level': parsed_data['data']['classes'][0]['level'],
            'avatar_url': parsed_data['data']['avatarUrl'],
            'page_url': parsed_data['data']['readonlyUrl'],
            'stats': Stats(
                str = parsed_data['data']['stats'][0]["value"],
                dex = parsed_data['data']['stats'][1]["value"],
                con = parsed_data['data']['stats'][2]["value"],
                int = parsed_data['data']['stats'][3]["value"],
                wis = parsed_data['data']['stats'][4]["value"],
                cha = parsed_data['data']['stats'][5]["value"],
            ),
            'base_hp': parsed_data['data']['baseHitPoints'],
            'bonus_hp': parsed_data['data']['bonusHitPoints'],
            'removed_hp': parsed_data['data']['removedHitPoints'],
            'temp_hp': parsed_data['data']['temporaryHitPoints']
        }

        return Character(**gathered_data)
    
    # TODO: Remove this (huge) comment once you emotionally processed the fact that you parse the data in a more generic way but you can't.
    #  dndb_data_map = {
    #     'name': {'data': 'name'},
    #     'level': { 'data': { 'classes': 'level'}},
    #     'avatar_url': {'data': 'avatarUrl'},
    #     'base_hp': {'data': 'baseHitPoints'}, # +characterValues, value?
    #     'bonus_hp': {'data': 'bonusHitPoints'},
    #     'removed_hp': {'data': 'removedHitPoints'},
    #     'temp_hp': {'data': 'temporaryHitPoints'},
    #     'stats': {
    #         'str': { 'data': { 'stats' : {'id': 1, 'value': 'str'}}},
    #         'dex': { 'data': { 'stats' : {'id': 2, 'value': 'dex'}}},
    #         'con': { 'data': { 'stats' : {'id': 3, 'value': 'con'}}},
    #         'int': { 'data': { 'stats' : {'id': 4, 'value': 'int'}}},
    #         'wis': { 'data': { 'stats' : {'id': 5, 'value': 'wis'}}},
    #         'cha': { 'data': { 'stats' : {'id': 6, 'value': 'cha'}}},
    #     }
    # }
    # TODO: Check out the idea to just work with paths like 'level.data.classes.0.level' 
    # This way you can specify paths AND work with arrays and maybe solve this in a more generic way.
    
    # def get_data(self, json, data_selector):

    #     keys, values = zip(*data_selector.items())

    #     keys = keys[0]
        # values = values[0]

        # print("Called with:")
        # print(data_selector)
        # print(keys)
        # print(values)

        # # if(values.length > 0):
        # #     # Het is een lijst, zoals 'stats'
        # #     if(keys[0] == 'stats'):
        # #         return "NOTIMPLEMENTED"

        # if type(values) is dict:
        #     # We zijn er nog niet, even doorzoeken
        #     return self.get_data(json[keys], values)
        # else:
        #     return json[keys][values]
        # # print(data_selector)


        # }
        # for item in self.dndb_data_map:
        #     gathered_data[item] = self.get_data(parsed_data, self.dndb_data_map[item])
        #     print("-----RESULT-----")
        #     print(gathered_data)
        #     print("-----NEXT-----")
