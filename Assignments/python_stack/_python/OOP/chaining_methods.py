
from unicodedata import name


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("this account is for user "+self.name+" current balance is "+ str(self.account_balance))
        return self
    def transfer_money(self, other_user, amount):
        other_user.account_balance+=amount
        print("the current user is "+self.name+" with balance "+str(self.account_balance))
        print("amount of value " +str(amount) +" had been trasfered to  "+other_user.name+" sucessfuly and the current balance of user "+other_user.name+" is " +str(other_user.account_balance))
        return self
        
 
        
        



imas = User("imas","imassamirammal97@gmail.com")
sami = User("sami","samirammal60@gmail.com")
ibtisam = User("ibtisam","ibtisam@gmail.com")

imas.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(100).display_user_balance()

sami.make_deposit(200).make_deposit(500).make_withdrawal(200).make_withdrawal(100).display_user_balance()

ibtisam.make_deposit(1000).make_withdrawal(200).make_withdrawal(400).make_withdrawal(100).display_user_balance()

imas.transfer_money(ibtisam,500)

