import logging
import os
import time

import requests
import telegram
from dotenv import load_dotenv
from requests.exceptions import RequestException
from telegram import TelegramError

from exceptions import ErrorSendMessage, NegativeStatusCode, UrlError

load_dotenv()

PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
TELEGRAM_RETRY_TIME = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}

HOMEWORK_STATUSES = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}

logging.basicConfig(
    level=logging.DEBUG,
    filename='program.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


def send_message(bot, message):
    """Бот отправляет сообщение в Телеграм чат."""
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        logger.info('Отпралено сообщение в Телеграм чат')
    except TelegramError:
        error_message = 'Не удалось отправить сообщение'
        logger.error(error_message)
        raise ErrorSendMessage(error_message)


def get_api_answer(current_timestamp):
    """Запрос к эндпоинту API."""
    timestamp = current_timestamp or int(time.time())
    params = {'from_date': timestamp}
    try:
        response = requests.get(url=ENDPOINT, headers=HEADERS, params=params)
    except RequestException:
        error_message = f'Сбой в работе: URL {ENDPOINT} недоступен'
        logger.error(error_message)
        raise UrlError(error_message)
    if response.status_code != 200:
        error_message = (f'Сбой в работе: URL {ENDPOINT} недоступен'
                         f'Код ответа API: {response.status_code}')
        logger.error(error_message)
        raise NegativeStatusCode(error_message)
    try:
        return response.json()
    except ValueError:
        error_message = 'В ответе сервера невалидный файл'
        logger.error(error_message)


def check_response(response):
    """Проверка ответа API на корректность."""
    if not isinstance(response, dict):
        error_message = 'Ответ API не является словарем'
        logger.error(error_message)
        raise TypeError(error_message)
    if 'homeworks' not in response:
        error_message = 'Ответ не содержит ключ ["homeworks"]'
        logger.error(error_message)
        raise KeyError(error_message)
    homeworks = response['homeworks']
    if not isinstance(homeworks, list):
        error_message = 'Ответ API не является списком'
        logger.error(error_message)
        raise TypeError(error_message)
    if len(homeworks) == 0:
        error_message = 'В ответе API нет домашнего задания'
        logger.error(error_message)
        raise IndexError(error_message)
    return response


def parse_status(homework):
    """
    Извлечение из информации статуса конкретной домашней работы.
    В случае успеха возвращает строку из словаря "HOMEWORK_STATUSES".
    """
    homeworks_keys = ('status', 'homework_name')
    for key in homeworks_keys:
        if key not in homework:
            error_message = f'В словаре "homeworks" нет ключа {key}'
            logger.error(error_message)
            raise KeyError(error_message)
    homework_status = homework['status']
    homework_name = homework['homework_name']
    if homework_status not in HOMEWORK_STATUSES:
        error_message = 'Неизвестый статус домашнего задания'
        logger.error(error_message)
        raise KeyError(error_message)
    verdict = HOMEWORK_STATUSES[homework_status]
    return f'Изменился статус проверки работы "{homework_name}". {verdict}'


def check_tokens():
    """
    Проверка доступности переменных окружения.
    Если отсутсвует хотябы одна переменная вернуть False.
    """
    Tokens = {
        'PRACTICUM_TOKEN': PRACTICUM_TOKEN,
        'TELEGRAM_TOKEN': TELEGRAM_TOKEN,
        'TELEGRAM_CHAT_ID': TELEGRAM_CHAT_ID
    }
    error_message = 'Отсутсвует токен:'
    for keys, values in Tokens.items():
        if values == "None":
            logger.critical(f'{error_message} {keys}')
            return False
        elif values is None:
            logger.critical(f'{error_message} {keys}')
            return False
    return True


def main():
    """Основная логика работы бота."""
    if check_tokens() is False:
        raise ValueError('Отсутсвует переменная окружения')
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    current_timestamp = int(time.time())
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text='Бот активирован!')
    while True:
        try:
            response = get_api_answer(current_timestamp)
            homework = check_response(response)
            message = parse_status(homework['homeworks'][0])
            send_message(bot, message)
            current_timestamp = response.get(
                'current_date') or int(time.time())
        except Exception as error:
            message = f'Сбой в работе программы: {error}'
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
            logger.exception(message)
        else:
            message = 'Сообщение успешно отправлено'
            logger.info(message)
        finally:
            time.sleep(TELEGRAM_RETRY_TIME)


if __name__ == '__main__':
    main()
