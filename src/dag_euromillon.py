from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def saludar():
    print("Holaaa Airflow")
    
default_args={
    "owner":"airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries":1,
    "retry_delay":timedelta(minutes=5),
    "start_date":datetime(2024,8,20),
}

dag = DAG(
    "simple_greeting",
    description="Un DAG simple para imprimir saludo",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False,
)

saludo_task = PythonOperator(
    task_id="saludar",
    python_callable=saludar,
    dag=dag,
)
saludo_task