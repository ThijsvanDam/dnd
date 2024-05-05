from services.data.dnd_beyond_fetch_service import DndbDataFetchService


character = DndbDataFetchService().get_character(48841603)
print(character)