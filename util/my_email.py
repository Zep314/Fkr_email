# Отправка одного письма с вложением по указанному адресу

import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from email.utils import formataddr
from re import sub


from util.settings import Settings


class Email:
    def __init__(self):  # Берем настройки
        self._server = Settings().server
        self._port = Settings().port
        self._user = Settings().user
        self._password = Settings().password
        self._from_name = Settings().from_name
        self._sender = Settings().sender
        self._subject = Settings().subject

    @staticmethod
    def get_html_msg():  # Генерируем текст письма в HTML формате
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
               '<font size="1">' \
               'Вы получили это письмо, так как Ваш лицевой счет подписан на доставку платежных документов ' \
               'по электронной почте.<br>' \
               'В случае, если вы не хотите получать платежный документ на электронную почту, перейдите ' \
               'по <a href="https://kabinet.rkc43.ru/kp/Account/LogOn">этой ссылке</a> в Личный кабинет и ' \
               'отмените доставку.' \
               '</font>' \
               '</html>'

    @staticmethod
    def get_text_msg():  # Генерируем текст письма в текстовом формате
        return 'Уважаемый собственник!\n\n' \
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

    def send_message(self, receiver, attach):  # Метод отправки одного письма с вложением
        receivers = [receiver]

        # Формируем тело письма
        msg = MIMEMultipart()
        msg['Subject'] = self._subject
        msg['From'] = formataddr((self._from_name, self._sender))
        msg['To'] = receiver

        with open(attach, 'rb') as file:  # вкладываем вложение
            fn = sub(' +', ' ', attach).split('.')[-2].strip().split(' ')[-2] + '.pdf'
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-disposition', 'attachment', filename=('utf-8', '', fn))
            msg.attach(part)

        # noinspection PyTypeChecker
        msg.attach(MIMEText(self.get_html_msg().encode('utf-8'), 'html', 'UTF-8'))

        # Вдруг надо будет чистый текст рассылать
        # msg.attach(MIMEText(self.get_text_msg().encode('utf-8'), 'plain', 'UTF-8'))

        context = ssl.create_default_context()

        # Соединение с сервером и отправляем письмо
        with smtplib.SMTP_SSL(self._server, self._port, context=context) as server:
            server.login(self._user, self._password)
            server.sendmail(self._sender, receivers, msg.as_string())
