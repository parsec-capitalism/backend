# About
Backend for the game Parsec Capitalism.
Made using:
- Django
- Sqlite

---
**Table of Contents**
 - [Project Structure](#project-structure)
 - [Setup](#setup)
    - [Python](#python)
    - [Load game data](#load-game-data)
    - [Django](#django)
 - [Test API](#bruno-api-testing)
 - [Endpoints](#endpoints)
---

## Setup

### Python

First, you need to activate virtual enviroment and install requirements.
This should be done from `~backend/`
```bash
# Create virtual enviroment
python3 -m venv venv 

# Launch virtual enviroment
source venv/bin/activate 

# Install dependencies inside VE
python3 -m pip install -r requirements.txt 

# If you need to deactivate venv
deactivate
```

### Load game data
Game data is stored in `~backend/parsec_capitalism/static/game_data` in a csv files.
```bash
# Command should be done from ~backend/parsec_capitalism/
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


## Bruno api testing

### How import collection

1. Download Bruno: https://www.usebruno.com/.
2. In the menu at the top left corner choose "Import collection" and pick "Bruno collection".
3. Choose the folder bruno_collection inside Backend repo.

### How run the collection
1. Right-click the collection name in the left menu.
2. Choose Settings.
3. Go to the Vars tab.
4. Add value to the Username variable (this should be done before every Run). Press Save.
5. Right-click the collection name in the left menu again and choose Run.
6. Run Collection.v


## Endpoints 
`api/v1/docs/` - API Documentation (OpenAPI 3.0 compatible)
`admin/` - Admin panel


