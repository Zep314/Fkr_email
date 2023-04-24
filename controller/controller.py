from view.view import View
from util.my_email import Email


class Controller:
    def __init__(self):
        self._viewer = View()
        self._email = Email()

    def run(self):
        print("Hi!")
        receive = 'mordanovda@mail.ru'
#        attach = 'C:\\temp\\исходящий.pdf'
        attach = '/home/dima/temp/Гибкие методологии04.pdf'

        self._email.send_message(receive, attach)

        print("Email sent successfully!")
