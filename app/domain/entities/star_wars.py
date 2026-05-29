from dataclasses import dataclass, field


@dataclass
class StarWarsEntity:
    id: str
    name: str
    appearances: list[str] = field(default_factory=list)


@dataclass
class CharacterEntity(StarWarsEntity):
    affiliation: str = ""
    homeworld: str = ""
    species: str = ""


@dataclass
class FactionEntity(StarWarsEntity):
    type: str = ""
    era: list[str] = field(default_factory=list)


@dataclass
class SpaceshipEntity(StarWarsEntity):
    model: str = ""
    manufacturer: str = ""
    affiliation: str = ""


@dataclass
class WorldEntity(StarWarsEntity):
    region: str = ""
    sector: str = ""
    affiliation: str = ""
