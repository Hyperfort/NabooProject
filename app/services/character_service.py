from app.repositories.character_repository import CharacterRepository


class CharacterService:
    def __init__(self, repository: CharacterRepository | None = None) -> None:
        self.repository = repository or CharacterRepository()

    async def list(self, limit: int = 100):
        return await self.repository.list(limit)
