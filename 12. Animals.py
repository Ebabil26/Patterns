# Шаг 1: Объявим интерфейс Animal
class Animal:
    def accept(self, visitor):
        pass

# Шаг 2: Обеспечим реализацию интерфейса для каждого класса животных зоопарка
class Monkey(Animal):
    def shout(self):
        print("У-у-у аaaaaаa!")

    def accept(self, visitor):
        # Вызываем соответствующий метод посетителя для обезьяны
        visitor.visit_monkey(self)

class Lion(Animal):
    def roar(self):
        print("Рррррррррр!")

    def accept(self, visitor):
        # Вызываем соответствующий метод посетителя для льва
        visitor.visit_lion(self)

class Dolphin(Animal):
    def speak(self):
        print("Пиу пиу пиу")

    def accept(self, visitor):
        # Вызываем соответствующий метод посетителя для дельфина
        visitor.visit_dolphin(self)

# Шаг 3: Объявим интерфейс Visitor с методами для каждого животного
class Visitor:
    def visit_monkey(self, monkey):
        pass

    def visit_lion(self, lion):
        pass

    def visit_dolphin(self, dolphin):
        pass

# Шаг 4: Создадим класс расширения функциональности животных зоопарка
class SoundVisitor(Visitor):
    def visit_monkey(self, monkey):
        # Визит к клетке с обезьянкой
        print("Вы подошли к клетке с Обезьянкой:")
        monkey.shout()  # Вызываем функцию обезьяны

    def visit_lion(self, lion):
        # Визит к клетке с львом
        print("Вы подошли к клетке со Львом:")
        lion.roar()  # Вызываем функцию льва

    def visit_dolphin(self, dolphin):
        # Визит к бассейну с дельфином
        print("Вы подошли к бассейну с Дельфином:")
        dolphin.speak()  # Вызываем функцию дельфина

# Использование
def main():
    monkey = Monkey()
    lion = Lion()
    dolphin = Dolphin()
    sound_visitor = SoundVisitor()

    # Принимаем посетителя для каждого животного и выводим соответствующий звук
    monkey.accept(sound_visitor)
    print()
    lion.accept(sound_visitor)
    print()
    dolphin.accept(sound_visitor)

if __name__ == "__main__":
    main()
