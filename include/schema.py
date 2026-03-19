from pydantic import BaseModel
from typing import Optional

class PokemonSchema(BaseModel): #schema de dados
    name: str
    type: str
    id: Optional[str] = None

    class Config:
        from_attributes = True