from app.models.model import StarWarsModel

class Faction(StarWarsModel):
    type: str
    era: list[str]
