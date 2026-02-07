from app.repositories.world_repository import WorldRepository


class WorldService:
    def __init__(self, repository: WorldRepository | None = None) -> None:
        self.repository = repository or WorldRepository()

    async def list(self, limit: int = 100):
        return await self.repository.list(limit)
