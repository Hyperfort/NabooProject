from pydantic import BaseModel, ConfigDict, Field


class StarWarsModel(BaseModel):
    id: str = Field(alias="_id")
    name: str
    appearances: list[str]

    model_config = ConfigDict(populate_by_name=True)
