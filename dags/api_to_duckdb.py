from airflow.sdk import task, dag
from include.controller import gerar_numero_aleatorio, fetch_pokemon_data, add_pokemon_to_db
from datetime import datetime

@dag(
    dag_id='pokemon_dag',
    description='pipeline para coletar dados de pokemons da api',
    start_date=datetime(2026,3,18),
    schedule='@hourly',
    catchup=False,
    default_args={"retries": 2},
    tags=["pokemon", "example"],
)

def api_duckdb():

    @task
    def extract_pokemon():
        pokemon_id = gerar_numero_aleatorio()
        return fetch_pokemon_data(pokemon_id)

    @task
    def load_pokemon(pokemon_data):
        if pokemon_data is None:
            raise ValueError("Falha ao extrair dados do Pokemon da API")
        add_pokemon_to_db(pokemon_data)

    
    pokemon_data = extract_pokemon()
    load_pokemon(pokemon_data)

api_duckdb()
        