from functools import lru_cache

from app.adapters.outbound.factory import (
    create_character_repository,
    create_faction_repository,
    create_spaceship_repository,
    create_world_repository,
)
from app.application.services.character_service import CharacterService
from app.application.services.faction_service import FactionService
from app.application.services.spaceship_service import SpaceshipService
from app.application.services.world_service import WorldService


@lru_cache
def get_character_service() -> CharacterService:
    return CharacterService(create_character_repository())


@lru_cache
def get_faction_service() -> FactionService:
    return FactionService(create_faction_repository())


@lru_cache
def get_spaceship_service() -> SpaceshipService:
    return SpaceshipService(create_spaceship_repository())


@lru_cache
def get_world_service() -> WorldService:
    return WorldService(create_world_repository())
