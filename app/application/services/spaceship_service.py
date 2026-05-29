from app.domain.entities import SpaceshipEntity
from app.domain.ports import SpaceshipRepositoryPort


class SpaceshipService:
    def __init__(self, repository: SpaceshipRepositoryPort) -> None:
        self._repository = repository

    async def list(self, limit: int = 100) -> list[SpaceshipEntity]:
        return await self._repository.list(limit)
