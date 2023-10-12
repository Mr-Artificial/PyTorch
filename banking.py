class Banking:
    def __init__(self, password, balance, withdraw, deposit, statement):
        self.password = password
        self.balance = int(balance)
        self.withdraw = int(withdraw)
        self.deposit = int(deposit)
        self.statement = statement

    def check_balance(self, balance):
        return balance

    def withdraw_funds(self, withdraw, balance):
        new_balance = balance - withdraw
        return "Your new account value is: " + str(new_balance) + "$, you withdrew: " + str(withdraw) + "$\n"
