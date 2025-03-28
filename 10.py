class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner}, ваш рахунок поповнено на {amount} грн. Новий баланс: {self.balance} грн.")
        else:
            print("Сума поповнення повинна бути більше 0!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner}, ви зняли {amount} грн. Новий баланс: {self.balance} грн.")
        else:
            print("Недостатньо коштів або некоректна сума!")

    def __str__(self):
        return f"Рахунок {self.account_number} (Власник: {self.owner}, Баланс: {self.balance} грн)"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, account_number, balance=0):
        if account_number in self.accounts:
            print("Рахунок з таким номером вже існує!")
        else:
            self.accounts[account_number] = BankAccount(owner, account_number, balance)
            print(f"Рахунок {account_number} створено для {owner}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)

        if sender and receiver:
            if sender.balance >= amount and amount > 0:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Переказ {amount} грн з {from_acc} на {to_acc} успішно здійснено!")
            else:
                print("Недостатньо коштів для переказу або некоректна сума!")
        else:
            print("Один або обидва рахунки не знайдено!")

    def show_accounts(self):
        if not self.accounts:
            print("У банку немає рахунків.")
        else:
            print("Список рахунків у банку:")
            for account in self.accounts.values():
                print(account)

bank = Bank()

bank.create_account("Іван Петренко", "12345", 5000)
bank.create_account("Оксана Коваль", "67890", 3000)

acc1 = bank.get_account("12345")
acc2 = bank.get_account("67890")

acc1.deposit(2000)
acc1.withdraw(1000)
bank.transfer("12345", "67890", 1500)

bank.show_accounts()