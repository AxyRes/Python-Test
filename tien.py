import smtplib, ssl
from requests import get
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

current_date = date.today()
ip = get('https://api.ipify.org').text
#print(f'My public IP address is: {ip}')

# The mail addresses and password
sender_email = "ippulicathome@gmail.com" 
receiver_email = "prodesaxy@gmail.com"  # Enter your receiver address
password = "Ippublic123"


#setup MINE
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'GET IP PUBLIC FROM HOME ' + str(current_date)
MAIL_CONTENT = '''
Hey AxyRes, I give this for you.

Here is IP public from Home: 
''' + str(ip) + '''


Hacker Man
'''


message.attach(MIMEText(MAIL_CONTENT, 'plain'))


context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("Has send mail suscesfully!!")

raise SystemExit(0)