import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def connect_to_database():
    try:
        # Connect to PostgreSQL server
        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )
        return connection
    except OperationalError as e:
        print(f"The error '{e}' occurred.")

def close_connection(connection, cursor):
    # Close the connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")

def add_client(client_data):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        placeholders = ', '.join(['%s'] * len(client_data))
        sql_query = f"INSERT INTO Clients VALUES ({placeholders})"

        cursor.execute(sql_query, client_data)
        connection.commit()
        print("Client added successfully!")

    finally:
        close_connection(connection, cursor)

def update_client(user_id, new_data):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Generate SQL query for updating client data
        update_query = """
            UPDATE Clients
            SET created_at = %s,
                status = %s,
                batch = %s,
                credit_limit = %s,
                interest_rate = %s,
                denied_reason = %s,
                denied_at = %s
            WHERE user_id = %s
        """
        # Add user_id to new_data for proper execution of the query
        new_data.append(user_id)

        cursor.execute(update_query, new_data)
        connection.commit()
        print("Client updated successfully!")

    finally:
        close_connection(connection, cursor)

if __name__ == "__main__":
    # Example usage
    new_client_data = [0, '2024-02-29 12:00:00', 'approved', 1, 5000, 5, None, None]
    add_client(new_client_data)

    # Example usage for updating client data
    user_id_to_update = 0
    updated_client_data = ['2024-03-01 12:00:00', 'denied', 2, 3000, 6, 'Income too low', '2024-03-01 12:00:00']
    update_client(user_id_to_update, updated_client_data)
