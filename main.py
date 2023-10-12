from banking import *

if __name__ == '__main__':
    oAccount = Banking("abcd", 100, 20, 20, ["14$", "10$", "200$"])
    balance = oAccount.check_balance(100)
    print(str(balance) + '$')
    print(oAccount.withdraw_funds(10, balance))

