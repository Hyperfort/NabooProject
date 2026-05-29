from app.adapters.outbound.mongo.mappers import (
    document_to_character,
    document_to_faction,
    document_to_spaceship,
    document_to_world,
)
from app.core.database import get_db
from app.domain.entities import (
    CharacterEntity,
    FactionEntity,
    SpaceshipEntity,
    WorldEntity,
)
from app.domain.ports import (
    CharacterRepositoryPort,
    FactionRepositoryPort,
    SpaceshipRepositoryPort,
    WorldRepositoryPort,
)


class MongoCharacterRepository(CharacterRepositoryPort):
    collection_name = "characters"

    @property
    def collection(self):
        return get_db()[self.collection_name]

    async def list(self, limit: int) -> list[CharacterEntity]:
        docs = await self.collection.find().to_list(limit)
        return [document_to_character(doc) for doc in docs]


class MongoFactionRepository(FactionRepositoryPort):
    collection_name = "factions"

    @property
    def collection(self):
        return get_db()[self.collection_name]

    async def list(self, limit: int) -> list[FactionEntity]:
        docs = await self.collection.find().to_list(limit)
        return [document_to_faction(doc) for doc in docs]


class MongoSpaceshipRepository(SpaceshipRepositoryPort):
    collection_name = "spaceships"

    @property
    def collection(self):
        return get_db()[self.collection_name]

    async def list(self, limit: int) -> list[SpaceshipEntity]:
        docs = await self.collection.find().to_list(limit)
        return [document_to_spaceship(doc) for doc in docs]


class MongoWorldRepository(WorldRepositoryPort):
    collection_name = "worlds"

    @property
    def collection(self):
        return get_db()[self.collection_name]

    async def list(self, limit: int) -> list[WorldEntity]:
        docs = await self.collection.find().to_list(limit)
        return [document_to_world(doc) for doc in docs]
