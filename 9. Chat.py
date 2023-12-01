class ChatMediator:
    def __init__(self):
        # Создание списка пользователей чата
        self.users = []

    def add_user(self, user):
        # Добавление пользователя в список
        self.users.append(user)

    def send_message(self, msg, sending_user):
        # Рассылка сообщения всем пользователям, кроме отправителя
        for user in self.users:
            if user != sending_user:  # Проверка, чтобы не отправлять сообщение автору
                user.receive(msg)  # Пользователи получают сообщение


class ChatUser:
    def __init__(self, mediator, name):
        self.mediator = mediator  # Посредник для общения
        self.name = name  # Имя пользователя

    def send(self, msg):
        # Отправка сообщения через посредника
        print(f"{self.name}: Sending Message= {msg}")
        self.mediator.send_message(msg, self)  # Отправка сообщения всем пользователям чата

    def receive(self, msg):
        # Получение сообщения
        print(f"{self.name}: Message received: {msg}")


if __name__ == "__main__":
    # Создание посредника чата
    mediator = ChatMediator()

    # Создание пользователей чата
    user1 = ChatUser(mediator, "Alice")
    user2 = ChatUser(mediator, "Bob")
    user3 = ChatUser(mediator, "Charlie")

    # Добавление пользователей в чат
    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)

    # Пользователи отправляют сообщения
    user1.send("Hello, everyone!")
    user2.send("Hey there!")
