from view.view import View
from util.email import Email


class Controller:
    def __init__(self):
        self._viewer = View()
        self._email = Email()

    def run(self):
        print("Hi!")
        self._email.send_message()
