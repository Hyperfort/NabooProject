from app.api.dependencies import get_world_service
from app.api.mappers import world_to_schema
from app.application.services.world_service import WorldService
from app.models.world import World
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("", response_model=list[World])
async def list_worlds(
    service: WorldService = Depends(get_world_service),
):
    entities = await service.list()
    return [world_to_schema(entity) for entity in entities]
