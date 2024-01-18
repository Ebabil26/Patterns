class CelsiusTemperature:
    def __init__(self, temperature):
        # Инициализация объекта CelsiusTemperature с температурой в градусах Цельсия
        self.temperature = temperature

class Temperature:
    temperature = 0.0  # Интерфейс Temperature с полем temperature

class FahrenheitTemperature(Temperature):
    def __init__(self, celsius_temperature):
        super().__init__()
        self.celsius_temperature = celsius_temperature

    @property
    def temperature(self):
        # Геттер для temperature, конвертирующий температуру из Цельсия в Фаренгейты
        return self.convert_celsius_to_fahrenheit(self.celsius_temperature.temperature)

    @temperature.setter
    def temperature(self, temperature_in_f):
        # Сеттер для temperature, конвертирующий температуру из Фаренгейтов в Цельсии
        self.celsius_temperature.temperature = self.convert_fahrenheit_to_celsius(temperature_in_f)

    def convert_fahrenheit_to_celsius(self, f):
        # Вспомогательная функция для конвертации из Фаренгейтов в Цельсии
        return (f - 32) * 5 / 9

    def convert_celsius_to_fahrenheit(self, c):
        # Вспомогательная функция для конвертации из Цельсия в Фаренгейты
        return (c * 9 / 5) + 32

def main():
    celsius_temperature = CelsiusTemperature(36.6)
    fahrenheit_temperature = FahrenheitTemperature(celsius_temperature)

    # Вывод температур до и после конвертации
    print(f"Температура по Цельсию: {celsius_temperature.temperature}")
    print(f"Температура по Фаренгейту: {fahrenheit_temperature.temperature}")

    # Установка новой температуры в Фаренгейтах и вывод результатов
    fahrenheit_temperature.temperature = 451.0
    print(f"Температура по Цельсию: {celsius_temperature.temperature}")
    print(f"Температура по Фаренгейту: {fahrenheit_temperature.temperature}")

    # Изменение температуры в Цельсиях и вывод результатов
    celsius_temperature.temperature = 100.0
    print(f"Температура по Цельсию: {celsius_temperature.temperature}")
    print(f"Температура по Фаренгейту: {fahrenheit_temperature.temperature}")

if __name__ == "__main__":
    main()
