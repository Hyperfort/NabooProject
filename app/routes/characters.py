from app.core.database import get_db
from app.models.character import Character
from app.services.character_service import CharacterService
from fastapi import APIRouter

router = APIRouter()
_service = CharacterService()


@router.get("", response_model=list[Character])
async def list_characters():
    return await _service.list()
