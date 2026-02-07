from app.repositories.repository import StarWarsRepository


class CharacterRepository(StarWarsRepository):
    collection_name = "characters"
