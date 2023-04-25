# Настройки

import configparser
import sys


class Settings:
    def __init__(self):
        # Настройки читаем из ini - файла
        config = configparser.ConfigParser()

        try:
            config.read('fkr_email.ini')
        except Exception as e:
            print(f"Не могу прочитать файл конфигурации: {e}")
            sys.exit(-1)

        self.server = config.get('DEFAULT', 'server')
        self.port = config.getint('DEFAULT', 'port')
        self.user = config.get('DEFAULT', 'user')
        self.password = config.get('DEFAULT', 'password')
        self.from_name = config.get('DEFAULT', 'from_name')
        self.sender = config.get('DEFAULT', 'sender')
        self.subject = config.get('DEFAULT', 'subject')
        self.work_dir = config.get('DEFAULT', 'work_dir')
        self.email_delay = config.getint('DEFAULT', 'email_delay')
        self.try_if_error = config.getint('DEFAULT', 'try_if_error')
        self.log_file = config.get('DEFAULT', 'log_file')
