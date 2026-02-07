from app.models.model import StarWarsModel


class World(StarWarsModel):
    region: str
    sector: str
    affiliation: str
