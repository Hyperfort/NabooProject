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


app = FastAPI(lifespan=lifespan)

app.include_router(characters.router, prefix="/characters", tags=["Characters"])
app.include_router(factions.router, prefix="/factions", tags=["Factions"])
app.include_router(spaceships.router, prefix="/spaceships", tags=["Spaceships"])
app.include_router(worlds.router, prefix="/worlds", tags=["Worlds"])


@app.get("/health")
async def main():
    return {"status": "ok"}
