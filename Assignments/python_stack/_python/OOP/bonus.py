class BankAccount:
    def __init__(self, int_rate, balance=0): 
            self.int_rate=int_rate
            self.balance=balance

    def deposit(self, amount):
            self.balance+=amount
            return self
            
    def withdraw(self, amount):
            if(self.balance>0):
                self.balance-=amount
            else:
                print("Insufficient funds:Charging a $5 fee")
                self.balance-=5
            return self
            
    def display_account_info(self):
            print("balance:$"+str(self.balance))
            return self
    def yield_interest(self):
            if(self.balance>0):
                self.balance+=(self.balance*self.int_rate)
            return self
		

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.current_account = BankAccount(int_rate=0.02, balance=0)
        self.saving_account = BankAccount(int_rate=0.02, balance=0)


    def make_deposit(self, amount,choice):
        if(choice=="current"):
            self.current_account.deposit(amount)	
        elif(choice=="saving"):
             self.saving_account.deposit(amount)

    def make_withdrawal(self, amount,choice):
        if(choice=="current"):
            self.current_account.withdraw(amount)
        elif(choice=="saving"):
             self.saving_account.withdraw(amount)
    def display_user_balance(self,choice):
            if(choice=="current"):
                self.current_account.display_account_info()
            elif(choice=="saving"):
                self.saving_account.display_account_info()


imas = User("imas","imassamirammal97@gmail.com")
sami = User("sami","samirammal60@gmail.com")

imas.make_deposit(100,"current")
imas.make_deposit(200000000000,"saving")
imas.display_user_balance("current")
imas.display_user_balance("saving")
