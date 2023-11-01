class Banking:
    def __init__(self, username, password, balance, withdraw, deposit, statement):
        self.username = username
        self.password = password
        self.balance = int(balance)
        self.withdraw = int(withdraw)
        self.deposit = int(deposit)
        self.statement = statement

    def account_info(self, username, balance, statement):
        return username + "'s account info: \n" +"\tBalance: " + str(balance) + "\n\tStatement: " + str(statement)
    def check_balance(self, balance):
        return balance

    def withdraw_funds(self, withdraw, balance):
        new_balance = balance - withdraw
        return "Your new account value is: " + str(new_balance) + "$, you withdrew: " + str(withdraw) + "$\n"

    def deposit_fund(self, balance, deposit):
        new_balance = balance + deposit
        return "Your new account value is: " + str(new_balance) + "$, you deposited: " + str(deposit) + "$\n"