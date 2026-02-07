from app.repositories.repository import StarWarsRepository


class FactionRepository(StarWarsRepository):
    collection_name = "factions"
