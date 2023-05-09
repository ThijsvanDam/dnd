# %%
import json

from models import Character

with open("example_henk.json", "r") as f:
    data = json.load(f)

c = Character.parse_obj(data["data"])
...
