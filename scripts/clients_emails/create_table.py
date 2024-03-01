import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
import traceback

# Load environment variables from .env file
load_dotenv()

def create_table():
    connection = None
    try:
        # Connect to PostgreSQL server
        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )

        cursor = connection.cursor()

        # Define the table creation SQL statement
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL
        );
        '''

        # Execute the table creation SQL statement
        cursor.execute(create_table_query)

        print("Table created successfully!")

    except OperationalError as e:
        print(f"The error '{e}' occurred.")
        traceback.print_exc()

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

if __name__ == "__main__":
    create_table()
