class OrderCommand:
    # Базовый класс для команд заказа
    def execute(self):
        # Абстрактный метод для выполнения команды
        pass

class OrderAddCommand(OrderCommand):
    # Команда добавления заказа
    def __init__(self, order_id):
        # Инициализация с идентификатором заказа
        self.id = order_id

    def execute(self):
        # Выполнение команды добавления заказа
        print(f"Adding order: {self.id}")

class OrderPayCommand(OrderCommand):
    # Команда оплаты заказа
    def __init__(self, order_id):
        # Инициализация с идентификатором заказа
        self.id = order_id

    def execute(self):
        # Выполнение команды оплаты заказа
        print(f"Paying order: {self.id}")

class OrderCancelCommand(OrderCommand):
    # Команда отмены заказа
    def __init__(self, order_id):
        # Инициализация с идентификатором заказа
        self.id = order_id

    def execute(self):
        # Выполнение команды отмены заказа
        print(f"Cancel order: {self.id}")

class CommandProcessor:
    # Класс для обработки команд
    def __init__(self):
        # Инициализация очереди команд
        self.queue = []

    def add_to_queue(self, order_command):
        # Добавление команды в очередь
        self.queue.append(order_command)

    def process_commands(self):
        # Выполнение всех команд в очереди
        for command in self.queue:
            command.execute()
        # Очистка очереди после выполнения всех команд
        self.queue.clear()

if __name__ == "__main__":
    # Точка входа программы
    command_processor = CommandProcessor()
    # Создание экземпляра класса обработчика команд
    command_processor.add_to_queue(OrderAddCommand(1))
    command_processor.add_to_queue(OrderAddCommand(2))
    command_processor.add_to_queue(OrderPayCommand(2))
    command_processor.add_to_queue(OrderCancelCommand(1))
    # Добавление команд в очередь обработчика
    command_processor.process_commands()
    # Выполнение всех команд в очереди
