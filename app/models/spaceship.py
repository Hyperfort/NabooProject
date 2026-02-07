from app.models.model import StarWarsModel


class Spaceship(StarWarsModel):
    model: str
    manufacturer: str
    affiliation: str
