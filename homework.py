from pprint import pprint
import os

import requests
import telegram
from telegram.ext import CommandHandler, Updater
from telegram import ReplyKeyboardMarkup, Bot

from dotenv import load_dotenv

load_dotenv()

PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

RETRY_TIME = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}

### Проверка работы практикум Токена
payload = {'from_date': 1640446000} # 25 декабря 2021
h_status = requests.get(url=ENDPOINT, headers=HEADERS, params=payload)
pprint(h_status.json().get('homeworks'))
###

HOMEWORK_STATUSES = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}


def send_message(bot, message):
    pass
    # Отправляет сообщение в Телеграм чат (TELEGRAM_CHAT_ID)
    # Принимает на вход два параметра экземпляр класса Bot и строка с текстом сообщения
    ...


def get_api_answer(current_timestamp):
    pass
    # Запрос к единственному эндпоинту API
    # В случае успешного запроса венуть ответ API и преобразовать json()
    timestamp = current_timestamp or int(time.time())
    params = {'from_date': timestamp}

    ...


def check_response(response):
    pass
    # Проверка ответа API на корректность.
    # В качестве параметра ответ API приведенный к типам данных Python
    # ключ 'homeworks'
    ...


def parse_status(homework):
    pass
    # Извлекает из информации статус конкретной домашней работы
    # Получает только один элемент из списка домашних работ
    # В случае успеха возвращает в Телеграм строку из словаря 'HOMEWORK_STATUSES'
    homework_name = ...
    homework_status = ...

    ...

    verdict = ...

    ...

    return f'Изменился статус проверки работы "{homework_name}". {verdict}'


def check_tokens():
    pass
    # Проверка доступности переменных окружения
    # Если отсутсвует хотябы одна переменная вернуть False 
    ...


def main():
    pass
    """Основная логика работы бота."""
    # Сделать запрос API
    # Проверить ответ
    # Если есть обновления получить статус работы из обновления
    # и отправить в Телеграм
    # Подождать время и сделать новый запрос
    ...
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    current_timestamp = int(time.time())

    ...

    while True:
        try:
            response = ...

            ...

            current_timestamp = ...
            time.sleep(RETRY_TIME)

        except Exception as error:
            message = f'Сбой в работе программы: {error}'
            ...
            time.sleep(RETRY_TIME)
        else:
            ...


# if __name__ == '__main__':
#    main()
