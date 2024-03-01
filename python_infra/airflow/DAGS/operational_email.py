from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def retrieve_data():
    conn = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
    )
    query = """
    SELECT
        COUNT(*) AS total_loans,
        SUM(loan_amount) AS total_loan_amount
    FROM loans
    WHERE EXTRACT(WEEK FROM created_at) = EXTRACT(WEEK FROM CURRENT_DATE)
    """
    df = pd.read_sql(query, conn)
    conn.close()
    df.to_csv("/path/to/weekly_summary.csv", index=False)

def send_weekly_email():
    with open("/path/to/weekly_summary.csv", "r") as file:
        email_content = file.read()

    email_subject = "Weekly Operational Summary"
    email_body = f"Attached is the weekly operational summary.\n\n{email_content}"

    email_task = EmailOperator(
        task_id="send_email",
        to="recipient@example.com",
        subject=email_subject,
        html_content=email_body,
        dag=dag
    )
    email_task.execute()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 26),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "weekly_operational_summary",
    default_args=default_args,
    description="Weekly Operational Summary DAG",
    schedule_interval="0 0 * * 1",  # Run every Monday at midnight
    catchup=False
)

retrieve_data_task = PythonOperator(
    task_id="retrieve_data",
    python_callable=retrieve_data,
    dag=dag
)

send_email_task = PythonOperator(
    task_id="send_weekly_email",
    python_callable=send_weekly_email,
    dag=dag
)

retrieve_data_task >> send_email_task
