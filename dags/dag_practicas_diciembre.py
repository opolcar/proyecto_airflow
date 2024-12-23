from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

#primera tarea de saludar
def hola_mundo():
    print('Hola, estamos usando el primer DAG de saludar')
    
    
#definir el DAG
default_args={ #Es un diccionario que define parámetros comunes para todas las tareas del DAG.
    'owner':'airflow', #Especifica quién es responsable del DAG (útil para identificar al dueño en equipos grandes).
    'depends_on_past': False, #Si es True, una tarea esperará a que su ejecución anterior haya terminado con éxito. En este caso, False significa que cada ejecución es independiente.
    'retries':1,
}

with DAG( #con DAG: Creamos una instancia de un DAG.
    dag_id='primer_dag_de_practicas', #Es el nombre único de tu DAG
    default_args=default_args, #Asocia los argumentos comunes a este DAG
    description="Primer DAG para las prácticas de diciembre",
    schedule='@daily',
    start_date=datetime(2024,12,19), 
    catchup=False #Si es True, Airflow ejecutará todas las fechas pendientes desde la start_date. Aquí usamos False para evitar ejecuciones pasadas.
) as dag:
    
    # Crear una tarea con Python
    tarea_hola_mundo=PythonOperator(
        task_id="Tarea_saludar_diciembre",
        python_callable=hola_mundo,
    )
    
# aquí se definirían las dependencias aunque en este caso solo hay una 

tarea_hola_mundo