import aiomysql

from app.core.config import settings

_pool: aiomysql.Pool | None = None


async def open_mysql_connection() -> None:
    global _pool
    _pool = await aiomysql.create_pool(
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT,
        user=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        autocommit=True,
    )


async def close_mysql_connection() -> None:
    global _pool
    if _pool is not None:
        _pool.close()
        await _pool.wait_closed()
        _pool = None


def get_mysql_pool() -> aiomysql.Pool:
    if _pool is None:
        raise RuntimeError("MySQL pool not initialized. Did lifespan run?")
    return _pool
