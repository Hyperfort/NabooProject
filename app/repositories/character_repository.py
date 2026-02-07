from app.repositories.repository import StarWarsRepository


class CharacterRepository(StarWarsRepository):
    collection_name = "characters"

    async def list(self):
        return await self.collection.find().to_list(100)
