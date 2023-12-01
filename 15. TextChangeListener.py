# Создаем интерфейс для слушателей изменений текста
class TextChangeListener:
    def on_text_change(self, old_text, new_text):
        pass

# Класс, реализующий слушателя изменений текста
class IWillListen(TextChangeListener):
    def __init__(self):
        self.text = ""  # Переменная для хранения текста

    # Метод, вызываемый при изменении текста
    def on_text_change(self, old_text, new_text):
        # Обновляем текст и выводим информацию о старом и новом значении
        self.text = f"Old: {old_text} -> New: {new_text}"
        print(self.text)

# Класс, представляющий текст и уведомляющий слушателей об изменениях
class SomeText:
    def __init__(self):
        self.listeners = []  # Список слушателей
        self._text = ""  # Переменная для хранения текста

    @property
    def text(self):
        return self._text  # Возвращает текущее значение текста

    @text.setter
    def text(self, value):
        # Устанавливает новое значение текста и оповещает слушателей об изменении
        for listener in self.listeners:
            listener.on_text_change(self._text, value)
        self._text = value

# Основная функция программы
def main():
    some_text = SomeText()  # Создаем объект для хранения текста
    listener = IWillListen()  # Создаем слушателя
    some_text.listeners.append(listener)  # Добавляем слушателя к объекту текста

    # Выводим начальное значение текста, меняем его и выводим новые значения
    print(some_text.text)
    some_text.text = "Это новое значение"
    print(some_text.text)
    some_text.text = "тест значение"
    print(some_text.text)

# Запускаем основную функцию при запуске скрипта
if __name__ == "__main__":
    main()
