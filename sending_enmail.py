import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()
password: str = os.getenv("password")
email1: str = os.getenv("email")
remail: str = os.getenv("remail")


def send_reset_email(email: str, token: str):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = email1
    smtp_password = password

    # Email content
    subject = "Password Reset"
    body = f"Click the following link to reset your password: http://your-app.com/reset-password?token={token}"

    # Create MIMEText object
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = smtp_username
    message["To"] = email

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the SMTP server
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, [email], message.as_string())

        # Disconnect from the SMTP server
        server.quit()

        print("Password reset email sent successfully.")
    except Exception as e:
        print(f"Error sending password reset email: {e}")

# Update your function to include the SMTP setup
def send_reset_email_with_smtp(email: str, token: str):
    # Assuming you have a function to get user by email
    user = get_user_by_email(email)

    if user:
        # Send the reset email using SMTP
        send_reset_email(email, token)
        print("Password reset email sent.")
    else:
        print("User not found for the given email.")

# Assuming you have a function to get user by email
def get_user_by_email(email: str):
    # Your implementation to get user from the database
    pass

# Assuming you have a function to update user password
def update_user_password(user, new_password: str):
    # Your implementation to update user password in the database
    pass

# Example usage:
# Assuming you have a user and a reset token
print(f"my email is {email1} \nmy password is {password} \nmy remail is {remail}")
user_email = remail
reset_token = "your-reset-token"

# Send the password reset email using SMTP
send_reset_email(user_email, reset_token)
