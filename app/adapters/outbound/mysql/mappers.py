import json
from typing import Any

from app.domain.entities import (
    CharacterEntity,
    FactionEntity,
    SpaceshipEntity,
    WorldEntity,
)


def _row_id(row: dict[str, Any]) -> str:
    return str(row["id"])


def _parse_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, (bytes, bytearray)):
        value = value.decode()
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
            if isinstance(parsed, list):
                return [str(item) for item in parsed]
        except json.JSONDecodeError:
            return [value]
    return [str(value)]


def row_to_character(row: dict[str, Any]) -> CharacterEntity:
    return CharacterEntity(
        id=_row_id(row),
        name=row["name"],
        appearances=_parse_list(row.get("appearances")),
        affiliation=row.get("affiliation", "") or "",
        homeworld=row.get("homeworld", "") or "",
        species=row.get("species", "") or "",
    )


def row_to_faction(row: dict[str, Any]) -> FactionEntity:
    return FactionEntity(
        id=_row_id(row),
        name=row["name"],
        appearances=_parse_list(row.get("appearances")),
        type=row.get("type", "") or "",
        era=_parse_list(row.get("era")),
    )


def row_to_spaceship(row: dict[str, Any]) -> SpaceshipEntity:
    return SpaceshipEntity(
        id=_row_id(row),
        name=row["name"],
        appearances=_parse_list(row.get("appearances")),
        model=row.get("model", "") or "",
        manufacturer=row.get("manufacturer", "") or "",
        affiliation=row.get("affiliation", "") or "",
    )


def row_to_world(row: dict[str, Any]) -> WorldEntity:
    return WorldEntity(
        id=_row_id(row),
        name=row["name"],
        appearances=_parse_list(row.get("appearances")),
        region=row.get("region", "") or "",
        sector=row.get("sector", "") or "",
        affiliation=row.get("affiliation", "") or "",
    )
