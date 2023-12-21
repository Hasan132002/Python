import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_emails):
    # SMTP server details
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    
    # Email credentials
    EMAIL_ADDRESS = 'hasanraza132002@gmail.com'
    EMAIL_PASSWORD = ''
    
    # Create a MIMEText object
    msg = MIMEText(body)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject
    
    try:
        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_emails, msg.as_string())
        print(f"Email sent successfully to {', '.join(to_emails)}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage with multiple recipients
recipients = ["hasanraza132002@gmail.com", "hasanraza132002@gmail.com", "hasanraza132002@gmail.com"]
send_email("Test Subject", "ProgrammingFundamentals101", recipients)
