# import smtplib                                      # Импортируем библиотеку по работе с SMTP
#
# # Добавляем необходимые подклассы - MIME-типы
# from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
# from email.mime.text import MIMEText                # Текст/HTML
# #from email.mime.image import MIMEImage              # Изображения

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class Email:
    def __init__(self):
        pass

    def send_message(self):
        # addr_from = "mordanov.da@rkc43.ru"  # Адресат
        # addr_to = "mordanovda@mail.ru"  # Получатель
        # password = "Qwerty123Rkc"  # Пароль
        #
        # msg = MIMEMultipart()  # Создаем сообщение
        # msg['From'] = addr_from  # Адресат
        # msg['To'] = addr_to  # Получатель
        # msg['Subject'] = 'Тема сообщения123'  # Тема сообщения
        #
        # body = "Текст сообщения123"
        # msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст
        #
        # server = smtplib.SMTP(host = 'mail.vdkanal.ru', port = 465)  # Создаем объект SMTP
        # server.set_debuglevel(True)  # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
        # server.starttls()  # Начинаем шифрованный обмен по TLS
        # server.login(addr_from, password)  # Получаем доступ
        # server.send_message(msg)  # Отправляем сообщение
        # server.quit()

        mail_content = '''Hello,
        This mail is to inform you about Today's meeting.
        '''

        sender_address = 'mordanov.da@rkc43.ru'
        sender_pass = 'Qwerty123Rkc'
        receiver_address = 'mordanovda@mail.ru'

        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Info about meeting.'
        message.attach(MIMEText(mail_content, 'plain'))

        session = smtplib.SMTP('mail.vdkanal.ru', 465)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

        print('Mail Sent')