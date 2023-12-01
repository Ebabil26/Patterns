# Интерфейс цепочки обязанностей
class HeadersChain:
    def __init__(self):
        self.next = None  # Ссылка на следующий элемент в цепочке

    def add_header(self, headers):
        pass  # Абстрактный метод добавления заголовков, будет переопределен в подклассах

# Класс для формирования заголовка авторизации
class AuthHeader(HeadersChain):
    def __init__(self, token):
        super().__init__()
        self.token = token  # Инициализация токена для заголовка авторизации

    def add_header(self, headers):
        # Добавление заголовка авторизации в список заголовков
        headers.append("Authorization: Bearer {}".format(self.token))
        if self.next:
            return self.next.add_header(headers)  # Передача управления следующему элементу цепочки, если он есть
        return headers  # Возврат сформированных заголовков

# Класс для формирования заголовка Content-Type
class ContentTypeHeader(HeadersChain):
    def __init__(self, content_type):
        super().__init__()
        self.content_type = content_type  # Инициализация типа контента для заголовка Content-Type

    def add_header(self, headers):
        # Добавление заголовка Content-Type в список заголовков
        headers.append("Content-Type: {}".format(self.content_type))
        if self.next:
            return self.next.add_header(headers)  # Передача управления следующему элементу цепочки, если он есть
        return headers  # Возврат сформированных заголовков

# Пример использования шаблона "Цепочка Обязанностей" для формирования заголовков запроса
if __name__ == "__main__":
    # Создание объектов для формирования заголовков
    auth_header = AuthHeader("123")
    content_type_header = ContentTypeHeader("application/json")

    # Установка порядка цепочки обязанностей
    content_type_header.next = auth_header

    # Формирование заголовков запроса
    headers = content_type_header.add_header([])
    print(headers)
