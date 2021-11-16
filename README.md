# dnd
A small Python app for providing DND data.
- Using a mysql database.
- Using Flask to offer a webserver.


# Setup

- Edit config.json 


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