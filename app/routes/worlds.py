from app.core.database import get_db
from app.models.world import World
from app.services.world_service import WorldService
from fastapi import APIRouter

router = APIRouter()
_service = WorldService()


@router.get("", response_model=list[World])
async def list_worlds():
    return await _service.list()
