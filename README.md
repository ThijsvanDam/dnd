# dnd
A small Python app for providing DND data.
- Using a mysql database.
- Using Flask to offer a webserver.


# Setup

- Install python3
- Create virtual environment by running
`python3 -m venv /path/to/new/virtual/environment`
- Use venv by running {venvPath}/activate (maybe give runnable permission first through chmod +x {venvPath}/activate)
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
- Create database


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