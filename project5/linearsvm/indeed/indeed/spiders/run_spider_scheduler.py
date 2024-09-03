import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime
import getpass 

def send_email(subject, body, recipient_email, sender_email, password, attachment_path=None):
    """
    Function to send an email with optional attachment.
    
    Parameters:
    - subject: The subject of the email.
    - body: The body text of the email.
    - recipient_email: Email address of the recipient.
    - sender_email: Email address of the sender.
    - password: Password for the sender's email account.
    - attachment_path: Path to the file to attach (if any).
    """
    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body text
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file if specified
    if attachment_path:
        try:
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(attachment_path)}',
                )
                msg.attach(part)
        except Exception as e:
            print(f"Failed to attach file: {e}")

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def get_latest_file():
    """
    Function to get the path of the latest CSV file in the 'data' directory.
    
    Returns:
    - Path to the latest CSV file if it exists, otherwise None.
    """
    file_name = 'data/indeed_search.csv'

    if os.path.exists(file_name):
        return file_name
    else:
        print(f"No file found at {file_name}")
        return None

if __name__ == "__main__":
    # Sender email address
    sender_email = "vanthinh2231@gmail.com"
    # Prompt for the email password (application-specific)
    password = getpass.getpass("Enter your email password (application-specific): ")

    # Prompt for recipient email address
    recipient_email = input("Enter recipient's email: ")

    print(f"Fetching file at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    # Get the path of the latest file
    file_path = get_latest_file()

    # Define the subject and body of the email
    subject = f"New Job Listings for {datetime.now().strftime('%Y-%m-%d')}"
    body = "Please find the attached job listings file."

    # Send email with or without attachment based on file presence
    if file_path:
        send_email(subject, body, recipient_email, sender_email, password, attachment_path=file_path)
    else:
        send_email(subject, "No job listings found.", recipient_email, sender_email, password)
