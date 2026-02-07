import pytest
from bson import ObjectId

from app.repositories.repository import StarWarsRepository
from app.services.world_service import WorldService
import app.routes.worlds as worlds_module


class DummyRepo(StarWarsRepository):
    collection_name = "dummy"

    def __init__(self):
        # avoid calling parent initialization
        pass

    @property
    def collection(self):
        class C:
            def find(self):
                class F:
                    async def to_list(self, limit):
                        return [
                            {"_id": ObjectId(), "name": "Alpha"},
                            {"name": "NoID"},
                        ]

                return F()

        return C()


@pytest.mark.asyncio
async def test_repo_list_converts_objectids_to_strings():
    repo = DummyRepo()
    docs = await repo.list(10)
    assert isinstance(docs, list)
    assert any("name" in d for d in docs)
    for d in docs:
        if "_id" in d:
            assert isinstance(d["_id"], str)


@pytest.mark.asyncio
async def test_world_service_list_delegates_to_repository():
    repo = DummyRepo()
    service = WorldService(repository=repo)
    docs = await service.list()
    assert isinstance(docs, list)


@pytest.mark.asyncio
async def test_worlds_route_uses_service(monkeypatch):
    repo = DummyRepo()
    service = WorldService(repository=repo)
    monkeypatch.setattr(worlds_module, "_service", service)
    res = await worlds_module.list_worlds()
    assert isinstance(res, list)
