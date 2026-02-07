from app.core.database import get_db
from app.models.spaceship import Spaceship
from fastapi import APIRouter

router = APIRouter()

@router.get("/", response_model=list[Spaceship])
async def list_spaceships():
    _db = get_db()
    records = await _db["spaceships"].find().to_list(100)
    return [Spaceship(**record) for record in records]
