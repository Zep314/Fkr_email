# import smtplib                                      # Импортируем библиотеку по работе с SMTP
#
# # Добавляем необходимые подклассы - MIME-типы
# from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
# from email.mime.text import MIMEText                # Текст/HTML
# #from email.mime.image import MIMEImage              # Изображения

import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import formataddr

class Email:
    def __init__(self):
        pass

    def send_message(self):
        sender = 'krpd@rkc43.ru'
        receivers = ['mordanovda@mail.ru']
        server = 'mail.vdkanal.ru'

        port = 465
        user = 'krpd@rkc43.ru'
        password = 'Qwerty123Rkc'

        html = ""
        html += '<html>'
        html += '<center>'
        html += '<H1>Уважаемый собственник!</H1>'
        html += '</center>'
        html += '<p>Вам направлена счёт-квитанция на оплату Взноса на капитальный ремонт общего имущества многоквартирного дома.'
        html += '</p>'
        html += '<p>Напоминаем о необходимости оплатить данный счет <b>в срок до 25 числа месяца.</b></p>'
        html += '<p>Если у Вас остались вопросы, рекомендуем обратиться следующими способами:</p>'
        html += '<ul>'
        html += '<li>Позвонив в call-центр: <b>(8332) 254-888; (8332) 440-880</b></li>'
        html += '<li>Написав на e-mail: <a href="mailto:mail@rkc43.ru">mail@rkc43.ru</a></li>'
        html += '<li>При личном обращении в в центр обслуживания населения ООО «РКЦ» по адресам:</li>'
        html += '<ul>'
        html += '<li>г.Киров, ул. Воровского, д.10;</li>'
        html += '<li>г.Киров, ул. Казанская, д.24;</li>'
        html += '<li>г.Киров, ул. Маршала Конева, д.7/6;</li>'
        html += '<li>г.Киров (Радужный мкр), ул. Индустриальная, д.2.</li>'
        html += '</ul>'
        html += '</ul>'
        html += '<p>Благодарим Вас за своевременную оплату услуг!</p>'
        html += '<p>С уважением, ООО «РКЦ».</p>'
        html += '</html>'

        text = ''
        text += 'Уважаемый собственник!\n'
        text += '\n'
        text += 'Вам направлена счёт-квитанция на оплату Взноса на капитальный ремонт общего имущества многоквартирного дома.\n'
        text += 'Напоминаем о необходимости оплатить данный счет в срок до 25 числа месяца.\n'
        text += '\n'
        text += 'Если у Вас остались вопросы, рекомендуем обратиться следующими способами:\n'
        text += '- Позвонив в call-центр: (8332) 254-888; (8332) 440-880\n'
        text += '- Написав на e-mail: mail@rkc43.ru\n'
        text += '- При личном обращении в в центр обслуживания населения ООО "РКЦ" по адресам:\n'
        text += '  - г.Киров, ул. Воровского, д.10;\n'
        text += '  - г.Киров, ул. Казанская, д.24;\n'
        text += '  - г.Киров, ул. Маршала Конева, д.7/6;\n'
        text += '  - г.Киров (Радужный мкр), ул. Индустриальная, д.2.\n'
        text += '\n'
        text += 'Благодарим Вас за своевременную оплату услуг!\n'
        text += 'С уважением, ООО "РКЦ".\n'


        msg = MIMEMultipart()

        msg['Subject'] = 'Платежный документ - взнос на капитальный ремонт'
        msg['From'] = formataddr(('ООО "Расчетно-консультационный центр"', 'krpd@rkc43.ru'))
        msg['To'] = 'mordanovda@mail.ru'

        send_file = 'C:\\temp\\исходящий.pdf'

        fn = 'qwe.pdf'

        with open(send_file, 'rb') as file:
            file_name = os.path.basename(send_file)
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            #part = MIMEApplication(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename = %s' % fn)
            msg.attach(part)

        msg.attach(MIMEText(html.encode('utf-8'), 'html', 'UTF-8'))
        #msg.attach(MIMEText(text.encode('utf-8'), 'plain', 'UTF-8'))

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(server, port, context=context) as server:
            server.login(user, password)
            server.sendmail(sender, receivers, msg.as_string())
            print('mail successfully sent!')