class Account:
    def __init__(self,balance):
        self.balance1 = balance

    def get_balance(self):
        return self.balance1

acc = Account(1000)
print(acc.get_balance())

