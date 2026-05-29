from app.core.config import settings
from app.core.database import close_mongodb_connection, open_mongodb_connection
from app.core.mysql_database import close_mysql_connection, open_mysql_connection


async def open_database_connection() -> None:
    if settings.DATABASE_PROVIDER == "mysql":
        await open_mysql_connection()
        return
    await open_mongodb_connection()


async def close_database_connection() -> None:
    if settings.DATABASE_PROVIDER == "mysql":
        await close_mysql_connection()
        return
    await close_mongodb_connection()
