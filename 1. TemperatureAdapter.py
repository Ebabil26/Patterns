class TemperatureAdapter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

# Ввод пользователем температуры и выбор типа конвертации
print("Выберите тип конвертации:")
print("1. Цельсий в Фаренгейт")
print("2. Фаренгейт в Цельсий")

choice = input("Ваш выбор (1/2): ")

if choice == '1':
    celsius_temperature = float(input("Введите температуру в градусах Цельсия: "))
    converted_to_fahrenheit = TemperatureAdapter.celsius_to_fahrenheit(celsius_temperature)
    print(f"{celsius_temperature} градусов Цельсия = {converted_to_fahrenheit} градусов Фаренгейта")
elif choice == '2':
    fahrenheit_temperature = float(input("Введите температуру в градусах Фаренгейта: "))
    converted_to_celsius = TemperatureAdapter.fahrenheit_to_celsius(fahrenheit_temperature)
    print(f"{fahrenheit_temperature} градусов Фаренгейта = {converted_to_celsius} градусов Цельсия")
else:
    print("Неверный выбор. Пожалуйста, выберите 1 или 2.")
