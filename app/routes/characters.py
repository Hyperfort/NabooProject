from app.api.dependencies import get_character_service
from app.api.mappers import character_to_schema
from app.application.services.character_service import CharacterService
from app.models.character import Character
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("", response_model=list[Character])
async def list_characters(
    service: CharacterService = Depends(get_character_service),
):
    entities = await service.list()
    return [character_to_schema(entity) for entity in entities]
