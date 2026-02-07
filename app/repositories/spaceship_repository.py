from app.repositories.repository import StarWarsRepository


class SpaceshipRepository(StarWarsRepository):
    collection_name = "spaceships"

    async def list(self, limit: int):
        return await self.collection.find().to_list(limit)
