# IYKWIM DND CHARACTER LOADER
A small Python app for providing DND data.
- Using `SQLModel` for database interaction.
- Using `Flask` to offer a webserver.
- Using `Jinja` to render templates.
- Using `Dndb` to fetch character data.

# Contact
Feel free to contact me on this GitHub account or on thijsvandamtvd@gmail.com.

# Setup (Unix/macOS with Windows alternatives)

- Install python (3+) through `brew install python` 
- Create virtual environment by running
`python -m venv /path/to/new/virtual/environment` or [for Windows](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- Use venv by running `source {envPath}/bin/activate` or [for Windows](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- Install python packages by running `python -m pip install -r ./requirements.txt` or [for Windows](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- Create config.json according to the example: `{ "app": { "ip": "127.0.0.1", "port": "5001" }, "database": { "username": "root", "password": "" } }`
- Install SQLite by running `brew install sqlite` or [for Windows](https://www.sqlitetutorial.net/download-install-sqlite/)
- Run `python create_db.py` to create the database and tables.
- Run `python app.py` to run the application.

# Package explanation:

- /controllers:
Classes to handle the database logic of the application.

- /db:
Actual connection to the database.

- /services:
All stateless classes performing some sort of action.
    - /data: All stateless classes performing the gathering dndb data and parsing it.

- /models:
Dataclasses used to contain data stored in the database.

- /static:
Css and img data for the webpages and components.

- /templates:
Webpages and components used to render pages.

- /examples:
Examples of character data gathered from dndb.

- /instance:
A directory that flask uses. Program data like settings are gathered from there.