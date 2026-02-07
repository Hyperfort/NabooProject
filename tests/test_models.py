import pytest
from bson import ObjectId

from app.models.object_id import PyObjectId
from app.models.model import StarWarsModel


def test_pyobjectid_validate_with_objectid():
    oid = ObjectId()
    assert PyObjectId.validate(oid) is oid


def test_pyobjectid_validate_with_valid_str():
    oid = ObjectId()
    res = PyObjectId.validate(str(oid))
    assert isinstance(res, ObjectId)
    assert res == oid


def test_pyobjectid_validate_invalid():
    with pytest.raises(ValueError):
        PyObjectId.validate("not-an-oid")


def test_starwarsmodel_json_encodes_id_as_string():
    m = StarWarsModel(name="Luke", appearances=["A New Hope"])
    j = m.model_dump_json()
    assert str(m.id) in j
