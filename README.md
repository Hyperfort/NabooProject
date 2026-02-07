# NabooProject

An unofficial Star Wars–inspired REST API built with FastAPI and Motor (async MongoDB). It exposes simple endpoints for characters, factions, spaceships, and worlds so you can quickly explore or prototype against a small galaxy dataset.

Key features
- FastAPI app with lifespan-managed MongoDB connection
- Pydantic v2 models and custom ObjectId handling
- Async MongoDB access via Motor
- OpenAPI docs auto-generated at /docs and /redoc

Prerequisites
- Python 3.12+
- A running MongoDB instance and connection URI

Install
1. Create a virtual environment and activate it:

```bash
python3 -m venv .venv --prompt="NabooProject"
source .venv/bin/activate
```

2. Install dependencies:

```bash
# sync runtime deps into the active venv
uv sync --extra dev --python .venv/bin/python
```

Configuration (.env)
Create a `.env` file in the repository root with the following variables:

```env
MONGODB_URI=mongodb://localhost:27017
MONGODB_DATABASE=naboo_project
```

Run (development)

```bash
uvicorn app.main:app --reload
```

API
- Health check: GET /health
- List characters: GET /characters
- List factions: GET /factions
- List spaceships: GET /spaceships
- List worlds: GET /worlds

OpenAPI docs:
- Interactive UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Example curl

```bash
curl http://localhost:8000/characters
```

Models (high level)
- StarWarsModel (base): id (_id), name, appearances
- Character: affiliation, homeworld, species
- Faction: type, era
- Spaceship: model, manufacturer, affiliation
- World: region, sector, affiliation

Project structure

```text
NabooProject/
├── app/
│   ├── main.py                  # FastAPI app + lifespan (MongoDB init)
│   ├── core/
│   │   ├── config.py            # Settings (pydantic-settings)
│   │   └── database.py          # Motor client and get_db()
│   ├── models/                  # Pydantic models (StarWarsModel + types)
│   └── routes/                  # Route modules for each resource
├── .env                         # local env (not checked in)
├── pyproject.toml               # project metadata & deps
└── README.md
```

Notes for developers
- The app uses a lifespan context (in `app.main`) to open/close the MongoDB connection.
- `app.models.object_id.PyObjectId` provides Pydantic v2 integration for BSON ObjectIds.
- `app.routes.*` modules return Pydantic models which are serialized to JSON (ObjectId -> str).
- Ensure your `.env` is present before running the server, otherwise the DB connection will fail.

Links
- FastAPI: https://fastapi.tiangolo.com

Running tests
----------------

Unit tests are provided in the `tests/` directory and use `pytest` (including `pytest-asyncio`).

```bash
# run the test suite
pytest --verbose
```
