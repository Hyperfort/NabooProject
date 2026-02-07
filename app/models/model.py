from app.models.object_id import PyObjectId
from pydantic import BaseModel, ConfigDict, Field


class StarWarsModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    appearances: list[str]

    model_config = ConfigDict(populate_by_name=True, json_encoders={PyObjectId: str})
