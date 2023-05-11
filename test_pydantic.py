# %%
import json

from models.beyond.Character import Character

with open("example_henk.json", "r") as f:
    data = json.load(f)

c = Character.parse_obj(data["data"])
...

# %%
from services.beyond.DndbDataFetchService import DndbDataFetchService

dndb = DndbDataFetchService()
c = dndb.get_character(48845859)
...