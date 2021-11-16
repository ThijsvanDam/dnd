# dnd
A small Python app for providing DND data.
- Using a mysql database.
- Using Flask to offer a webserver.


# Setup (Unix/macOS)

- Install python3
- Create virtual environment by running
`python3 -m venv /path/to/new/virtual/environment` or [for Windows](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- Use venv by running `source {envPath}/bin/activate`
- Install python packages by running `python3 -m pip install -r ./requirements.txt`
- Create config.json according to the example:
```
{
    "app": {
        "ip": "127.0.0.1",
        "port": "5001"
    },
    "database": {
        "username": "root",
        "password": ""
    }
}
```
- Create database by running `scripts/createDatabaseAndTables.sh`
- Fill database with iykwim data by running `scripts/fillDbWithIykwim.sh`


# Package explanation:

- /data:
Classes to access and parse the dndbeyond data

- /repositories:
Has a db instance to run it's queries on

- /db
Actual connection to the database and performing the queries

- /services
All stateless classes performing some sort of action.
    - /Data All stateless classes performing some sort of action with data (e.g. gathering dndb data and parsing it)

- /models
Dataclasses used to contain data, defining two groups:
    - DbModels
    *Defining the models that are stored in the database. All read only.*
    - Other
    *Defining the models that contain newly fetched (e.g. dndb) data.*

- /static
Css and img data for the webpages and components.

- /templates
Webpages and components used to render pages.

- /examples
Examples of character data gathered from dndb.

- /scripts
Scripts that can be run 