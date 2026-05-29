import json

import pytest
from bson import ObjectId

from app.adapters.outbound.factory import create_world_repository
from app.adapters.outbound.mongo.mappers import document_to_world
from app.adapters.outbound.mysql.mappers import row_to_world
from app.core import config


def test_document_to_world_converts_objectid():
    oid = ObjectId()
    entity = document_to_world(
        {
            "_id": oid,
            "name": "Naboo",
            "appearances": ["Ep I"],
            "region": "Mid Rim",
            "sector": "Chommell",
            "affiliation": "Galactic Republic",
        }
    )
    assert entity.id == str(oid)
    assert entity.name == "Naboo"
    assert entity.appearances == ["Ep I"]


def test_row_to_world_parses_json_appearances():
    entity = row_to_world(
        {
            "id": 7,
            "name": "Coruscant",
            "appearances": json.dumps(["Ep I", "Ep II"]),
            "region": "Core Worlds",
            "sector": "Corusca",
            "affiliation": "Galactic Republic",
        }
    )
    assert entity.id == "7"
    assert entity.appearances == ["Ep I", "Ep II"]


def test_factory_uses_mongo_adapter_by_default(monkeypatch):
    monkeypatch.setattr(config.settings, "DATABASE_PROVIDER", "mongodb")
    repo = create_world_repository()
    assert repo.__class__.__name__ == "MongoWorldRepository"


def test_factory_uses_mysql_adapter_when_configured(monkeypatch):
    monkeypatch.setattr(config.settings, "DATABASE_PROVIDER", "mysql")
    repo = create_world_repository()
    assert repo.__class__.__name__ == "MySQLWorldRepository"
