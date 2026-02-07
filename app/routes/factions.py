from app.core.database import get_db
from app.models.faction import Faction
from app.repositories.faction_repository import FactionRepository
from fastapi import APIRouter

router = APIRouter()
_repository = FactionRepository()

@router.get("/", response_model=list[Faction])
async def list_factions():
    return await _repository.list()
