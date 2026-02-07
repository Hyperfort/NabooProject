import pytest

from app.core import database


def test_get_db_raises_before_init():
    # Ensure database.get_db raises if the DB has not been initialized
    with pytest.raises(RuntimeError):
        database.get_db()
