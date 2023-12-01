# Абстрактный класс работника
class Employee:
    def earned_amount(self):
        pass

# Класс дизайнера
class Designer(Employee):
    def __init__(self, name, salary, bonus=0):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def earned_amount(self):
        # Возвращает сумму зарплаты и бонуса для дизайнера
        return self.salary + self.bonus

    def do_design(self):
        # Метод, выполняющий действия дизайнера
        print("Do Design")

# Класс разработчика
class Developer(Employee):
    def __init__(self, name, salary, bonus=0):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def earned_amount(self):
        # Возвращает сумму зарплаты и бонуса для разработчика
        return self.salary + self.bonus

    def do_developer(self):
        # Метод, выполняющий действия разработчика
        print("Do Developer")

# Класс менеджера
class Manager(Employee):
    def __init__(self, name, salary, bonus=0):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def earned_amount(self):
        # Возвращает только зарплату для менеджера без бонуса
        return self.salary

# Класс Компании (Компоновщик)
class Company:
    def __init__(self):
        self.employees = []  # Список работников в компании

    def add_employee(self, employee):
        # Добавление нового работника в список компании
        self.employees.append(employee)

    def get_salary(self):
        # Возвращает общую заработную плату всей команды
        return sum(employee.earned_amount() for employee in self.employees)

# Использование
if __name__ == "__main__":
    # Создание экземпляров работников различных специализаций
    alica = Designer("Алиса", 19)
    bob = Designer("Боб", 25, 5)
    jon = Developer("Джон", 21)
    alex = Developer("Алекс", 22, 10)
    max_manager = Manager("Мах", 24)

    # Создание компании и добавление в неё сотрудников
    company = Company()
    company.add_employee(alica)
    company.add_employee(bob)
    company.add_employee(jon)
    company.add_employee(alex)
    company.add_employee(max_manager)

    # Вывод общей заработной платы всей команды
    print(f"Заработная плата: {company.get_salary()}")
