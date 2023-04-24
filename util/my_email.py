import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from email.utils import formataddr
from util.settings import Settings


class Email:
    def __init__(self):
        self._server = Settings().server
        self._port = Settings().port
        self._user = Settings().user
        self._password = Settings().password
        self._from_name = Settings().from_name
        self._sender = Settings().sender
        self._subject = Settings().subject

    @staticmethod
    def get_html_msg():
        return '<html>' \
                '<center>' \
                '<H1>Уважаемый собственник!</H1>' \
                '</center>' \
                '<p>Вам направлена счёт-квитанция на оплату Взноса на капитальный ремонт общего' \
                ' имущества многоквартирного дома.' \
                '</p>' \
                '<p>Напоминаем о необходимости оплатить данный счет <b>в срок до 25 числа месяца.</b></p>' \
                '<p>Если у Вас остались вопросы, рекомендуем обратиться следующими способами:</p>' \
                '<ul>' \
                '<li>Позвонив в call-центр: <b>(8332) 254-888; (8332) 440-880</b></li>' \
                '<li>Написав на e-mail: <a href="mailto:mail@rkc43.ru">mail@rkc43.ru</a></li>' \
                '<li>При личном обращении в в центр обслуживания населения ООО «РКЦ» по адресам:</li>' \
                '<ul>' \
                '<li>г.Киров, ул. Воровского, д.10;</li>' \
                '<li>г.Киров, ул. Казанская, д.24;</li>' \
                '<li>г.Киров, ул. Маршала Конева, д.7/6;</li>' \
                '<li>г.Киров (Радужный мкр), ул. Индустриальная, д.2.</li>' \
                '</ul>' \
                '</ul>' \
                '<p>Благодарим Вас за своевременную оплату услуг!</p>' \
                '<p>С уважением, ООО «РКЦ».</p>' \
                '</html>'

    @staticmethod
    def get_text_msg(self):
        return  'Уважаемый собственник!\n\n' \
                'Вам направлена счёт-квитанция на оплату Взноса на капитальный ремонт' \
                ' общего имущества многоквартирного дома.\n' \
                'Напоминаем о необходимости оплатить данный счет в срок до 25 числа месяца.\n\n' \
                'Если у Вас остались вопросы, рекомендуем обратиться следующими способами:\n' \
                '- Позвонив в call-центр: (8332) 254-888; (8332) 440-880\n' \
                '- Написав на e-mail: mail@rkc43.ru\n' \
                '- При личном обращении в в центр обслуживания населения ООО "РКЦ" по адресам:\n' \
                '  - г.Киров, ул. Воровского, д.10;\n' \
                '  - г.Киров, ул. Казанская, д.24;\n' \
                '  - г.Киров, ул. Маршала Конева, д.7/6;\n' \
                '  - г.Киров (Радужный мкр), ул. Индустриальная, д.2.\n\n' \
                'Благодарим Вас за своевременную оплату услуг!\n' \
                'С уважением, ООО "РКЦ".\n'
    def send_message(self, receiver, attach):
        receivers = [receiver]
        msg = MIMEMultipart()

        msg['Subject'] = self._subject
        msg['From'] = formataddr((self._from_name, self._sender))
        msg['To'] = receiver

#        send_file = 'C:\\temp\\исходящий.pdf'
        send_file = attach

        with open(send_file, 'rb') as file:
            fn = os.path.basename(send_file)
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-disposition', 'attachment', filename=('utf-8', '', fn))
            msg.attach(part)

        # noinspection PyTypeChecker
        msg.attach(MIMEText(self.get_html_msg().encode('utf-8'), 'html', 'UTF-8'))
#        msg.attach(MIMEText(self.get_text_msg().encode('utf-8'), 'plain', 'UTF-8'))

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(self._server, self._port, context=context) as server:
            server.login(self._user, self._password)
            server.sendmail(self._sender, receivers, msg.as_string())
