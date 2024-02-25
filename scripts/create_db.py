import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
import traceback

# Load environment variables from .env file
load_dotenv()

def create_database():
    connection = None  # Initialize the connection variable

    try:
        # Connect to PostgreSQL server
        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        
        # Set autocommit to True
        connection.set_session(autocommit=True)

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Get the database name from the .env file
        db_name = os.getenv("DB_NAME")

        # Execute a SQL command to create a database
        cursor.execute(f"CREATE DATABASE {db_name}")

        print("Database created successfully!")

    except OperationalError as e:
        print(f"The error '{e}' occurred.")
        traceback.print_exc()

    finally:
        # Close the connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

if __name__ == "__main__":
    create_database()
