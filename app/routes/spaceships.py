from app.api.dependencies import get_spaceship_service
from app.api.mappers import spaceship_to_schema
from app.application.services.spaceship_service import SpaceshipService
from app.models.spaceship import Spaceship
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("", response_model=list[Spaceship])
async def list_spaceships(
    service: SpaceshipService = Depends(get_spaceship_service),
):
    entities = await service.list()
    return [spaceship_to_schema(entity) for entity in entities]
