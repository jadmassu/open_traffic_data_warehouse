from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_dbt_vehicles():
    subprocess.run(['dbt', 'run', '--models', 'vehicles'])

def run_dbt_vehicle_path():
    subprocess.run(['dbt', 'run', '--models', 'vehicle_path'])

dag = DAG(
    'dbt_workflow',
    default_args=default_args,
    description='DAG for running DBT models',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 5, 8),
    tags=['dbt']
)

dbt_run_vehicles = PythonOperator(
    task_id='dbt_run_vehicles',
    python_callable=run_dbt_vehicles,
    dag=dag,
)

dbt_run_vehicle_path = PythonOperator(
    task_id='dbt_run_vehicle_path',
    python_callable=run_dbt_vehicle_path,
    dag=dag,
)

dbt_run_vehicles >> dbt_run_vehicle_path
