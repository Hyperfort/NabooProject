from app.api.dependencies import get_faction_service
from app.api.mappers import faction_to_schema
from app.application.services.faction_service import FactionService
from app.models.faction import Faction
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("", response_model=list[Faction])
async def list_factions(
    service: FactionService = Depends(get_faction_service),
):
    entities = await service.list()
    return [faction_to_schema(entity) for entity in entities]
