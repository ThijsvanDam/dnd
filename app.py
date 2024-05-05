import os
import json
import atexit

from flask import Flask, render_template

from db.database import Db
from controllers.character_controller import CharacterRepo
from controllers.player_controller import PlayerRepo

from services.character_service import CharacterService
from services.data.dnd_beyond_fetch_service import DndbDataFetchService as DataFetcher
from services.data.dnd_beyond_data_parse_service import DndbDataParseServiceV3 as DataParser

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.player import Player

# from models.Character import Character


# TODO: https://stackoverflow.com/questions/66716267/lask-cli-noappexception-while-importing-app-an-importerror-was-raised
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("flask_config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # index page
    @app.route("/")
    def home():
        return render_template(
            "home.html",
            nav=nav,
            title="Welkom op de D&D pagina.",
            description="Hier kun je alle geupdate informatie over de IYKWIM D&D characters vinden.",
        )

    @app.route("/character/id/<id>")
    def characterById(id: int):
        # dbCharacter = char_s.get_character_with_id(id)
        # raw_character_data = fetcher.get_character(character_id=dbCharacter.dndb_id)
        # parsed_character_data = dndb_parser.parse_character_data(raw_character_data)
        parsed_character_data = None
        return render_template(
            "widget/character_widget_page.html",
            nav=nav,
            character=parsed_character_data,
            isolated=True,
        )

    @app.route("/character/id/<id>/json")
    def parsedCharacterDataById(id: int):
        dbCharacter = char_s.get_character_with_id(id)
        # raw_character_data = fetcher.get_character(character_id=dbCharacter.dndb_id)
        # parsed_character_data = dndb_parser.parse_character_data(raw_character_data)
        parsed_character_data = None
        return parsed_character_data.toJSON()

    @app.route("/character/id/<id>/raw")
    def rawCharacterDataById(id: int):
        dbCharacter = char_s.get_character_with_id(id)
        raw_character_data = fetcher.get_character(character_id=dbCharacter.dndb_id)
        return raw_character_data

    @app.route("/character/name/<name>")
    def characterByName(name):
        raise NotImplementedError()

    @app.route("/character/all")
    def characters():
        characters = char_s.get_all_characters()

        return render_template(
            "characters/characters_page.html",
            nav=nav,
            title="All characters",
            description="This is a list of all characters.",
            characters=characters,
        )

    @app.route("/character/widget/all")
    def widgets():
        # dbCharacters = char_s.get_all_characters()
        # characterList = []
        # for dbCharacter in dbCharacters:
        #     if dbCharacter == None:
        #         continue

        #     raw_character_data = fetcher.get_character(character_id=dbCharacter.dndb_id)
        #     parsed_character_data = dndb_parser.parse_character_data(raw_character_data)
        #     characterList.append(parsed_character_data)
        characterList = [None]
        return render_template(
            "widget/character_widgets.html",
            nav=nav,
            title="All character widgets",
            description="This is a list of all character widgets.",
            characters=characterList,
        )

        # return render_template(
        #     'characters/characters.html',
        #     nav=nav,
        #     title="All characters",
        #     description="This is a list of all characters.",
        #     characters=characters
        # )

    return app


if __name__ == "__main__":
    custom_config = json.load(open("./config.json"))["app"]
    db = Db()

    # this is not the way to go, but it works for now
    with Session(db.engine) as session:
        db.session = session

        playerRepo = PlayerRepo(db)
        player: Player = playerRepo.get_player_with_id(1)
        print(player)

        char_r = CharacterRepo(db)
        char_s = CharacterService(char_r)

        char_r.get_all_characters()
        for character in char_r.get_all_characters():
            print(character)

        fetcher = DataFetcher()

        dndb_parser = DataParser()

        """Landing page."""
        nav: list[dict[str, str]] = [
            {"name": "Home", "url": "/"},
            {"name": "Characters", "url": "/character/all"},
            {"name": "Widgets", "url": "/character/widget/all"},
        ]

        # atexit.register(db.close)
        create_app().run(custom_config["ip"], port=int(custom_config["port"]))
