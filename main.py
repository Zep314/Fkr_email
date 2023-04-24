from controller.controller import Controller

if __name__ == '__main__':
    controller = Controller()
    controller.run()

#http://codius.ru/articles/Python_%D0%9A%D0%B0%D0%BA_%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D1%8C_%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE_%D0%BD%D0%B0_%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D1%83%D1%8E_%D0%BF%D0%BE%D1%87%D1%82%D1%83


# /usr/bin/python3.10 /home/dima/Work/Python/Fkr_email/main.py
# Hi!
# Traceback (most recent call last):
#   File "/home/dima/Work/Python/Fkr_email/main.py", line 5, in <module>
#     controller.run()
#   File "/home/dima/Work/Python/Fkr_email/controller/controller.py", line 12, in run
#     self._email.send_message()
#   File "/home/dima/Work/Python/Fkr_email/util/my_email.py", line 52, in send_message
#     session = smtplib.SMTP('mail.vdkanal.ru', 465)
#   File "/usr/lib/python3.10/smtplib.py", line 255, in __init__
#     (code, msg) = self.connect(host, port)
#   File "/usr/lib/python3.10/smtplib.py", line 343, in connect
#     (code, msg) = self.getreply()
#   File "/usr/lib/python3.10/smtplib.py", line 405, in getreply
#     raise SMTPServerDisconnected("Connection unexpectedly closed")
# smtplib.SMTPServerDisconnected: Connection unexpectedly closed
