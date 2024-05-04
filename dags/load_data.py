from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import os,sys
rpath = os.path.abspath('/opt/airflow')

if rpath not in sys.path:
    sys.path.insert(0, rpath)
    
from utils.database_manager import DatabaseManager
from utils.data_splitter import load_data_from_csv
from models.models import Vehicle, VehiclePath



# connection_string = os.getenv('DB_CONNECTION_STRING')
# database_name = os.getenv('DB_NAME')
# vehicle_table_name = os.getenv('VEHICLE_TABLE_NAME')
# vehicle_path_table_name = os.getenv('VEHICLE_PATH_TABLE_NAME')
# csv_file_path = os.getenv('CSV_FILE_PATH')


connection_string='postgresql+psycopg2://airflow:airflow@postgres/airflow'
database_name='open_traffic'

csv_file_path='./data/openTraffic.csv'

db_manager = DatabaseManager(connection_string, database_name)

 
def create_database(ds, **kwargs):
    try:
        print("-------------------------testtttttt  ")
       
        x =db_manager.create_database()
        print("-------------------------  ",x)
    except Exception as e:
        print(f"An error occurred while creating the database: {e}")

def load_data_into_database(ds, **kwargs):
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
    task_id='create_database_task',
    python_callable=create_database,
    dag=dag,
)  


load_data_task = PythonOperator(
    task_id='load_data_into_database_task',
    python_callable=load_data_into_database,
    dag=dag,
)


create_db_task >> load_data_task