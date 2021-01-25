class BankAccount:

    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount

    def withdraw_cash(self, amount):
        if amount < 0:
            return

        if amount > self.cash:
            amount = self.cash

        self.cash -= amount
        return amount

    def print_info(self):
        print(f"{self.number} {self.cash}")



