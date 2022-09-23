
from unicodedata import name


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print("this account is for user "+self.name+" current balance is "+ str(self.account_balance))
    def transfer_money(self, other_user, amount):
        other_user.account_balance+=amount
        print("the current user is "+self.name+" with balance "+str(self.account_balance))
        print("amount of value " +str(amount) +" had been trasfered to  "+other_user.name+" sucessfuly and the current balance of user "+other_user.name+" is " +str(other_user.account_balance))
 
        
        



imas = User("imas","imassamirammal97@gmail.com")
sami = User("sami","samirammal60@gmail.com")
ibtisam = User("ibtisam","ibtisam@gmail.com")

imas.make_deposit(100)
imas.make_deposit(200)
imas.make_deposit(300)
imas.make_withdrawal(100)
imas.display_user_balance()
sami.make_deposit(200)
sami.make_deposit(500)
sami.make_withdrawal(200)
sami.make_withdrawal(100)
sami.display_user_balance()
ibtisam.make_deposit(1000)
ibtisam.make_withdrawal(200)
ibtisam.make_withdrawal(400)
ibtisam.make_withdrawal(100)
ibtisam.display_user_balance()

imas.transfer_money(ibtisam,500)

