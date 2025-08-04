## Bank Account Class

class BankAccount(object):
    """Models a simple bank account"""
    interest_rate = .05
    number_of_accounts = 0
    ##Constructor
    def __init__(self, owner, aNumber, balance = 0):
        self.owner = owner
        self.accountNum = aNumber
        self.__balance = balance
        BankAccount.number_of_accounts += 1
    def pay_interest(self):
        self.__balance += self.__balance * BankAccount.interest_rate

    @staticmethod
    def change_interest_rate(new_rate):
        BankAccount.interest_rate = new_rate

    ##Other methods
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
         
    def getBalance(self):
        return self.__balance

    def copy(self):
        return BankAccount(self.owner, self.accountNum, self.__balance)
     
    ##Print method
    def __str__(self):
        out = self.owner + " has account number " + str(self.accountNum)
        out = out + " with balance " + str(self.__balance)
        return out


# def pay_interest(amount, bankacct):
#     bankacct.deposit(amount)

def testBankAccount():
     print("Test BankAccount class")
     acct = BankAccount("Joe Account", 456,1)
     acct2 = BankAccount("suzy account", 678,1)
     BankAccount.change_interest_rate(.1)
     acct.pay_interest()
     acct2.pay_interest()

     print(acct)
     print(acct2)
     print(BankAccount.number_of_accounts)
     # acct.deposit(1000)
     # # acct.__balance += 1000
     # print(acct)
     # pay_interest(10, acct)
     # print(acct)
     # acct2 = acct
     # acct3 = acct.copy()
     # print(acct, acct2, acct3)
     # acct.deposit(100)
     # print(acct, acct2, acct3)





if __name__ == "__main__":
    testBankAccount()
    
