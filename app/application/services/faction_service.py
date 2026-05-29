from app.domain.entities import FactionEntity
from app.domain.ports import FactionRepositoryPort


class FactionService:
    def __init__(self, repository: FactionRepositoryPort) -> None:
        self._repository = repository

    async def list(self, limit: int = 100) -> list[FactionEntity]:
        return await self._repository.list(limit)
