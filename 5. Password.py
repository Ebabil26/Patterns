# Интерфейс File
class File:
    def read(self, name):
        pass

# Реализация базового класса SimpleFile, представляющего файл без защиты
class SimpleFile(File):
    def read(self, name):
        print(f"Читаем файл {name}")

# Класс SecuredFile, представляющий прокси для защиты файла паролем
class SecuredFile(File):
    def __init__(self):
        # Создаем экземпляр SimpleFile для работы с файлом
        self.simple_file = SimpleFile()
        # Переменная для хранения пароля
        self.password = ""

    def read(self, name):
        # Проверяем, совпадает ли введенный пароль с ожидаемым
        if self.password == "vasya":
            # Если пароль верный, позволяем доступ к файлу через SimpleFile
            self.simple_file.read(name)
        else:
            # Если пароль неверный, выводим сообщение об отказе доступа
            print("Пароль неверный. У вас нет разрешения для чтения файла")

# Пример использования паттерна Прокси
def main():
    # Создаем экземпляр SecuredFile
    secured_file = SecuredFile()
    
    # Попытка чтения файла без ввода пароля (должен быть отказ)
    secured_file.read("ImportantInfo")
    
    # Устанавливаем пароль
    secured_file.password = "vasya"
    
    # Попытка чтения файла после установки верного пароля (должно быть разрешено)
    secured_file.read("ImportantInfo")

if __name__ == "__main__":
    main()
