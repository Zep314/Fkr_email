import smtplib
import ssl
from email.mime.text import MIMEText

sender = 'mordanov.da@rkc43.ru'
receivers = ['mordanovda@mail.ru']

port = 465
user = 'mordanov.da@rkc43.ru'
password = 'Qwerty123Rkc'

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'mordanov.da@rkc43.ru'
msg['To'] = 'mordanovda@mail.ru'

context = ssl.create_default_context()

with smtplib.SMTP_SSL("mail.vdkanal.ru", port, context=context) as server:

    server.login(user, password)
    server.sendmail(sender, receivers, msg.as_string())
    print('mail successfully sent')
