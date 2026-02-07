from app.repositories.repository import StarWarsRepository


class FactionRepository(StarWarsRepository):
    collection_name = "factions"

    async def list(self, limit: int):
        return await self.collection.find().to_list(limit)
