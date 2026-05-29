import json
from typing import Any

from app.domain.entities import (
    CharacterEntity,
    FactionEntity,
    SpaceshipEntity,
    WorldEntity,
)


def _document_id(doc: dict[str, Any]) -> str:
    if "_id" in doc:
        return str(doc["_id"])
    if "id" in doc:
        return str(doc["id"])
    return ""


def _parse_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
            if isinstance(parsed, list):
                return [str(item) for item in parsed]
        except json.JSONDecodeError:
            return [value]
    return [str(value)]


def document_to_character(doc: dict[str, Any]) -> CharacterEntity:
    return CharacterEntity(
        id=_document_id(doc),
        name=doc["name"],
        appearances=_parse_list(doc.get("appearances")),
        affiliation=doc.get("affiliation", ""),
        homeworld=doc.get("homeworld", ""),
        species=doc.get("species", ""),
    )


def document_to_faction(doc: dict[str, Any]) -> FactionEntity:
    return FactionEntity(
        id=_document_id(doc),
        name=doc["name"],
        appearances=_parse_list(doc.get("appearances")),
        type=doc.get("type", ""),
        era=_parse_list(doc.get("era")),
    )


def document_to_spaceship(doc: dict[str, Any]) -> SpaceshipEntity:
    return SpaceshipEntity(
        id=_document_id(doc),
        name=doc["name"],
        appearances=_parse_list(doc.get("appearances")),
        model=doc.get("model", ""),
        manufacturer=doc.get("manufacturer", ""),
        affiliation=doc.get("affiliation", ""),
    )


def document_to_world(doc: dict[str, Any]) -> WorldEntity:
    return WorldEntity(
        id=_document_id(doc),
        name=doc["name"],
        appearances=_parse_list(doc.get("appearances")),
        region=doc.get("region", ""),
        sector=doc.get("sector", ""),
        affiliation=doc.get("affiliation", ""),
    )
