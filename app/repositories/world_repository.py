from app.repositories.repository import StarWarsRepository


class WorldRepository(StarWarsRepository):
    collection_name = "worlds"
