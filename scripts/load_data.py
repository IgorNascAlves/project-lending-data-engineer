import os
import csv
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def read_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        data = []
        for row in reader:
            # Replace empty datetime values with None
            row = [None if value == '' else value for value in row]
            data.append(row)
        return data


def load_data_into_table(table_name, data):
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

        # Generate the SQL query for inserting data
        placeholders = ', '.join(['%s'] * len(data[0]))
        sql_query = f"INSERT INTO {table_name} VALUES ({placeholders})"

        # Execute the SQL query to insert data into the table
        cursor.executemany(sql_query, data)

        # Commit the changes
        connection.commit()
        print(f"Data loaded into '{table_name}' table successfully!")

    except OperationalError as e:
        print(f"The error '{e}' occurred.")

    finally:
        # Close the connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

if __name__ == "__main__":
    clients_data = read_csv('files/clients.csv')
    loans_data = read_csv('files/loans.csv')

    load_data_into_table('Clients', clients_data)
    load_data_into_table('Loans', loans_data)
