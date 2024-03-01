from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import OperationalError
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

# Get SMTP server info from environment variables
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

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

def send_payment_reminder_emails(clients_with_pending_payments):
    # Function to send payment reminder emails to clients
    try:
        # Connect to SMTP server
        smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtp_server.starttls()
        smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)
        
        # Query database for clients with pending payments
        
        # Loop through clients and send reminder emails
        # Replace placeholders with actual client information
        for client in clients_with_pending_payments:
            subject = 'Payment Reminder'
            body = f"Dear {client['name']},\n\nThis is a reminder that your loan payment of {client['amount']} is due on {client['due_date']}. Please ensure timely payment to avoid any penalties.\n\nBest regards,\nYour Bank"
            message = MIMEMultipart()
            message['From'] = SMTP_USERNAME
            message['To'] = get_user_email(client['user_id'])
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))
            smtp_server.send_message(message)
        
        # Close connection to SMTP server
        smtp_server.quit()
        
        print("Payment reminder emails sent successfully!")
    except Exception as e:
        print(f"Error sending payment reminder emails: {e}")


def send_weekly_summary_email():
    # Function to send weekly summary email to operations team
    try:
        # Connect to SMTP server
        smtp_server = smtplib.SMTP('smtp.example.com', 587)
        smtp_server.starttls()
        smtp_server.login('your_email@example.com', 'your_password')
        
        # Compile weekly operational summary data
        
        # Construct email body with summary data
        subject = 'Weekly Operational Summary'
        body = "This is the weekly operational summary:\n\n- Number of loans issued: 100\n- Number of payments received: 90\n- Default rate: 5%\n- Adherence to payment schedule: 95%\n\nPlease review the attached report for detailed information."
        message = MIMEMultipart()
        message['From'] = 'your_email@example.com'
        message['To'] = 'operations_team@example.com'
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        
        # Attach report file if necessary
        # with open('weekly_report.pdf', 'rb') as attachment:
        #     part = MIMEBase('application', 'octet-stream')
        #     part.set_payload((attachment).read())
        # encoders.encode_base64(part)
        # part.add_header('Content-Disposition', "attachment; filename= weekly_report.pdf")
        # message.attach(part)
        
        # Send email
        smtp_server.send_message(message)
        
        # Close connection to SMTP server
        smtp_server.quit()
        
        print("Weekly summary email sent successfully!")
    except Exception as e:
        print(f"Error sending weekly summary email: {e}")

def get_user_email(user_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Query database to get user email based on user_id
        cursor.execute("SELECT email FROM Users WHERE user_id = %s", (user_id,))
        user_email = cursor.fetchone()

        if user_email:
            return user_email[0]  # Return the email address
        else:
            print(f"No email found for user with user_id {user_id}.")
            return None
    finally:
        if connection:
            cursor.close()
            connection.close()
