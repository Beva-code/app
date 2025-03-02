import smtplib
import time
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv  # Load environment variables

# Load environment variables from .env file
load_dotenv()

# Email configuration (use environment variables for security)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465  # Use SSL
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
APP_PASSWORD = os.getenv('APP_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')

def send_email(current_time):
    subject = "Current Time Update"
    body = f"The current time is: {current_time}"

    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = RECIPIENT_EMAIL
    message['Subject'] = subject

    # Attach the email body to the message
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())
            print(f"Email sent: {body}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        send_email(current_time)
        time.sleep(300)  # Wait for 5 minutes (300 seconds)

if __name__ == "__main__":
    main()
