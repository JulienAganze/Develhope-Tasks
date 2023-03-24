from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


default_dag_args = { 
    'start_date': datetime(2023,3,10), 
    'email_on_failure': False, 'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=5),
    'project_id': 1 }

def create_file():
    source_path = "/home/julian/Desktop/DATA_CENTER_1/DATA_LAKE/"
    open(source_path + "dataset_raw.txt", 'w')
# Let us define our DAG
with DAG("FIRST_DAG", schedule_interval = None, default_args = default_dag_args) as dag:

    # Here at this level we define our tasks of the DAG
    task_0 = BashOperator(task_id = 'bash_task', bash_command = "echo 'command executed from Bash Operator' ")
    task_1 = PythonOperator(task_id = 'create_file', python_callable = create_file)
    task_2 = BashOperator(task_id = 'bash_task_move_data', bash_command = " cp /home/julian/Desktop/DATA_CENTER_1/DATA_LAKE/dataset_raw.txt  /home/julian/Desktop/DATA_CENTER_1/CLEAN_DATA")
    task_3 = BashOperator(task_id = 'bash_task_remove_data', bash_command = " rm /home/julian/Desktop/DATA_CENTER_1/DATA_LAKE/dataset_raw.txt")

    # Let us now write dependencies between tasks
    task_0 >> task_1 >> task_2 >> task_3