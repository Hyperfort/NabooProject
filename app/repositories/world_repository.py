from app.repositories.repository import StarWarsRepository


class WorldRepository(StarWarsRepository):
    collection_name = "worlds"

    async def list(self):
        return await self.collection.find().to_list(100)
