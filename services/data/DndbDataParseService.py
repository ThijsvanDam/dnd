from models import Character, Stats, Health, Saves
import json

"""
Parsing dndb json character data to the known Character model.
"""
class DndbDataParseService:
    
    @staticmethod
    def parse_stats(parsed_data):
        # Base stats
        statsList = [
            parsed_data['stats'][0]["value"],
            parsed_data['stats'][1]["value"],
            parsed_data['stats'][2]["value"],
            parsed_data['stats'][3]["value"],
            parsed_data['stats'][4]["value"],
            parsed_data['stats'][5]["value"],
        ]
        
        # Add racial bonus
        racialModifiersList = parsed_data['modifiers']['race']
        racialScores = list(filter(lambda x: x['subType'].endswith('-score'), racialModifiersList))
        for score in racialScores:
            modId = score['modifierSubTypeId']
            value = score['value']
            statsList[modId - 2] += value
        
        # Add class bonus
        invalidClassBonusString = "choose-an-ability-score"
        classModifiersList = parsed_data['modifiers']['class']
        classScores = list(filter(lambda x: (x['subType'].endswith('-score') and x['subType'] != invalidClassBonusString), classModifiersList))
        for score in classScores:
            modId = score['modifierSubTypeId']
            value = score['value']
            statsList[modId - 2] += value
        
        # Todo's based on modifiers from 
        # TODO: Add misc bonus
        # TODO: Add stacking bonus
        # TODO: Add set score
        # TODO: Add other modifier?
        
        return Stats(*statsList)
    
    @staticmethod
    def parse_health(parsed_data):
        healthObject = {
            'base_hp': parsed_data['baseHitPoints'],
            'bonus_hp': parsed_data['bonusHitPoints'],
            'removed_hp': parsed_data['removedHitPoints'],
            'temp_hp': parsed_data['temporaryHitPoints'],
            'total_hp': 0
        }
        return Health(**healthObject)
    
    @staticmethod
    def parse_saves(parsed_data):
        saveData = {
            'deathSaves': parsed_data['deathSaves'] or 0,
            'successSaves': parsed_data['successSaves'] or 0,
            'isStabilized': parsed_data['isStabilized']
        }
        return Saves(**saveData)
        

    def parse_character_data(self, data) -> Character:
        """
        This method parses all character data and returns a usable dictionary
        :param data:
        :return:
        """
        parsed_data = json.loads(data)['data']
        
        gathered_data = {
            'name': parsed_data['name'],
            'level': parsed_data['classes'][0]['level'],
            'avatar_url': parsed_data['avatarUrl'],
            'page_url': parsed_data['readonlyUrl'],
            'stats': DndbDataParseService.parse_stats(parsed_data=parsed_data),
            'health': DndbDataParseService.parse_health(parsed_data=parsed_data),
            'saves': DndbDataParseService.parse_saves(parsed_data=parsed_data)
        }
        
        # TODO: Think of a better way to do this. Total hp is based on base hp, level and conMod.
        gathered_data['health'].total_hp = gathered_data['health'].base_hp + (gathered_data['level'] * gathered_data['stats'].conMod)
        
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
