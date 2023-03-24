from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_dag_args = { 
    'start_date': datetime(2023,3,10), 
    'email_on_failure': False, 'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=5),
    'project_id': 1 }

def current_datetime():
    print("The current date and time:", datetime.now())


#Defining our dag
with DAG('date_time_printer_dag', schedule_interval = '@daily', catchup=False, default_args = default_dag_args) as dag_python:
    #let us define the task now 
    task_0 = PythonOperator(task_id = "printing_current_date_and_time", python_callable=current_datetime)
