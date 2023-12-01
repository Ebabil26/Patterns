class Burger:
    class Builder:
        def __init__(self):
            # Инициализация параметров ингредиентов по умолчанию (все False)
            self.cheese = False
            self.pepperoni = False
            self.lettuce = False
            self.tomato = False

        def add_cheese(self):
            # Добавление сыра в бургер через Builder
            self.cheese = True
            return self

        def add_pepperoni(self):
            # Добавление пепперони в бургер через Builder
            self.pepperoni = True
            return self

        def add_lettuce(self):
            # Добавление салата в бургер через Builder
            self.lettuce = True
            return self

        def add_tomato(self):
            # Добавление помидора в бургер через Builder
            self.tomato = True
            return self

        def build(self):
            # Возвращение экземпляра Burger с текущими ингредиентами Builder
            return Burger(self.cheese, self.pepperoni, self.lettuce, self.tomato)

    def __init__(self, cheese=False, pepperoni=False, lettuce=False, tomato=False):
        # Инициализация бургера с определенными ингредиентами
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.lettuce = lettuce
        self.tomato = tomato

# Создание бургера с ингредиентами
burger = Burger.Builder().add_cheese().add_tomato().build()

# Вывод информации о бургере
print(f"Класть ли в бургер сыр? - {burger.cheese}")
print(f"Класть ли в бургер пепперони? - {burger.pepperoni}")
print(f"Класть ли в бургер листья салата? - {burger.lettuce}")
print(f"Класть ли в бургер помидор? - {burger.tomato}")
