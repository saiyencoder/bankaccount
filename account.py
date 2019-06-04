class Account():

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} has been deposited to your account')

    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds')
            return False
        else:
            self.balance -= amount
            print(f'{amount} has been withdrawn from account')
            return True

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f'Account Owner:   {self.name}\nAccount Balace:  ${self.balance}'
