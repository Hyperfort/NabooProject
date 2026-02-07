from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

client: AsyncIOMotorClient | None = None
_db = None


async def open_mongodb_connection():
    global client, _db
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    _db = client[settings.MONGODB_DATABASE]


async def close_mongodb_connection():
    global client
    if client:
        client.close()


def get_db():
    if _db is None:
        raise RuntimeError("Database not initialized. Did lifespan run?")
    return _db
