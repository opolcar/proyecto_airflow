from datetime import datetime, timedelta
from airflow import DAG
from airflow.exceptions import AirflowFailException
from airflow.operators.python import PythonOperator
from src.consultar_euromillones_task import  saludar, extraer_numeros_premiados
    
default_args={
    "owner":"airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries":1,
    "retry_delay":timedelta(minutes=5),
    "start_date":datetime(2024,8,20),
}

dag = DAG(
    "saludar_y_consultar_euromillones",
    description="Un DAG simple para imprimir saludo y consultar euromillones",
    default_args=default_args,
    schedule="0 1 * * *", 
    catchup=False,
)

saludo_task = PythonOperator(
    task_id="saludar",
    python_callable=saludar,
    dag=dag,
)

consultar_euromillones_task=PythonOperator(
    task_id="consultar_numeros_premiados",
    python_callable=extraer_numeros_premiados,
    dag=dag,
)


saludo_task >> consultar_euromillones_task