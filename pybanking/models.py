class User():
    def __init__(self, name):
        self.name = name

    def show_details(self):
        x = 'Personal details'
        y = 'name: ' + self.name
        z = 'account balance is now £' + str(self.balance)
        result = [x, y, z]
        return result


class Bank(User):
    def __init__(self, name):
        super().__init__(name)
        self.balance = 0

    def deposit(self, amount):
        self.amount = int(amount)
        self.balance = self.balance + self.amount
        return 'account balance after deposit is now £' + str(self.balance)

    def withdraw(self, amount):
        self.amount = int(amount)
        if self.balance-self.amount < 0:
            return "Insufficient funds £" + str(self.balance)

        self.balance = self.balance-self.amount
        return 'account balance after withdraw is now £' + str(self.amount)

    def view_money(self):
        return str(self.balance)
