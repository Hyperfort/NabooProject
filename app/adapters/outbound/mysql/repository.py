import aiomysql

from app.adapters.outbound.mysql.mappers import (
    row_to_character,
    row_to_faction,
    row_to_spaceship,
    row_to_world,
)
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


class MySQLCharacterRepository(CharacterRepositoryPort):
    async def list(self, limit: int) -> list[CharacterEntity]:
        rows = await _fetch_rows(
            """
            SELECT id, name, appearances, affiliation, homeworld, species
            FROM characters
            LIMIT %s
            """,
            limit,
        )
        return [row_to_character(row) for row in rows]


class MySQLFactionRepository(FactionRepositoryPort):
    async def list(self, limit: int) -> list[FactionEntity]:
        rows = await _fetch_rows(
            """
            SELECT id, name, appearances, type, era
            FROM factions
            LIMIT %s
            """,
            limit,
        )
        return [row_to_faction(row) for row in rows]


class MySQLSpaceshipRepository(SpaceshipRepositoryPort):
    async def list(self, limit: int) -> list[SpaceshipEntity]:
        rows = await _fetch_rows(
            """
            SELECT id, name, appearances, model, manufacturer, affiliation
            FROM spaceships
            LIMIT %s
            """,
            limit,
        )
        return [row_to_spaceship(row) for row in rows]


class MySQLWorldRepository(WorldRepositoryPort):
    async def list(self, limit: int) -> list[WorldEntity]:
        rows = await _fetch_rows(
            """
            SELECT id, name, appearances, region, sector, affiliation
            FROM worlds
            LIMIT %s
            """,
            limit,
        )
        return [row_to_world(row) for row in rows]
