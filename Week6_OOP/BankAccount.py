from Person import *


class BankAccount:
    """Model bank account with attributes owner, balance,
    account number """

    ##Constructor
    def __init__(self, owner, account, bal):
        self.owner = owner
        self.account_number = account
        self.balance = bal


    ##Class related methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")


    def get_balance(self):
        return self.balance

    def change_owner(self, new_name):
        self.owner = new_name

    def change_owner_phone(self, new_number):
        self.owner.change_phone_number(new_number)



    ##Nice to have method to print things out
    # def __str__(self):
    #     out = str(self.owner) + " has account " + str(self.account_number)
    #     out = out + " that contains a balance of " + str(self.balance)
    #
    #     return out

    def __repr__(self):
        out = str(self.owner) + " has account " + str(self.account_number)
        out = out + " that contains a balance of " + str(self.balance)

        return out



def tester():
    suzy = Person("Suzy Que", "1111-11-1111","222-222-2222")
    sam = Person("Sam", "9999-99-9999", "888-888-8888")
    suzy_account = BankAccount(suzy, 3456, 10)
    sam_account = BankAccount(sam, 1234, 50)
    print(suzy_account)
    # print(f"Suzy's balance is {suzy_account.balance}")
    # suzy_account.deposit(101)
    # print(f"Suzy's balance is {suzy_account.balance}")
    # print(f"Sam's balance is {sam_account.balance}")



if __name__ == "__main__":
    tester()