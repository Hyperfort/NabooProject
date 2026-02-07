from app.core.database import get_db
from app.models.faction import Faction
from fastapi import APIRouter

router = APIRouter()

@router.get("/", response_model=list[Faction])
async def list_factions():
    _db = get_db()
    records = await _db["factions"].find().to_list(100)
    return [Faction(**record) for record in records]