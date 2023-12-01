# Создаем интерфейс Coffee
class Coffee:
    def get_cost(self):
        raise NotImplementedError
    
    def get_description(self):
        raise NotImplementedError

# Реализация простой чашки кофе
class SimpleCoffee(Coffee):
    def get_cost(self):
        return 25.0
    
    def get_description(self):
        return "Чашка кофе"

# Базовый декоратор
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def get_cost(self):
        return self._coffee.get_cost()

    def get_description(self):
        return self._coffee.get_description()

# Декоратор для добавления молока
class CoffeeWithMilk(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 10.0

    def get_description(self):
        return self._coffee.get_description() + ", с молоком"

# Декоратор для добавления сахара
class CoffeeWithSugar(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 5.0

    def get_description(self):
        return self._coffee.get_description() + ", с сахаром"

# Декоратор для добавления корицы
class CoffeeWithCinnamon(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 5.0

    def get_description(self):
        return self._coffee.get_description() + ", с корицей"

# Пример использования
if __name__ == "__main__":
    # Создаем базовую чашку кофе
    coffee = SimpleCoffee()
    # Добавляем сахар
    coffee = CoffeeWithSugar(coffee)
    # Добавляем молоко
    coffee = CoffeeWithMilk(coffee)
    print(f"Стоимость кофе: {coffee.get_cost()}")
    print(f"Состав кофе: {coffee.get_description()}")

    # Создаем Латте - кофе с молоком и корицей
    latte = CoffeeWithCinnamon(CoffeeWithMilk(SimpleCoffee()))
    print(f"Стоимость латте: {latte.get_cost()}")
    print(f"Состав латте: {latte.get_description()}")
