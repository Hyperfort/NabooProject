from app.domain.entities import WorldEntity
from app.domain.ports import WorldRepositoryPort


class WorldService:
    def __init__(self, repository: WorldRepositoryPort) -> None:
        self._repository = repository

    async def list(self, limit: int = 100) -> list[WorldEntity]:
        return await self._repository.list(limit)
