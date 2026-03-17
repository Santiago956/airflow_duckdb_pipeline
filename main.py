from airflow.sdk import dag, task
from datetime import datetime

@dag
def hello_dag(dag_id="hello_dag",
              start_date=datetime(2026,3,17),
              schedule_interval='@hourly',
              catchup=False):
    @task
    def hello_task():
        print("Hello World!")

    task()

