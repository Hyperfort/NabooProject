import pytest
from bson import ObjectId

from app.api.mappers import world_to_schema
from app.application.services.world_service import WorldService
from app.domain.entities import WorldEntity
from app.routes import worlds as worlds_module


class InMemoryWorldRepository:
    async def list(self, limit: int) -> list[WorldEntity]:
        return [
            WorldEntity(
                id=str(ObjectId()),
                name="Alpha",
                appearances=["Ep IV"],
                region="Outer Rim",
                sector="Test",
                affiliation="Independent",
            ),
            WorldEntity(
                id="42",
                name="NoID",
                appearances=[],
                region="Core",
                sector="Test",
                affiliation="Republic",
            ),
        ][:limit]


@pytest.mark.asyncio
async def test_world_service_list_returns_entities():
    service = WorldService(InMemoryWorldRepository())
    entities = await service.list(10)
    assert len(entities) == 2
    assert entities[0].name == "Alpha"
    assert entities[1].id == "42"


@pytest.mark.asyncio
async def test_world_to_schema_maps_entity_fields():
    entity = WorldEntity(
        id="1",
        name="Tatooine",
        appearances=["Ep IV"],
        region="Outer Rim",
        sector="Arkanis",
        affiliation="Hutt Cartel",
    )
    schema = world_to_schema(entity)
    assert schema.id == "1"
    assert schema.name == "Tatooine"


@pytest.mark.asyncio
async def test_worlds_route_uses_service(monkeypatch):
    service = WorldService(InMemoryWorldRepository())
    monkeypatch.setattr(worlds_module, "get_world_service", lambda: service)
    res = await worlds_module.list_worlds(service=service)
    assert len(res) == 2
    assert res[0].name == "Alpha"
