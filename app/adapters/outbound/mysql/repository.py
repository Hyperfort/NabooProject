import aiomysql

from app.adapters.outbound.mysql.mappers import (
    row_to_character,
    row_to_faction,
    row_to_spaceship,
    row_to_world,
)
from app.core.config import settings
from app.core.mysql_database import get_mysql_pool
from app.domain.entities import (
    CharacterEntity,
    FactionEntity,
    SpaceshipEntity,
    WorldEntity,
)
from app.domain.ports import (
    CharacterRepositoryPort,
    FactionRepositoryPort,
    SpaceshipRepositoryPort,
    WorldRepositoryPort,
)


async def _fetch_rows(query: str, limit: int) -> list[dict]:
    pool = get_mysql_pool()
    async with pool.acquire() as connection:
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute(query, (limit,))
            rows = await cursor.fetchall()
    return list(rows)


def _table(name: str) -> str:
    return f"{settings.MYSQL_DATABASE}.{name}"


class MySQLCharacterRepository(CharacterRepositoryPort):
    async def list(self, limit: int) -> list[CharacterEntity]:
        rows = await _fetch_rows(
            f"""
            SELECT id, name, appearances, affiliation, homeworld, species
            FROM {_table("characters")}
            LIMIT %s
            """,
            limit,
        )
        return [row_to_character(row) for row in rows]


class MySQLFactionRepository(FactionRepositoryPort):
    async def list(self, limit: int) -> list[FactionEntity]:
        rows = await _fetch_rows(
            f"""
            SELECT id, name, appearances, type, era
            FROM {_table("factions")}
            LIMIT %s
            """,
            limit,
        )
        return [row_to_faction(row) for row in rows]


class MySQLSpaceshipRepository(SpaceshipRepositoryPort):
    async def list(self, limit: int) -> list[SpaceshipEntity]:
        rows = await _fetch_rows(
            f"""
            SELECT id, name, appearances, model, manufacturer, affiliation
            FROM {_table("spaceships")}
            LIMIT %s
            """,
            limit,
        )
        return [row_to_spaceship(row) for row in rows]


class MySQLWorldRepository(WorldRepositoryPort):
    async def list(self, limit: int) -> list[WorldEntity]:
        rows = await _fetch_rows(
            f"""
            SELECT id, name, appearances, region, sector, affiliation
            FROM {_table("worlds")}
            LIMIT %s
            """,
            limit,
        )
        return [row_to_world(row) for row in rows]
