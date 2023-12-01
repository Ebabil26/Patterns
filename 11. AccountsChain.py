class AccountsChain:
    def __init__(self, name, balance, next_account=None):
        self.name = name
        self.balance = balance
        self.next_account = next_account  # Следующий аккаунт в цепочке

    def pay(self, amount):
        if self.can_pay(amount):  # Проверка возможности оплаты с текущего аккаунта
            print(f"Вы оплатили {amount} со счета: {self.name}")
        else:
            if self.next_account is not None:  # Если есть следующий аккаунт в цепочке
                self.next_account.pay(amount)  # Передача запроса следующему аккаунту
            else:
                print("На всех счетах недостаточно средств")

    def can_pay(self, amount):
        return self.balance >= amount  # Проверка достаточности средств для оплаты


class Bank(AccountsChain):
    pass  # Класс банковского счета


class Paypal(AccountsChain):
    pass  # Класс счета Paypal


class Bitcoin(AccountsChain):
    pass  # Класс Bitcoin кошелька


def main():
    bank = Bank("Bank", 300)
    paypal = Paypal("Paypal", 200)
    bitcoin = Bitcoin("Bitcoin", 700)

    # Установим приоритеты оплаты: Bank -> Paypal -> Bitcoin
    bank.next_account = paypal
    paypal.next_account = bitcoin

    # Пример использования
    bank.pay(500)  # Попытка оплаты 500
    bank.pay(900)  # Попытка оплаты 900
    bank.pay(250)  # Попытка оплаты 250


if __name__ == "__main__":
    main()
