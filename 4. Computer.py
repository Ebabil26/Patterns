# Создаем класс Computer, который имеет различные методы для работы с компьютером.
class Computer:
    def get_electric_shock(self):
        print("Ouch!")

    def make_sound(self):
        print("Beep beep!")

    def show_loading_screen(self):
        print("Loading..")

    def bam(self):
        print("Ready to be used!")

    def close_everything(self):
        print("Bup bup bup buzzzz!")

    def sooth(self):
        print("Zzzzz")

    def pull_current(self):
        print("Haaah!")


# Создаем класс ComputerFacade, который предоставляет упрощенный интерфейс для работы с Computer.
class ComputerFacade:
    def __init__(self, computer):
        self.computer = computer

    # Метод turn_on() включает компьютер, выполняя необходимые шаги.
    def turn_on(self):
        self.computer.get_electric_shock()
        self.computer.make_sound()
        self.computer.show_loading_screen()
        self.computer.bam()

    # Метод turn_off() выключает компьютер, выполняя соответствующие действия.
    def turn_off(self):
        self.computer.close_everything()
        self.computer.pull_current()
        self.computer.sooth()


# Функция main() демонстрирует использование паттерна Фасад для управления компьютером.
def main():
    # Создаем объект класса Computer.
    computer = Computer()
    # Создаем объект класса ComputerFacade, передавая объект компьютера в качестве аргумента.
    computer_facade = ComputerFacade(computer)

    # Включаем компьютер через фасад.
    print("Включаем компьютер:")
    computer_facade.turn_on()
    print("\nВыключаем компьютер:")
    # Выключаем компьютер через фасад.
    computer_facade.turn_off()


# Проверяем, запущен ли данный файл напрямую, и вызываем функцию main() в этом случае.
if __name__ == "__main__":
    main()
