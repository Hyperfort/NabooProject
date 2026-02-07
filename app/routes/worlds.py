from app.core.database import get_db
from app.models.world import World
from fastapi import APIRouter

router = APIRouter()

@router.get("/", response_model=list[World])
async def list_worlds():
    _db = get_db()
    records = await _db["worlds"].find().to_list(100)
    return [World(**record) for record in records]