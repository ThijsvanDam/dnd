import os

from flask import Flask

from db.Db import Db
from services.CharacterService import CharacterService
from repos.CharacterRepo import CharacterRepo

# db = Db()
# char_r = CharacterRepo(db)
# char_s = CharacterService(char_r)

# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

#TODO: https://stackoverflow.com/questions/66716267/lask-cli-noappexception-while-importing-app-an-importerror-was-raised

# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )
#
#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)
#
#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass
#
#     # a simple page that says hello
#     @app.route('/app')
#     def hello():
#         # return char_s.get_character_with_player_id(1)
#         return 'Hello, World!'
#
#     return app


create_app()
