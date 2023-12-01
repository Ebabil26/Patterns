# Определяем абстрактный класс Donut (пончик)
class Donut:
    def eat(self):  # Абстрактный метод eat, который будет переопределен в подклассах
        pass

# Классы-подклассы, представляющие конкретные типы пончиков: вишневый, шоколадный, заварной
class CherryDonut(Donut):
    def eat(self):
        print("Мммм, это пончик с вишней")

class ChocolateDonut(Donut):
    def eat(self):
        print("Оооо, это шоколадный пончик")

class CustardDonut(Donut):
    def __init__(self):
        self.calorie = "Много"  # Добавляем атрибут calorie для представления калорийности пончика

    def eat(self):
        print("Уж ты, любимый пончик Леонида с заварным кремом")

# Перечисление DonutType для различных типов пончиков
class DonutType:
    cherry = 1
    chocolate = 2
    custard = 3

# Фабрика для производства пончиков
class DonutFactory:
    def bake(self, type):
        # Создаем пончик определенного типа, в зависимости от входного параметра type
        if type == DonutType.cherry:
            return CherryDonut()
        elif type == DonutType.chocolate:
            return ChocolateDonut()
        elif type == DonutType.custard:
            return CustardDonut()

if __name__ == "__main__":
    # Создаем экземпляр фабрики
    donut_factory = DonutFactory()
    
    # Пекарь производит пончик для Леонида (в данном случае - заварной)
    donut_for_leonid = donut_factory.bake(DonutType.custard)
    
    # Леонид съедает пончик
    donut_for_leonid.eat()
    
    # Если пончик является типом CustardDonut, выводим его калорийность
    if isinstance(donut_for_leonid, CustardDonut):
        print(f"Калорийность: {donut_for_leonid.calorie}")
