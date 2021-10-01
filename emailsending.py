import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from maprequest import MapRequest, FROM_LOCATION, TO_LOCATION

import os

FROM_EMAIL = os.getenv("FROM_EMAIL")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")


def send_email(no_of_trips_available):
    no_of_trips_available = no_of_trips_available
    from_location, to_location = FROM_LOCATION, TO_LOCATION
    receiver_email = "***@gmail.com"
    subject = f"{no_of_trips_available} Trip Details are available"
    message = MIMEMultipart()
    message["From"] = FROM_EMAIL
    message["To"] = receiver_email
    message["Subject"] = subject
    body = f"Please find the attached trip details from {from_location}  to  {to_location}"
    message.attach(MIMEText(body, "plain"))
    filename = "data.txt"
    attachment = open("F:/blablacarAPI/data.txt", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    message.attach(p)
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=FROM_EMAIL, password=GMAIL_PASSWORD)
    text = message.as_string()
    connection.sendmail(from_addr=FROM_EMAIL, to_addrs=message["To"], msg=text)
    connection.close()
