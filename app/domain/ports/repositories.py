from typing import Protocol

from app.domain.entities import (
    CharacterEntity,
    FactionEntity,
    SpaceshipEntity,
    WorldEntity,
)


class CharacterRepositoryPort(Protocol):
    async def list(self, limit: int) -> list[CharacterEntity]: ...


class FactionRepositoryPort(Protocol):
    async def list(self, limit: int) -> list[FactionEntity]: ...


class SpaceshipRepositoryPort(Protocol):
    async def list(self, limit: int) -> list[SpaceshipEntity]: ...


class WorldRepositoryPort(Protocol):
    async def list(self, limit: int) -> list[WorldEntity]: ...
