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
		
first_account=BankAccount(0.01,100)
first_account.deposit(100).deposit(200).deposit(300).withdraw(100).display_account_info()

second_account=BankAccount(0.02)
second_account.deposit(400).deposit(200).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()