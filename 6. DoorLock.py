# Интерфейс двери
class Door:
    def open_door(self):
        pass

    def close_door(self):
        pass

# Реализация простой двери
class SimpleDoor(Door):
    def open_door(self):
        print("Дверь открыта")

    def close_door(self):
        print("Дверь закрыта")

# Прокси (Заместитель) для установки пароля на дверь
class SecuredDoor(Door):
    def __init__(self, door):
        self._door = door  # Инициализация внутренней двери
        self._password = ""  # Инициализация пароля

    def open_door(self):
        if self._check_password(self._password):  # Проверка пароля
            self._door.open_door()  # Открытие двери, если пароль верный
        else:
            print("Пароль не верный. Дверь не открылась.")

    def close_door(self):
        self._door.close_door()  # Закрытие двери

    def set_password(self, password):
        self._password = password  # Установка пароля

    def _check_password(self, password):
        return password == "secret"  # Проверка совпадения пароля

# Использование
if __name__ == "__main__":
    simple_door = SimpleDoor()
    secured_door = SecuredDoor(simple_door)  # Создание защищенной двери

    secured_door.open_door()  # Попытка открыть дверь без введенного пароля

    secured_door.set_password("secret")  # Установка пароля
    secured_door.open_door()  # Попытка открыть дверь с введенным паролем
