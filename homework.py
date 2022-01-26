import os

import requests
from telegram.ext import CommandHandler, Updater
from telegram import ReplyKeyboardMarkup

from dotenv import load_dotenv

load_dotenv()

PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

RETRY_TIME = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}


HOMEWORK_STATUSES = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}


def send_message(bot, message):
    # Отправляет сообщение в Телеграм чат (TELEGRAM_CHAT_ID)
    # Принимает на вход два параметра экземпляр класса Bot и строка с текстом сообщения
    ...


def get_api_answer(current_timestamp):
    # Запрос к единственному эндпоинту API
    # В случае успешного запроса венуть ответ API и преобразовать json()
    timestamp = current_timestamp or int(time.time())
    params = {'from_date': timestamp}

    ...


def check_response(response):
    # Проверка ответа API на корректность.
    # В качестве параметра ответ API приведенный к типам данных Python
    # ключ 'homeworks'
    ...


def parse_status(homework):
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
    # Проверка доступности переменных окружения
    # Если отсутсвует хотябы одна переменная вернуть False 
    ...


def main():
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


if __name__ == '__main__':
    main()
