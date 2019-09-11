import smtplib
import csv
from email.message import EmailMessage

#Your gmail credentials
gmail_name = 'your gmail account goes here'
gmail_password = 'your password goes here'

#Define the message
with open('discourse.txt') as text:
    msg = text.read()

#Basic function to send mails
def send_mail(body, subject, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = gmail_name
    msg['To'] = to

    #Send the email
    try:
        server_ssl.send_message(msg)
    except:
        print('Impossible to send the mail')

    return
##########################################

#Open the connection to the server and login into it
try:
    server_ssl= smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.login(gmail_name,gmail_password)
except:
    print("Impossible to set the connection")

with open('to_example.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        msg = msg.replace("{}",row[0],1)
        send_mail(msg,'Bienvenido a ACM',row[1])
        msg = msg.replace(row[0],"{}",1)
    line_count += 1

#Close the connection
server_ssl.quit()