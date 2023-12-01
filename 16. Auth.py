class AuthState:
    pass

class Authed(AuthState):
    def __init__(self, name):
        self.name = name

class Unauthed(AuthState):
    pass

class AuthPresenter:
    def __init__(self):
        # Изначально устанавливаем состояние в "неавторизованный"
        self.state = Unauthed()

    @property
    def is_authed(self):
        # Проверяем, авторизован ли пользователь
        return isinstance(self.state, Authed)

    @property
    def user_name(self):
        # Получаем имя пользователя, если авторизован, в противном случае возвращаем "Unknown"
        if isinstance(self.state, Authed):
            return self.state.name
        return "Unknown"

    def login(self, username):
        # Выполняем вход, устанавливая состояние "авторизованный" с указанным именем пользователя
        self.state = Authed(username)

    def logout(self):
        # Выполняем выход, устанавливая состояние в "неавторизованный"
        self.state = Unauthed()

if __name__ == "__main__":
    # Создаем экземпляр AuthPresenter
    auth_presenter = AuthPresenter()

    # Выводим состояние авторизации и имя пользователя до входа
    print(auth_presenter.is_authed)
    print(auth_presenter.user_name)

    # Выполняем вход пользователя с именем "Gleb"
    auth_presenter.login("Gleb")

    # Выводим состояние авторизации и имя пользователя после входа
    print(auth_presenter.is_authed)
    print(auth_presenter.user_name)

    # Выполняем выход пользователя
    auth_presenter.logout()

    # Выводим состояние авторизации и имя пользователя после выхода
    print(auth_presenter.is_authed)
    print(auth_presenter.user_name)
