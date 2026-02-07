from app.repositories.repository import StarWarsRepository


class SpaceshipRepository(StarWarsRepository):
    collection_name = "spaceships"
