# Контроллер программы - тут все происходит

import os
from time import sleep

from view.view import View
from util.my_email import Email
from util.settings import Settings
from tqdm import tqdm


class Controller:
    def __init__(self):
        self._viewer = View()
        self._email = Email()

    @staticmethod
    def files(path, ext):  # Генератор списка файлов в указанной директории с использованием маски
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)) and file.endswith(ext):
                yield file

    def run(self):  # Сама программа
        self._viewer.print("Запуск выгрузки...")
        self._viewer.print("Читаю каталог с файлами...")

        # Список файлов, с которыми будем работать
        file_list = [file for file in self.files(Settings().work_dir, '.csv')]

        self._viewer.print("Каталог с файлами прочитан.")
        self._viewer.print(f"Запрос выполнен, будет выгружено {len(file_list)} записей.")

        if len(file_list) > 0:
            for file in tqdm(file_list, desc='Прогресс'):  # Главный цикл обработки
                with open(Settings().work_dir + '\\' + file, 'r') as f:  # Открыли файл CSV - там должен быть email
                    email = f.readline()
                attach = os.path.splitext(Settings().work_dir + '\\' + file)[0] + '.pdf'  # Формируем путь к PDF

                try_if_error = Settings().try_if_error
                while try_if_error > 0:  # Может потребоваться несколько раз отправить
                    try:
                        self._email.send_message(email, attach)  # Вот тут отправка!!!!
                        self._viewer.to_log(f"Отправлено address: {email}; файл: {attach}")
                        break
                    except Exception as e:
                        self._viewer.print(f"Ошибка отправки: {e} address: {email}; файл: {attach}")
                        self._viewer.print("Пробую отправить письмо еще раз...")
                        try_if_error = - 1
                        if try_if_error == 0:
                            self._viewer.print(f"ОШИБКА! Квитанция не отправлена!!!. address: {email}; "
                                               f"файл: {attach}")
                sleep(Settings().email_delay)  # Задержка между письмами

        self._viewer.print("Выгрузка завершена!")
