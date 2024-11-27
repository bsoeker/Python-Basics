# use the dotenvx or other .env manager to your liking
# dotenvx run -- python <your_python_file_name>.py
# if the terminal is PowerShell, the command is dotenvx run -- -- python <your_python_file_name>.py
# https://dotenvx.com/docs/quickstart


import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("PASSWORD")

to_email = os.getenv("TARGET")
subject = os.getenv("SUBJECT")
body = os.getenv("BODY")

msg = MIMEMultipart()
msg["From"] = EMAIL_ADDRESS
msg["To"] = to_email
msg["Subject"] = subject
msg["X-Priority"] = "3"  # High priority (1=High, 3=Normal, 5=Low)

# Attach the email body
msg.attach(MIMEText(body, "plain"))

# Attach a file (optional)
# file_path = "example.txt"
# attachment = MIMEBase("application", "octet-stream")
# with open(file_path, "rb") as file:
#     attachment.set_payload(file.read())
# encoders.encode_base64(attachment)
# attachment.add_header(
#     "Content-Disposition",
#     f"attachment; filename={file_path}",
# )
# msg.attach(attachment)

# Send the email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
