
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models.models import Base 

class DatabaseManager:
    def __init__(self, connection_string, database_name):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        self.database_name = database_name

       
    def create_database(self):
        try:
            with self.engine.connect() as connection:
                connection.execute("COMMIT")
                result = connection.execute(
                    f"SELECT 1 FROM pg_database WHERE datname='{self.database_name}'"
                )
                exists = bool(result.fetchone())
                if not exists:
                    connection.execute(f'CREATE DATABASE {self.database_name}')
                    print(f"Database '{self.database_name}' created successfully.")
                else:
                    print(f"Database '{self.database_name}' already exists.")
        except Exception as e:
            print(f"Error creating database: {e}")
            
    def insert_data(self, table_type, data):      
        try:           
            session = self.Session()
            session.bulk_insert_mappings(table_type, data)
            session.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error inserting data into database: {e}")
            session.rollback()
        finally:
            # Close session
            session.close()

