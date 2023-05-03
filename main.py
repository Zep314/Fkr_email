# Программа отправки электронных писем с вложениями в формате ФКР

from controller.controller import Controller

if __name__ == '__main__':
    controller = Controller()
    controller.run()

# Подсказка на потом:
# сделать exe-файл:

# Открыть командную строку windows
# Установить pyinstaller

# pip install pyinstaller

# Затем перейти в папку с Вашим файлом .py в командной строке (при помощи команды cd)
# Запустить команду pyinstaller не забудьте указать имя вашего скрипта

# pyinstaller --onefile main.py --name fkr_email.exe

# Всё - у вас в папке появится папка src и там будет .exe файл.
