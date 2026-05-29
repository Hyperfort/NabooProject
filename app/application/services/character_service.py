from app.domain.entities import CharacterEntity
from app.domain.ports import CharacterRepositoryPort


class CharacterService:
    def __init__(self, repository: CharacterRepositoryPort) -> None:
        self._repository = repository

    async def list(self, limit: int = 100) -> list[CharacterEntity]:
        return await self._repository.list(limit)
