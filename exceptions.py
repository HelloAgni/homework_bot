class NegativeStatusCode(Exception):
    """Ошибка статуса ответа сервера."""

    pass


class ErrorSendMessage(Exception):
    """Ошибка отправки сообщения."""

    pass


class UrlError(Exception):
    """Ошибка, URL недоступен."""

    pass
