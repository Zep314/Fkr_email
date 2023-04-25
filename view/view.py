# Вывод на экран и логирование

from util.settings import Settings
import logging


class View:
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            filename=Settings().work_dir + '\\' + Settings().log_file, filemode="w",
                            format="%(asctime)s %(message)s"
                            )

    # Вывод в лог и на экран
    def print(self, msg):
        print(msg)
        self.to_log(msg)

    # Вывод только в лог
    @staticmethod
    def to_log(msg):
        logging.info(msg)
