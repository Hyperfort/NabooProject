from typing import Literal, overload

from app.adapters.outbound.mongo import (
    MongoCharacterRepository,
    MongoFactionRepository,
    MongoSpaceshipRepository,
    MongoWorldRepository,
)
from app.adapters.outbound.mysql import (
    MySQLCharacterRepository,
    MySQLFactionRepository,
    MySQLSpaceshipRepository,
    MySQLWorldRepository,
)
from app.core.config import settings
from app.domain.ports import (
    CharacterRepositoryPort,
    FactionRepositoryPort,
    SpaceshipRepositoryPort,
    WorldRepositoryPort,
)

DatabaseProvider = Literal["mongodb", "mysql"]


@overload
def _resolve(
    provider: DatabaseProvider,
    mongo_cls: type[CharacterRepositoryPort],
    mysql_cls: type[CharacterRepositoryPort],
) -> CharacterRepositoryPort: ...


@overload
def _resolve(
    provider: DatabaseProvider,
    mongo_cls: type[FactionRepositoryPort],
    mysql_cls: type[FactionRepositoryPort],
) -> FactionRepositoryPort: ...


@overload
def _resolve(
    provider: DatabaseProvider,
    mongo_cls: type[SpaceshipRepositoryPort],
    mysql_cls: type[SpaceshipRepositoryPort],
) -> SpaceshipRepositoryPort: ...


@overload
def _resolve(
    provider: DatabaseProvider,
    mongo_cls: type[WorldRepositoryPort],
    mysql_cls: type[WorldRepositoryPort],
) -> WorldRepositoryPort: ...


def _resolve(
    provider: DatabaseProvider,
    mongo_cls: type,
    mysql_cls: type,
):
    if provider == "mysql":
        return mysql_cls()
    return mongo_cls()


def create_character_repository() -> CharacterRepositoryPort:
    return _resolve(
        settings.DATABASE_PROVIDER,
        MongoCharacterRepository,
        MySQLCharacterRepository,
    )


def create_faction_repository() -> FactionRepositoryPort:
    return _resolve(
        settings.DATABASE_PROVIDER,
        MongoFactionRepository,
        MySQLFactionRepository,
    )


def create_spaceship_repository() -> SpaceshipRepositoryPort:
    return _resolve(
        settings.DATABASE_PROVIDER,
        MongoSpaceshipRepository,
        MySQLSpaceshipRepository,
    )


def create_world_repository() -> WorldRepositoryPort:
    return _resolve(
        settings.DATABASE_PROVIDER,
        MongoWorldRepository,
        MySQLWorldRepository,
    )
