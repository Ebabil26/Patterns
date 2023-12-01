# Через функцию:
# Определяем тип стратегии печати как функцию, принимающую строку и возвращающую строку
PrintStrategy = lambda s: str

# Функция для преобразования строки в нижний регистр
def low_cased(s: str) -> str:
    return s.lower()

# Класс принтера, принимающий стратегию печати
class Printer:
    def __init__(self, print_strategy: PrintStrategy):
        self.print_strategy = print_strategy
    
    # Метод печати, использующий выбранную стратегию печати
    def print_str(self, text: str):
        print(self.print_strategy(text))

# Примеры использования:

# Создаем принтер с стратегией печати в нижнем регистре
printer1 = Printer(low_cased)
printer1.print_str("LalAlA")

# Создаем принтер с lambda-функцией, преобразующей строку в верхний регистр
printer2 = Printer(lambda s: s.upper())
printer2.print_str("LalAlA")

# Еще один принтер с lambda-функцией, преобразующей строку в верхний регистр
printer3 = Printer(lambda s: s.upper())
printer3.print_str("LalAlA")

# Через класс:
# Базовый класс стратегии печати
class PrintStrategy:
    def strategy(self, text: str) -> str:
        pass

# Конкретная стратегия печати в нижнем регистре
class LowerPrintStrategy(PrintStrategy):
    def strategy(self, text: str) -> str:
        return text.lower()

# Класс принтера, принимающий стратегию печати
class Printer:
    def __init__(self, print_strategy: PrintStrategy):
        self.print_strategy = print_strategy
    
    # Метод печати, использующий выбранную стратегию печати
    def print_str(self, text: str):
        print(self.print_strategy.strategy(text))

# Пример использования:

# Создаем принтер с конкретной стратегией печати в нижнем регистре
printer1 = Printer(LowerPrintStrategy())
printer1.print_str("LalAlA")

