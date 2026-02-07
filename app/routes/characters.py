from app.core.database import get_db
from app.models.character import Character
from app.repositories.character_repository import CharacterRepository
from fastapi import APIRouter

router = APIRouter()
_repository = CharacterRepository()

@router.get("/", response_model=list[Character])
async def list_characters():
    return await _repository.list()
