#Working with OOP

class BankAccount:   #Creating a class called BankAccount
    def __init__(self, account_balance= 0):   #self value and initiating account_balance to 0

        self.account_balance = account_balance

    def deposit(self, amount):
        if amount >0:
            self.account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive. ")
           # print(f"Your new account balance is{total}.")


    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self, ):
        print(f"Current Balance: ${float(self.account_balance):.2f}")


