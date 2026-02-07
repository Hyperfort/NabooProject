from app.core.database import get_db
from app.models.spaceship import Spaceship
from fastapi import APIRouter

from app.repositories.spaceship_repository import SpaceshipRepository

router = APIRouter()
_repository = SpaceshipRepository()

@router.get("/", response_model=list[Spaceship])
async def list_spaceships():
    return await _repository.list()
