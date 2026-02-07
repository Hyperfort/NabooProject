from app.models.model import StarWarsModel


class Character(StarWarsModel):
    affiliation: str
    homeworld: str
    species: str
