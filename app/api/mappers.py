from app.domain.entities import (
    CharacterEntity,
    FactionEntity,
    SpaceshipEntity,
    WorldEntity,
)
from app.models.character import Character
from app.models.faction import Faction
from app.models.spaceship import Spaceship
from app.models.world import World


def character_to_schema(entity: CharacterEntity) -> Character:
    return Character(
        _id=entity.id,
        name=entity.name,
        appearances=entity.appearances,
        affiliation=entity.affiliation,
        homeworld=entity.homeworld,
        species=entity.species,
    )


def faction_to_schema(entity: FactionEntity) -> Faction:
    return Faction(
        _id=entity.id,
        name=entity.name,
        appearances=entity.appearances,
        type=entity.type,
        era=entity.era,
    )


def spaceship_to_schema(entity: SpaceshipEntity) -> Spaceship:
    return Spaceship(
        _id=entity.id,
        name=entity.name,
        appearances=entity.appearances,
        model=entity.model,
        manufacturer=entity.manufacturer,
        affiliation=entity.affiliation,
    )


def world_to_schema(entity: WorldEntity) -> World:
    return World(
        _id=entity.id,
        name=entity.name,
        appearances=entity.appearances,
        region=entity.region,
        sector=entity.sector,
        affiliation=entity.affiliation,
    )
