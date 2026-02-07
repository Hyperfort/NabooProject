from app.core.database import get_db


class StarWarsRepository:
    collection_name: str = None

    @property
    def collection(self):
        _db = get_db()
        return _db[self.collection_name]

    def _convert_ids(self, docs: list[dict]) -> list[dict]:
        """Convert MongoDB ObjectId values to strings in a list of documents."""
        for d in docs:
            if "_id" in d:
                d["_id"] = str(d["_id"])
        return docs

    async def list(self, limit: int):
        """Return list of documents from the repository with stringified _id."""
        docs = await self.collection.find().to_list(limit)
        return self._convert_ids(docs)
