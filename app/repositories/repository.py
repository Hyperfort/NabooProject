from app.core.database import get_db

class StarWarsRepository:
    collection_name: str = None

    @property
    def collection(self):
        _db = get_db()
        return _db[self.collection_name]
