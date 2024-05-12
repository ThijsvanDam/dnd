from flask import Flask, render_template, g, jsonify

from db.database import init_session
from controllers.character_controller import CharacterController


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    @app.before_request
    def open_session():
        # Store session in g which is unique to each request
        g.session = next(init_session())

    @app.teardown_request
    def close_session(response_or_exc):
        # Check if a session was created and if so, close it
        session = g.pop("session", None)
        if session is not None:
            session.close()
        return response_or_exc

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
    def character_by_id(id: int):
        character_controller = CharacterController()
        db_character = character_controller.get_character_with_id(id)

        if db_character is None:
            return render_template(
                "error.html",
                nav=nav,
                title="Character not found",
                description="The character with the given id could not be found.",
            )

        return render_template(
            "widget/character_widget_page.html",
            nav=nav,
            character=db_character,
            isolated=True,
        )

    @app.route("/character/id/<id>/json")
    def character_by_id_json(id: int):
        character_controller = CharacterController()
        db_character = character_controller.get_character_with_id(id)

        if db_character is None:
            return jsonify({"error": "Character not found"})

        return jsonify(db_character.model_dump())

    @app.route("/character/id/<id>/raw")
    def character_by_id_raw(id: int):
        raise NotImplementedError()

    @app.route("/character/all")
    def characters():
        character_controller = CharacterController()
        db_characters = character_controller.get_all_characters()

        return render_template(
            "characters/characters_page.html",
            nav=nav,
            title="All characters",
            description="This is a list of all characters.",
            characters=db_characters,
        )

    @app.route("/character/widget/all")
    def widgets():
        character_controller = CharacterController()
        db_characters = character_controller.get_all_characters()

        return render_template(
            "widget/character_widgets.html",
            nav=nav,
            title="All character widgets",
            description="This is a list of all character widgets.",
            characters=db_characters,
        )

    return app


if __name__ == "__main__":
    """Landing page."""
    nav: list[dict[str, str]] = [
        {"name": "Home", "url": "/"},
        {"name": "Characters", "url": "/character/all"},
        {"name": "Widgets", "url": "/character/widget/all"},
    ]

    create_app().run(debug=True)
