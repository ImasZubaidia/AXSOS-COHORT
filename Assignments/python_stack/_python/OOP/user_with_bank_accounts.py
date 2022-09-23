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
        self.account = BankAccount(int_rate=0.02, balance=0)


    def make_deposit(self, amount):
        self.account.deposit(amount)	# hmmm...the User class doesn't have an account_balance attribute anymore
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        self.account.display_account_info()