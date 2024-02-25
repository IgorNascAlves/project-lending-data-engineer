import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_tables():
    try:
        # Connect to PostgreSQL server
        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Create Clients Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clients (
                user_id SERIAL PRIMARY KEY,
                created_at TIMESTAMP,
                status VARCHAR(10),
                batch INT,
                credit_limit INT,
                interest_rate INT,
                denied_reason VARCHAR(100),
                denied_at TIMESTAMP
            )
        """)

        # Create Loans Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Loans (
                user_id INT REFERENCES Clients(user_id),
                loan_id SERIAL PRIMARY KEY,
                created_at TIMESTAMP,
                due_at TIMESTAMP,
                paid_at TIMESTAMP,
                status VARCHAR(10),
                loan_amount FLOAT,
                tax FLOAT,
                due_amount FLOAT,
                amount_paid FLOAT
            )
        """)

        # Commit the changes
        connection.commit()
        print("Tables created successfully!")

    except OperationalError as e:
        print(f"The error '{e}' occurred.")

    finally:
        # Close the connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

if __name__ == "__main__":
    create_tables()
