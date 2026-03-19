import requests
from random import randint, choice
from .db import SessionLocal, engine, Base
from .models import Pokemon
from typing import Optional

Base.metadata.create_all(bind=engine)

def gerar_numero_aleatorio():
    with SessionLocal() as db:
        # Encontrar IDs já usados
        usados = db.query(Pokemon.id).all()
        ids_usados = {p.id for p in usados}
        
        # Sortear de IDs disponíveis
        disponíveis = [i for i in range(1, 351) if i not in ids_usados]
        
        if not disponíveis:
            # Se todos foram usados, reseta
            return randint(1, 350)
        
        return choice(disponíveis)

def fetch_pokemon_data(pokemon_id: int) -> Optional[dict]:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    if response.status_code == 200:
        data = response.json()
        types = ', '.join(type['type']['name'] for type in data['types'])
        return {"id": pokemon_id, "name": data['name'], "type": types}
    else:
        return None
    
def add_pokemon_to_db(pokemon_data: dict) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(
            id=pokemon_data["id"],
            name=pokemon_data["name"],
            type=pokemon_data["type"],
        )
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon