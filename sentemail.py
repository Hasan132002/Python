import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    # SMTP server details
    SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Default port for most SMTP servers. Change if different.
    
    # Email credentials
    EMAIL_ADDRESS = 'it.dev75@dawateislami.net'  # Replace with your email address
    EMAIL_PASSWORD = '$'  # Replace with your email password or app password if using Gmail
    
    # Create a MIMEText object
    msg = MIMEText(body)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = subject
    
    try:
        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start a TLS session (if required)
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
send_email("Test Subject", "ProgrammingFundamentals101", "hasanraza132002@gmail.com")
