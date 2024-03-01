from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def check_clients():
    conn = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
    )

    query = """
    SELECT DISTINCT c.user_id, u.email
    FROM clients c
    JOIN loans l ON c.user_id = l.user_id
    JOIN users u ON c.user_id = u.user_id
    WHERE l.status = 'ongoing'
    AND l.due_at BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days'
    """
    df = pd.read_sql(query, conn)
    conn.close()
    df.to_csv("/path/to/client_reminders.csv", index=False)

def send_reminder_email():
    with open("/path/to/client_reminders.csv", "r") as file:
        email_content = file.read()

    email_subject = "Loan Payment Reminder"
    email_body = "Dear Customer,\n\nThis is a friendly reminder that your loan payment is due soon. Please ensure to make the payment on time to avoid any penalties.\n\nThank you.\n\nBest regards,\nYour Partners from Infinity"

    for index, row in email_content.iterrows():
        email_task = EmailOperator(
            task_id=f"send_email_{index}",
            to=row['email'],
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
    "client_interaction",
    default_args=default_args,
    description="Client Interaction DAG",
    schedule_interval="0 0 * * *",  # Run daily at midnight
    catchup=False
)

check_clients_task = PythonOperator(
    task_id="check_clients",
    python_callable=check_clients,
    dag=dag
)

send_email_task = PythonOperator(
    task_id="send_reminder_email",
    python_callable=send_reminder_email,
    dag=dag
)

check_clients_task >> send_email_task
