# NabooProject

An unofficial Star Wars–inspired REST API built with [FastAPI](https://fastapi.tiangolo.com). It exposes read-only list endpoints for characters, factions, spaceships, and worlds so you can explore or prototype against a small galaxy dataset.

The service uses a **ports-and-adapters** layout: domain entities and repository ports sit at the center; application services orchestrate reads; outbound adapters talk to either **MongoDB** (Motor) or **MySQL** (aiomysql), selected at runtime via configuration.

## Features

- FastAPI app with lifespan-managed database connections (MongoDB or MySQL)
- Pluggable persistence: set `DATABASE_PROVIDER` to `mongodb` or `mysql`
- Domain layer with dataclass entities and `Protocol`-based repository ports
- Pydantic v2 response schemas with custom BSON `ObjectId` handling for MongoDB
- OpenAPI docs at `/docs` and `/redoc`
- Pytest suite with MongoDB-backed CI on `develop`

## Prerequisites

- Python 3.12+
- **MongoDB** (default): a running instance and connection URI, with collections `characters`, `factions`, `spaceships`, and `worlds`
- **MySQL** (optional): MySQL 8+ with schema applied from `scripts/mysql_schema.sql`
- **Vitess** (optional): a running local Kubernetes cluster with `vtgate` exposed through a port-forward

## Install

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv --prompt="NabooProject"
source .venv/bin/activate
```

2. Install dependencies:

```bash
uv sync --extra dev --python .venv/bin/python
```

## Configuration

Copy `.env.example` to `.env` and adjust values. The active backend is controlled by `DATABASE_PROVIDER`.

### MongoDB (default)

```env
DATABASE_PROVIDER=mongodb
MONGODB_URI=mongodb://localhost:27017
MONGODB_DATABASE=naboo_project
```

`MONGODB_URI` and `MONGODB_DATABASE` are required when using MongoDB.

### MySQL

```env
DATABASE_PROVIDER=mysql
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=naboo_project
```

Create the database and tables before starting the app:

```bash
mysql -u root -p naboo_project < scripts/mysql_schema.sql
```

JSON columns (`appearances`, `era`) store list fields; integer primary keys are exposed in API responses as string `id` values (via the `_id` alias).

### Vitess

The application connects to Vitess through the MySQL-compatible `vtgate` endpoint. For the local Kubernetes setup, configure `.env` with the `vtgate` host port and the Vitess application credentials:

```env
DATABASE_PROVIDER=mysql
MYSQL_HOST=127.0.0.1
MYSQL_PORT=15306
MYSQL_USER=vt_app
MYSQL_PASSWORD=your-vitess-password
MYSQL_DATABASE=naboo_project
```

Make sure the Kubernetes cluster is running, then verify the Vitess pods and locate the `vtgate` service:

```bash
kubectl get pods -A | grep -Ei 'vitess|naboo'
kubectl get svc -A | grep -Ei 'vitess|vtgate'
```

Forward the `vtgate` MySQL port to the host. Keep this terminal open while running the API:

```bash
kubectl port-forward -n default \
    svc/naboo-vitess-cluster-vtgate-f41759df \
    15306:3306
```

Use the service name shown by `kubectl get svc` if it differs in your cluster. Ensure the Vitess keyspace and `naboo_project` schema are initialized before starting the application.

## Run (development)

With MongoDB or a local MySQL server, start the API with:

```bash
uvicorn app.main:app --reload
```

With Vitess, use two terminals. In the first terminal, keep the `vtgate` port-forward running. In the second terminal:

```bash
source .venv/bin/activate
uvicorn app.main:app --reload
```

Verify that the API and database connection are ready:

```bash
curl http://localhost:8000/health
```

## Run with Rancher Desktop

Start Rancher Desktop with the Moby/Docker container engine enabled. Ensure MongoDB is available from the host on port `27017`. From the repository root, build the image and start the API container:

```bash
docker build -t naboo-api:dev .
docker run --detach \
  --name naboo-api \
  --restart unless-stopped \
  --publish 8000:8000 \
  --env DATABASE_PROVIDER=mongodb \
  --env MONGODB_URI=mongodb://host.docker.internal:27017 \
  --env MONGODB_DATABASE=naboo_project \
  naboo-api:dev
```

Check the API at http://localhost:8000/health. To stop and remove the container:

```bash
docker stop naboo-api
docker rm naboo-api
```

## API

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/characters` | List characters (default limit 100) |
| `GET` | `/factions` | List factions |
| `GET` | `/spaceships` | List spaceships |
| `GET` | `/worlds` | List worlds |

OpenAPI:

- Interactive UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Example:

```bash
curl http://localhost:8000/characters
```

## Data models

**Base (`StarWarsModel` / `StarWarsEntity`):** `id`, `name`, `appearances`

| Resource | Extra fields |
|----------|----------------|
| Character | `affiliation`, `homeworld`, `species` |
| Faction | `type`, `era` (list) |
| Spaceship | `model`, `manufacturer`, `affiliation` |
| World | `region`, `sector`, `affiliation` |

API responses use Pydantic models in `app/models/`; internally, adapters map storage records to domain entities in `app/domain/entities/`, and route handlers map entities back to schemas via `app/api/mappers.py`.

## Architecture

Request flow:

```text
HTTP route → FastAPI dependency (service) → application service → repository port
    → MongoDB or MySQL adapter → domain entity → API schema mapper → JSON
```

- **`app/domain/`** — Entities and repository port protocols (no framework or DB imports).
- **`app/application/services/`** — Thin services (e.g. `list(limit=100)`) that call ports.
- **`app/adapters/outbound/`** — Mongo and MySQL repository implementations plus `factory.py` to pick the adapter from `DATABASE_PROVIDER`.
- **`app/api/`** — FastAPI dependencies and entity-to-schema mappers.
- **`app/routes/`** — HTTP routers; one list endpoint per resource.
- **`app/core/`** — Settings, MongoDB client, MySQL pool, and shared lifespan helpers.

Adding a new storage backend means implementing the port protocols under `app/adapters/outbound/` and wiring them in `factory.py`.

## Project structure

```text
NabooProject/
├── app/
│   ├── main.py                         # FastAPI app + lifespan
│   ├── core/
│   │   ├── config.py                   # pydantic-settings (provider + DB config)
│   │   ├── database.py                 # Motor client (MongoDB)
│   │   ├── mysql_database.py           # aiomysql pool (MySQL)
│   │   └── database_lifecycle.py       # open/close by provider
│   ├── domain/
│   │   ├── entities/                   # Dataclass domain models
│   │   └── ports/                      # Repository Protocols
│   ├── application/services/           # Use cases (list resources)
│   ├── adapters/outbound/
│   │   ├── factory.py                  # Repository factory by provider
│   │   ├── mongo/                      # Motor repositories + mappers
│   │   └── mysql/                      # aiomysql repositories + mappers
│   ├── api/
│   │   ├── dependencies.py             # Service wiring for routes
│   │   └── mappers.py                  # Entity → Pydantic schema
│   ├── models/                         # Pydantic API schemas
│   └── routes/                         # Per-resource routers
├── scripts/mysql_schema.sql            # MySQL DDL
├── tests/                              # pytest (unit + adapter tests)
├── .env.example
└── pyproject.toml
```

## Developer notes

- The lifespan in `app/main.py` calls `open_database_connection()` / `close_database_connection()`, which delegate to MongoDB or MySQL based on `DATABASE_PROVIDER`.
- `app.models.object_id.PyObjectId` integrates BSON `ObjectId` with Pydantic v2 when using MongoDB.
- Repository instances are created per service via `app/adapters/outbound/factory.py` and cached with `@lru_cache` in `app/api/dependencies.py`.
- Ensure `.env` is present and valid for your chosen provider before starting the server.

## Running tests

Tests live under `tests/` and use `pytest` with `pytest-asyncio`. CI (`.github/workflows/tests.yml`) runs against MongoDB on pushes and PRs to `develop`.

```bash
export MONGODB_URI=mongodb://127.0.0.1:27017
export MONGODB_DATABASE=naboo_test
pytest --verbose
```

Optional static checking:

```bash
pyright
```

## Links

- [FastAPI](https://fastapi.tiangolo.com)
- [Motor](https://motor.readthedocs.io/) (async MongoDB)
- [aiomysql](https://aiomysql.readthedocs.io/) (async MySQL)
