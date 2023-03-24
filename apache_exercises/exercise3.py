import requests
import time
import json
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

def get_data():
    ticker = {'tickers': ['IBM', 'TSCO.LON', 'SHOP.TRT', 'GPV.TRV']}
    #ticker = kwargs['tickers']
    api_key = "4IRFUPKUNWEDMP5G"
    for i in ticker.values():
        for a in range(0,4):
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
            url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ i[a] +'&apikey='+ api_key 
            r = requests.get(url)
            try:
                data = r.json()
                path = "/home/julian/Desktop/DATA_CENTER_1/DATA_LAKE/"
                with open(path + "stock_market_raw_data_" + i[a] + "_" + str(time.time()), "w") as outfile:
                    json.dump(data,outfile)
            except:
                pass

def get_data2(**kwargs):
    ticker = kwargs ['ticker1']#,'ticker2','ticker3','ticker4']
    #ticker = kwargs['tickers']
    api_key = "4IRFUPKUNWEDMP5G"
    #for i in ticker.values():
        #for a in range(0,4):
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ ticker +'&apikey='+ api_key 
    r = requests.get(url)
    try:
        data = r.json()
        path = "/home/julian/Desktop/DATA_CENTER_1/DATA_LAKE/"
        with open(path + "stock_market_raw_data_" + ticker + "_" + str(time.time()), "w") as outfile:
            json.dump(data,outfile)
    except:
        pass


default_dag_args ={
    'start_date': datetime(2023,3,10),    #When do you want this DAG to run for the 1st time
    'email_on_failure': False,    #Do you want to send an email on failure
    'email_on_retry':False,    # Befor failing it might retry a bunch of times  
    'retries':1,            # How many retries do you want
    'retry_delay': timedelta(minutes=5),  #delay before doing another retry 
    'project_id':1
}  

with DAG("stock_market_data_dag", schedule_interval = '@daily', catchup=False, default_args = default_dag_args) as dag_python:

    # let  us define our tasks noe
   # task_0 = PythonOperator(task_id = "get_market_data", python_callable = get_data)#, op_kwargs = {'tickers': ['IBM', 'TSCO.LON', 'SHOP.TRT', 'GPV.TRV']})
    task_0 = PythonOperator(task_id = "get_market_data", python_callable = get_data2, op_kwargs = {'ticker1': 'IBM', 'ticker2':'TSCO.LON', 'ticker3':'SHOP.TRT', 'ticker4':'GPV.TRV'})