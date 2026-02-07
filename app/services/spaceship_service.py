from app.repositories.spaceship_repository import SpaceshipRepository


class SpaceshipService:
    def __init__(self, repository: SpaceshipRepository | None = None) -> None:
        self.repository = repository or SpaceshipRepository()

    async def list(self, limit: int = 100):
        return await self.repository.list(limit)
