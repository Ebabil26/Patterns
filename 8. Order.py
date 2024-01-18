# Базовый класс для команд заказа
class OrderCommand:
    # Абстрактный метод для выполнения команды
    def execute(self):
        pass

# Команда добавления заказа
class OrderAddCommand(OrderCommand):
    # Инициализация с идентификатором заказа
    def __init__(self, order_id):
        self.id = order_id

    # Выполнение команды добавления заказа
    def execute(self):
        print(f"Adding order: {self.id}")

# Команда оплаты заказа
class OrderPayCommand(OrderCommand):
    # Инициализация с идентификатором заказа
    def __init__(self, order_id):
        self.id = order_id

    # Выполнение команды оплаты заказа
    def execute(self):
        print(f"Paying order: {self.id}")

# Команда отмены заказа
class OrderCancelCommand(OrderCommand):
    # Инициализация с идентификатором заказа
    def __init__(self, order_id):
        self.id = order_id

    # Выполнение команды отмены заказа
    def execute(self):
        print(f"Cancel order: {self.id}")

# Класс для обработки команд
class CommandProcessor:
    # Инициализация очереди команд
    def __init__(self):
        self.queue = []

    # Добавление команды в очередь
    def add_to_queue(self, order_command):
        self.queue.append(order_command)

    # Выполнение всех команд в очереди
    def process_commands(self):
        for command in self.queue:
            command.execute()
        # Очистка очереди после выполнения всех команд
        self.queue.clear()

# Точка входа программы
if __name__ == "__main__":
    # Создание экземпляра класса обработчика команд
    command_processor = CommandProcessor()
    
    # Добавление команд в очередь обработчика
    command_processor.add_to_queue(OrderAddCommand(1))
    command_processor.add_to_queue(OrderAddCommand(2))
    command_processor.add_to_queue(OrderPayCommand(2))
    command_processor.add_to_queue(OrderCancelCommand(1))
    
    # Выполнение всех команд в очереди
    command_processor.process_commands()
