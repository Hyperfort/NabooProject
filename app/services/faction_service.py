from app.repositories.faction_repository import FactionRepository


class FactionService:
    def __init__(self, repository: FactionRepository | None = None) -> None:
        self.repository = repository or FactionRepository()

    async def list(self, limit: int = 100):
        return await self.repository.list(limit)
