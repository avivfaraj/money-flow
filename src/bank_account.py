from income import Income
from datetime import datetime as dt

class Bank_Account(object):

	ID : int
	name : str
	balance : float
	transactions : list

	def __init__(self,
				 id_ = None,
				 name = "", 
				 balance = None ,
				 transactions = []):
		self.set_ID(id_)
		self.set_name(name)
		self.set_balance(balance)
		self.set_trans(transactions)

	def set_ID(self, id_ = ""):
		if id_:
			self.ID = id_
		else:
			raise ValueError("ID must be positive")

	def set_name(self, name = ""):
		if isinstance(name, str):
			if name:
				self.name = name
			else:
				raise ValueError("Name was empty")
		else:
			raise TypeError("Name must be a string")

	def set_balance(self, balance = None):
		if isinstance(balance, (float,int)):
			self.balance = balance
		else:
			raise TypeError("Balance must be either an integer or float")

	def set_trans(self, transactions = []):
		self.transactions = transactions


	def get_ID(self):
		return self.ID

	def get_name(self):
		return self.name

	def get_balance(self):
		return self.balance

	def get_trans(self):
		return self.transactions

	def update_balance(self, price = 0, income = False):
		if income:
			self.balance += price
		else:
			self.balance -= price


	def add_income(self, ID = None,details = "", salary = 0, date = dt.now()):
		try:
			new_income = Income(ID = ID, details = details, salary = salary, date = date)
		except Exception as err:
			print(type(err).__name__,": ",str(err))
			return False

		self.transactions.append(new_income)
		self.update_balance(new_income.total, True)
		return True

	def add_expense(self, details = "", amount = 1, unit_price = 0):
		pass

	def __str__(self):
		b = "{:,.2f} $".format(self.get_balance())
		return ("ID: " + str(self.get_ID()) +
				"\nName: " + self.get_name()+
				"\nBalance: " + b)



a = Bank_Account(id_ = 1, name = "Aviv", balance = 10)
print(a.transactions)
print(a.add_income(details = "Test 2", salary = 10, date = "a"))
print(a.transactions)
print(a.balance)
