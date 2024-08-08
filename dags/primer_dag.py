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
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}


dag = DAG(
    "DAG Tutorial",
    description="DAG Tutorial",
    default_args=dag_args,
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
    params={"commit": "000000"}
)


def tarea0_func(**kwargs):
    conf = kwargs['dag_run'].conf


    if "commit" in conf and conf["commit"]=="1":
       raise AirflowFailException("Hoy no desplegamos porque no me gusta el commit 1!")


    return { "ok": 1 }


def tarea2_func(**kwargs):
    xcom_value = kwargs['ti'].xcom_pull(task_ids='tarea0')


    print( "Hola" )
    print( xcom_value )


    return { "ok": 2 }


tarea0 = PythonOperator(
    task_id='tarea0',
    python_callable=tarea0_func,
    dag=dag
)


tarea1 = BashOperator(
    task_id="print_date",
    bash_command='echo "La fecha es $(date)"',
    dag=dag
)


tarea2 = PythonOperator(
    task_id='tarea2',
    python_callable=tarea2_func,
    dag=dag
)


tarea0 >> [ tarea1, tarea2 ]
