#!/usr/bin/env python3

import smtplib
import csv
from email.message import EmailMessage

# MIME libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Your gmail credentials
gmail_name = 'your gmail account goes here'
gmail_password = 'your password goes here'

# Define the message
bodyHTML = open('email.html').read()
bodyPLAIN = open('email.txt').read()

    # Basic function to send mails
def send_mail(body_html, body_plan, subject, to):
    msg = MIMEMultipart('mixed')
    msgR = MIMEMultipart('related')
    msgA = MIMEMultipart('alternative')

    # Add HTML and plain text version of the mail
    msgR.attach(MIMEText(bodyHTML, 'html'))
    msgA.attach(MIMEText(bodyPLAIN, 'plain'))

    msgA.attach(msgR)
    msg.attach(msgA)

    msg['Subject'] = subject
    msg['From'] = gmail_name
    msg['To'] = to

    # Send the email
    try:
        server_ssl.send_message(msg)
    except:
        print('Impossible to send the mail')
##########################################

# Open the connection to the server and login into it
try:
    server_ssl= smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.login(gmail_name,gmail_password)
except:
    print("Impossible to set the connection")

with open('to_example.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count != 0:
            # Personalize email with name
            bodyHTML = bodyHTML.replace("{}", row[0], 1)
            bodyPLAIN = bodyPLAIN.replace("{}", row[0], 1)

            send_mail(bodyHTML, bodyPLAIN, 'subject', row[1])

            # Get back non-personalize version
            bodyHTML = bodyHTML.replace(row[0], "{}", 1)
            bodyPLAIN = bodyPLAIN.replace(row[0], "{}", 1)
        line_count += 1

# Close the connection
server_ssl.quit()
