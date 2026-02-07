from app.core.database import get_db
from app.models.world import World
from fastapi import APIRouter

from app.repositories.world_repository import WorldRepository

router = APIRouter()
_repository = WorldRepository()

@router.get("/", response_model=list[World])
async def list_worlds():
    return await _repository.list()
