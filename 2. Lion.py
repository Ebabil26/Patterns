# Интерфейс Lion
class Lion:
    def roar(self):
        pass

# Реализация африканского льва
class AfricanLion(Lion):
    def roar(self):
        print("Африканский лев сказал Ррррррр")

# Реализация азиатского льва
class AsianLion(Lion):
    def roar(self):
        print("Азиатский лев сказал Ррррррр")

# Класс для героя
class Hero:
    def find(self, lion):
        print("Герой увидел зверя")
        lion.roar()

# Класс для дикой собаки
class WildDog:
    def bark(self):
        print("Дикая собака сказала Ав-ав-ав")

# Адаптер для дикой собаки
class WildDogAdapter(Lion):
    def __init__(self, wild_dog):
        self.wild_dog = wild_dog

    def roar(self):
        self.wild_dog.bark()

# Использование
if __name__ == "__main__":
    # Создание экземпляров львов
    african_lion = AfricanLion()
    asian_lion = AsianLion()
    hero = Hero()

    # Герой находит и слышит рычание африканского льва
    hero.find(african_lion)

    # Герой находит и слышит рычание азиатского льва
    hero.find(asian_lion)

    # Создание экземпляра дикой собаки
    wild_dog = WildDog()
    
    # Создание адаптера для дикой собаки
    wild_dog_adapter = WildDogAdapter(wild_dog)

    # Герой использует адаптер для слышания "рычания" дикой собаки
    hero.find(wild_dog_adapter)
