from app.repositories.repository import StarWarsRepository


class CharacterRepository(StarWarsRepository):
    collection_name = "characters"

    async def list(self, limit: int):
        return await self.collection.find().to_list(limit)
