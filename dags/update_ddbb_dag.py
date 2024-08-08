from datetime import datetime, timedelta


from airflow import DAG
from airflow.exceptions import AirflowFailException
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


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


def update_ddbb_task(**kwargs):
    print('yo me cago en el puto airflow')


tarea1 = PythonOperator(
    task_id='update_ddbb_task',
    python_callable=update_ddbb_task,
    dag=dag
)


tarea1