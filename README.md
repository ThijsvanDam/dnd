# dnd
A small Python app for providing DND data.
- Using `Mysql` for a database.
- Using `Flask` to offer a webserver.
- Using `Jinja` to render templates.
- Using `Dndb` to fetch character data.

# Setup (Unix/macOS)

- Install python through `brew install python` 
- Create virtual environment by running
`python -m venv /path/to/new/virtual/environment` or [for Windows](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- Use venv by running `source {envPath}/bin/activate` or [for Windows](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- Install python packages by running `python -m pip install -r ./requirements.txt` or [for Windows](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
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
- Install mysql by running `brew install mysql`
- Go to the `scripts` folder in your terminal and run `mysql < databaseAndTables.sql` to create database and tables.
- Run `mysql < fillDbWithIykwim.sh` to fill with IYKWIM data.
/----- alternative to above two steps: -----\
- Open mysql command line by running `mysql` 
- Create database and tables by running `source {projectPath}/scripts/databaseAndTables.sql`
  **NOTE: This removes the current database names 'dnd' including its data.**
- Fill database with iykwim data by running `source {projectPath}/scripts/fillDbWithIykwim.sh`
\-------------------------------------------/
- After creating and filling the database and installing all requirements:
- Run `python3 app.py` to run the application.

# Package explanation:

- /data:
Classes to access and parse the dndbeyond data

- /repositories:
Has a db instance to run it's queries on

- /db:
Actual connection to the database and performing the queries

- /services:
All stateless classes performing some sort of action.
    - /Data All stateless classes performing some sort of action with data (e.g. gathering dndb data and parsing it)

- /models:
Dataclasses used to contain data, defining two groups:
    - DbModels:
    *Defining the models that are stored in the database. All read only.*
    - Other:
    *Defining the models that contain newly fetched (e.g. dndb) data.*

- /static:
Css and img data for the webpages and components.

- /templates:
Webpages and components used to render pages.

- /examples:
Examples of character data gathered from dndb.

- /scripts:
Scripts that can be run 