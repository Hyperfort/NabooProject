import pytest

from app.core import database, mysql_database


def test_get_db_raises_before_init():
    with pytest.raises(RuntimeError):
        database.get_db()


def test_get_mysql_pool_raises_before_init():
    with pytest.raises(RuntimeError):
        mysql_database.get_mysql_pool()
