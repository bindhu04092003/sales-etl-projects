
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def sales_task():
    print("Sales ETL Process Started")

with DAG(
    dag_id="sales_etl",
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id="sales_task",
        python_callable=sales_task,
    )
