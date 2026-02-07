# NabooProject

An unofficial Star Wars‑inspired API that provides structured data about characters, factions, spaceships, and worlds—built for developers who want a simple, modern way to explore a galaxy’s worth of information.

## Quick Start

### Start the development server

```bash
uvicorn app.main:app --reload
```

Visit http://localhost:8000

## Project Structure

NabooProject/
│
├── app/
│   ├── main.py                  # FastAPI app + lifespan (MongoDB init)
│   │
│   ├── core/
│   │   ├── config.py            # Settings (Pydantic v2)
│   │   └── database.py          # MongoDB connection + get_db()
│   │
│   ├── models/                  # Pydantic Schemas
│   │
│   ├── routes/                  # HTTP Layer
│   │
│   └── __init__.py
│
├── .env                         # MongoDB URI, DB name, secrets
├── pyproject.toml               # Dependencies (uv-managed)
└── README.md

## Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [FastAPI Cloud](https://fastapicloud.com)
