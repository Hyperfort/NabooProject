from app.core.database import get_db
from app.models.spaceship import Spaceship
from app.services.spaceship_service import SpaceshipService
from fastapi import APIRouter

router = APIRouter()
_service = SpaceshipService()


@router.get("/", response_model=list[Spaceship])
async def list_spaceships():
    return await _service.list()
