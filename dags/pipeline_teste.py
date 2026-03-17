from time import sleep
from loguru import logger
from datetime import datetime
from airflow.sdk import dag, task

@dag(
    dag_id="pipeline_teste",
    start_date=datetime(2026, 3, 17),
    schedule="@hourly",
    catchup=False,
    default_args={"retries": 2},
    tags=["example"],
)

def pipeline_teste():

    @task
    def primeira_atividade():
        logger.info("minha primeira atividade!")
        sleep(2)

    @task
    def segunda_atividade():
        logger.info("minha segunda atividade")
        sleep(2)

    @task
    def terceira_atividade():
        logger.info("minha terceira atividade")
        sleep(2)
        logger.success("Pipeline finalizado(no airflow!)")

    primeira_atividade() >> segunda_atividade() >> terceira_atividade()

pipeline_teste()