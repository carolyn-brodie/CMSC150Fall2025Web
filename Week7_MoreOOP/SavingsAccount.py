from BankAccount import *

class SavingsAccount(BankAccount):

    def __init__(self, owner, aNumber, interest, balance = 0):
        super().__init__(owner, aNumber, balance)
        self.interest_rate = interest



    def payInterest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        out = super().__str__()
        out = out + f" with interest rate {self.interest_rate}"
        return out

 
def test():
    print("tester")
    savings1 = SavingsAccount("Suzy", 1234, .1)
    bank1 = BankAccount("sam", 7890)
    savings1.deposit(100)
    bank1.deposit(200)
    print(savings1)
    print(bank1)
    savings1.payInterest()
    print(savings1)



if __name__ == "__main__":
    test()
