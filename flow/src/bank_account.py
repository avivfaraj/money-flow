from flow.src.deposit import Deposit
from flow.src.withdrawal import Withdrawal
from flow.src.card import Card

from datetime import datetime as dt

class Bank_Account(object):

	ID : int
	name : str
	balance : float
	transactions : list

	def __init__(self,
				 ID = None,
				 name = "", 
				 balance = None ,
				 transactions = []):
		self.ID = ID
		self.name = name
		self.balance = balance 
		self.transactions = transactions

	@property
	def ID(self):
		return self._ID

	@ID.setter
	def ID(self, ID = ""):
		if ID:
			self._ID = ID
		else:
			raise ValueError("ID must be positive")

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, name = ""):
		if isinstance(name, str):
			if name:
				self._name = name
			else:
				raise ValueError("Name was empty")
		else:
			raise TypeError("Name must be a string")

	@property
	def balance(self):
		return self._balance
	
	@balance.setter
	def balance(self, balance = None):
		if isinstance(balance, (float,int)):
			self._balance = balance
		else:
			raise TypeError("Balance must be either an integer or float")

	@property
	def transactions(self):
		return self._transactions
	
	@transactions.setter
	def transactions(self, transactions = []):
		self._transactions = transactions

	def update_balance(self, price = 0, income = False):
		if income:
			self.balance += price
		else:
			self.balance -= price


	def add_income(self, ID = None,details = "", salary = 0, date = dt.now()):
		try:
			new_income = Deposit(ID = ID, details = details, total = salary, date = date)
		except Exception as err:
			print(type(err).__name__,": ",str(err))
			return False

		self.transactions.append(new_income)
		self.update_balance(new_income.total, True)
		return True

	def add_expense(self,ID = None, details = "", amount = 1, unit_price = 0, date = dt.now(), pay_method = "Credit", card = None):
		try:
			new_withdrawal = Withdrawal(ID = ID, 
										details = details, 
										date = date, 
										unit_price = unit_price, 
										amount = amount,
										pay_method = pay_method,
										card = card)
		except Exception as err:
			print(type(err).__name__,": ",str(err))
			return False

		self.transactions.append(new_withdrawal)
		self.update_balance(new_withdrawal.total, False)
		return True

	def __str__(self):
		_ = "{:,.2f} $".format(self.balance)
		return ("ID: " + str(self.ID) +
				"\nName: " + self.name +
				"\nBalance: " + _)

if __name__ == "__main__":

	# test
	a = Bank_Account(ID = 1, name = "Aviv", balance = 10)
	c = Card(ID = 1756, company = "VISA", account_num = 12)

	print(a.transactions)
	print(a.add_income(ID = 2,details = "Test 2", salary = 10, date = dt(2021,2,2)))
	print(a.add_expense(ID = 2,details = "Test 2", date = dt(2021,2,2), amount = 1, unit_price = 3, card = c))
	print(a.transactions)
	print(a)