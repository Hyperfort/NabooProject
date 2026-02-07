from app.core.database import close_mongodb_connection, open_mongodb_connection
from app.routes import characters, factions, spaceships, worlds
from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await open_mongodb_connection()
    yield
    # Shutdown
    await close_mongodb_connection()


openapi_tags = [
    {
        "name": "Characters",
        "description": "Operations to list and retrieve characters.",
    },
    {"name": "Factions", "description": "Operations to list and retrieve factions."},
    {
        "name": "Spaceships",
        "description": "Operations to list and retrieve spaceships.",
    },
    {"name": "Worlds", "description": "Operations to list and retrieve worlds."},
]

app = FastAPI(
    title="Naboo Star Wars API",
    description="A simple FastAPI service exposing Star Wars resources: Characters, Factions, Spaceships and Worlds.",
    version="0.1.0",
    contact={"name": "Naboo Project", "email": "dev@naboo.dev"},
    license_info={"name": "MIT"},
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    openapi_tags=openapi_tags,
)

app.include_router(characters.router, prefix="/characters", tags=["Characters"])
app.include_router(factions.router, prefix="/factions", tags=["Factions"])
app.include_router(spaceships.router, prefix="/spaceships", tags=["Spaceships"])
app.include_router(worlds.router, prefix="/worlds", tags=["Worlds"])


@app.get("/health", tags=["Health"])
async def main():
    return {"status": "ok"}
