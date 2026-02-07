from app.core.database import get_db
from app.models.faction import Faction
from app.services.faction_service import FactionService
from fastapi import APIRouter

router = APIRouter()
_service = FactionService()


@router.get("/", response_model=list[Faction])
async def list_factions():
    return await _service.list()
