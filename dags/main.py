from airflow.sdk import dag, task
from datetime import datetime

@dag(
    dag_id="hello_dag",
    start_date=datetime(2026, 3, 17),
    schedule="@hourly",
    catchup=False,
    default_args={"retries": 2},
    tags=["example"],
)
def hello_dag():
    @task
    def hello_task():
        print("Hello World!")

    hello_task()

hello_dag()