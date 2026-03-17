from pydantic import BaseModel

class PokemonSchema(BaseModel): #schema de dados
    name: str
    type: str

    class Config:
        from_attributes = True