import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
import traceback

# Load environment variables from .env file
load_dotenv()

def create_connection():
    """Create a connection to the PostgreSQL database."""
    try:
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
        traceback.print_exc()
        return None

def fetch_user_ids(connection):
    """Fetch all user IDs from the clients table."""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM clients")
        user_ids = cursor.fetchall()
        return [row[0] for row in user_ids]
    except OperationalError as e:
        print(f"The error '{e}' occurred.")
        traceback.print_exc()
        return []

def generate_emails(user_ids):
    """Generate email addresses based on user IDs."""
    emails = [f"{user_id}@provider.com" for user_id in user_ids]
    return emails

def insert_emails(connection, user_ids, emails):
    """Insert emails into the users table."""
    try:
        cursor = connection.cursor()
        for user_id, email in zip(user_ids, emails):
            cursor.execute("INSERT INTO users (user_id, email) VALUES (%s, %s)", (user_id, email))
        connection.commit()
        print("Emails inserted successfully!")
    except OperationalError as e:
        print(f"The error '{e}' occurred.")
        traceback.print_exc()
        connection.rollback()

def main():
    # Create a connection to the database
    connection = create_connection()
    if connection is None:
        return

    # Fetch user IDs from the clients table
    user_ids = fetch_user_ids(connection)
    if not user_ids:
        print("No user IDs found in the clients table.")
        connection.close()
        return

    # Generate email addresses based on user IDs
    emails = generate_emails(user_ids)

    # Insert emails into the users table
    insert_emails(connection, user_ids, emails)

    # Close the database connection
    connection.close()
    print("PostgreSQL connection is closed.")

if __name__ == "__main__":
    main()
