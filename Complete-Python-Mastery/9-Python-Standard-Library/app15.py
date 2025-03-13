from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

message = MIMEMultipart()

template = Template(Path("template.html").read_text())

message["from"] = "Moody"
message["to"] = "test@gmail.com"
message["subject"] = "This is a test"
# body = template.substitute({"name": "John"})

body = template.substitute(name="John")
message. attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("image").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("set_email", "set_password")
    smtp.send_message(message)
    print("Sent...")
