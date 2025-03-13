from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()


message["from"] = "Moody"
message["to"] = "test@gmail.com"
message["subject"] = "This is a test"
# message.attach(MIMEText("Body", "html"))
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("image").read_bytes()))

# smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
# smtp.close()

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("set_email", "set_password")
    smtp.send_message(message)
    print("Sent...")
