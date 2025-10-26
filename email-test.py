# Email Automation -

# use gmail as sending and receving email 
# Key libraries for email automation - 
# 1) smtplib - simple mail transfer protocol - this is core library for sending emails. 
# it handles the connection to an email server (gmail smtp server) and process of sending message.

# it will initiate a secure connection - i.e starttls(), login with credentials and compose message and send
# MIME - multipurpose internet mail extension - its standard format for 
#   sending different types of content like text, images, attachments, etc
# workflow
# connection creation -> create messgae -> send email -> close connection

# https://myaccount.google.com/apppasswords
# pgmh skcy nlip vkhn
# python.email.class@gmail.com

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = os.getenv('USER_NAME')
EMAIL_PWD = os.getenv('USER_PASSWORD')


def send_mail(to_email, sub, body):
    msg = MIMEMultipart()
    msg['FROM'] = EMAIL_USER
    msg['TO'] = to_email
    msg['Subject'] = sub
    
    msg.attach(MIMEText(body, 'HTML'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as gmail_server:
        gmail_server.starttls()
        gmail_server.login(EMAIL_USER, EMAIL_PWD)
        gmail_server.sendmail(EMAIL_USER, to_email, msg.as_string())
        gmail_server.close()

    print("Email Sent .. ")

if __name__ == "__main__":
    send_mail("getsauin@gmail.com", "test-email", "This is test email sent from python client")