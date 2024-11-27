# About
Backend for the game Parsec Capitalism.
Made using:
- Django
- Sqlite (to be changes to PostreSQL)

---
**Table of Contents**
 - [Project Structure](#project-structure)
 - [Setup](#setup)
 - [API](#api)
---

## Setup

### Python

First, you need to activate virtual enviroment and install requirements.
This should be done from `~backend/`
```bash
#Create virtual enviroment
python3 -m venv venv 

# Launch virtual enviroment
source venv/bin/activate 

# Install dependencies inside VE
python3 -m pip install -r requirements.txt 

# If you need to deactivate venv
deactivate
```

### Load game data
Game data is stored in `~backend/static/game_data` in a csv files.
```bash
#Command should be done from ~backend/parsec_capitalism/
python3 manage.py loadcsv
```
This command will clean all respective DBs(models) and populate them with the objects from csv files.


### Django
Next step is to launch django project. Commands should be executed from `~backend/parsec_capitalism/`
```bash
# Migrate apps databases
python3 manage.py migrate

# Run the server 
python3 manage.py runserver
```
After that the server should be running and you can find it at [127.0.0.1:8000](http://127.0.0.1:8000/).


## Endpoints 
`api/v1/docs` - API Docummentation (OpenAPI 3.0 compatible)


