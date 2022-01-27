
import time
import os
import logging
import requests
import telegram

from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

RETRY_TIME = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}

### MY_1 Проверка работы практикум Токена V
# payload = {'from_date': 1641372273} # 5 января 2022
# h_status = requests.get(url=ENDPOINT, headers=HEADERS, params=payload)
# pprint(h_status.json().get('homeworks'))
###

HOMEWORK_STATUSES = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}
### MY_2
# updater = Updater(token=TELEGRAM_TOKEN)
# URL = ENDPOINT
###
logging.basicConfig(
    level=logging.DEBUG,
    filename='program.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


def send_message(bot, message):
    pass
    # Отправляет сообщение в Телеграм чат (TELEGRAM_CHAT_ID)
    # Принимает на вход два параметра экземпляр класса Bot и строка с текстом сообщения
    ...


def get_api_answer(current_timestamp):

    # Запрос к единственному эндпоинту API
    # В случае успешного запроса венуть ответ API и преобразовать json()
    timestamp = current_timestamp or int(time.time())
    headers = HEADERS
    params = {'from_date': timestamp}
    try:
        response = requests.get(url=ENDPOINT, headers=headers, params=params)
        if response.status_code != 200:
            logger.error
            raise ValueError
        return response.json()
    except requests.exceptions.RequestException as error:
        api_answer_error = f'Код API (RequestException): {error}'
        logger.error(api_answer_error)
        raise ValueError
        # pass
    ...


def check_response(response):
    pass
    # Проверка ответа API на корректность.
    # В качестве параметра ответ API приведенный к типам данных Python
    # ключ 'homeworks'
    # homework_statuses = requests.get(url, headers=headers, params=payload)
    # print(homework_statuses.json())
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
    """Основная логика работы бота."""
    # Сделать запрос API
    # Проверить ответ
    # Если есть обновления получить статус работы из обновления
    # и отправить в Телеграм
    # Подождать время и сделать новый запрос
    ...
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    current_timestamp = int(time.time())
    tmp_status = 'reviewing'
    errors = True
    # bot.send_message(chat_id=TELEGRAM_CHAT_ID, text='Проверка статуса!')
    ...
    while True:
        try:
            response = get_api_answer(ENDPOINT, current_timestamp)
            
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
