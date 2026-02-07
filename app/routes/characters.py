from app.core.database import get_db
from app.models.character import Character
from fastapi import APIRouter

router = APIRouter()

@router.get("/", response_model=list[Character])
async def list_characters():
    _db = get_db()
    records = await _db["characters"].find().to_list(100)
    return [Character(**record) for record in records]