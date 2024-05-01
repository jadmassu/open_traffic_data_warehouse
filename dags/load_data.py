from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from models.models import Vehicle, VehiclePath
from utils.database_manager import DatabaseManager
from utils.data_splitter import load_data_from_csv
import os




connection_string = os('DB_CONNECTION_STRING')
database_name = os('DB_NAME')
vehicle_table_name = os('VEHICLE_TABLE_NAME')
vehicle_path_table_name = os('VEHICLE_PATH_TABLE_NAME')
csv_file_path = os('CSV_FILE_PATH')


db_manager = DatabaseManager(connection_string, database_name)


def create_database():
    try:
        db_manager.create_database()
    except Exception as e:
        print(f"An error occurred while creating the database: {e}")

def load_data_into_database():
    try:
       
        vehicle, vehicle_path = load_data_from_csv(csv_file_path)
        db_manager.insert_data(Vehicle, vehicle)
        db_manager.insert_data(VehiclePath, vehicle_path)
        
     
    except Exception as e:
        print(f"An error occurred: {e}")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    'create_db_and_load_data_multiple_tables_dag',
    default_args=default_args,
    description='A DAG to create a database and load data from CSV into multiple tables',
    schedule_interval=timedelta(days=1),
)


create_db_task = PythonOperator(
    task_id='create_database',
    python_callable=create_database,
    dag=dag,
)


load_data_task = PythonOperator(
    task_id='load_data_into_database',
    python_callable=load_data_into_database,
    dag=dag,
)


create_db_task >> load_data_task