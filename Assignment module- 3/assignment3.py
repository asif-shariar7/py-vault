## Create a class BankAccount with a private attribute balance and provide methods deposit() and withdraw() to modify the balance safely so that the balance cannot be accessed directly. Then create two subclasses SavingsAccount and CurrentAccount, each having a method account_type() that prints its respective account type. Demonstrate polymorphism by calling account_type() from different account objects.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit (self, amount):
        if 0 < amount :
            self.__balance += amount
            print("Deposited: ", amount)
        else:
            print("Invalid deposit amount")    

    def withdraw (self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount") 

    def get_balance (self):
        return self.__balance        

class SavingsAccount(BankAccount):
    def account_type(self):
        print("Savings Account")  

class CurrentAccount(BankAccount):
    def account_type(self):
        print("Current Account")  



savings = SavingsAccount(1000)
current = CurrentAccount(2000)

savings.deposit(500)
savings.withdraw(800)
print("Saving Balance: ", savings.get_balance())

## polymorphism
def poly (calls):
    calls.account_type()

poly(SavingsAccount(1000))
poly(CurrentAccount(2000))