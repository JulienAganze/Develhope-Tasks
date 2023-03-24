import time 
import json
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.utils.dates import days_ago
from time import time
from datetime import datetime, timedelta

default_args ={
    'owner':'airflow' ,
    'retries': 1,            # How many retries do you want
    'retry_delay': timedelta(minutes=5),  #delay before doing another retry 
    }  


#Write a dag which creates an employe table- each row represents a new person and contains info about their name and age then insert 3 peole(with the correct metadata)
# and finally execute a query which calculates the average age of all employees

create_query = """
DROP TABLE IF EXISTS public.employee_data;
CREATE TABLE public.employee_data (first_name VARCHAR(250), age INT);
"""

#inserting some data into our table
insert_data_query = """
INSERT INTO  public.employee_data (first_name, age)
values ('Josue',24), ('Julien',25), ('Ketsia',22)
"""

#calculating average age
calculating_average_age = """
DROP TABLE IF EXISTS average_employees_age;
CREATE TABLE IF NOT EXISTS average_employees_age AS
SELECT round(avg(age),0) as average_employees_age
FROM employee_data
"""



#DAG creation

dag_postgres = DAG(dag_id = "employee_data_dag", default_args = default_args, schedule_interval = None, start_date = days_ago(1))

#Deining tasks

create_table = PostgresOperator(task_id = "creation_of_table", sql = create_query, dag = dag_postgres, postgres_conn_id = "postgres_julien_local")

insert_data = PostgresOperator(task_id = "insertion_of_data", sql = insert_data_query, dag = dag_postgres, postgres_conn_id = "postgres_julien_local")

group_data = PostgresOperator(task_id = "calculating_average_age", sql = calculating_average_age, dag = dag_postgres, postgres_conn_id = "postgres_julien_local")

create_table >> insert_data >> group_data