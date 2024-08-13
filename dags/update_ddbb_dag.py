from datetime import datetime, timedelta


from airflow import DAG
from airflow.exceptions import AirflowFailException
from airflow.operators.python import PythonOperator
from src.update_ddbb_task import execute

dag_args = {
    "depends_on_past": False,
    "email": ["test@test.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5)
}


dag = DAG(
    "Update_BBDD",
    description="Dag de actualización de base de datos",
    default_args=dag_args,
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["ETL"],
    params={"param1": "param1"}
)


tarea1 = PythonOperator(
    task_id='update_ddbb_task',
    python_callable=execute,
    op_kwargs={'database_name': 'proyecto_airflow/tienda_online.db'},
    dag=dag
)


tarea1