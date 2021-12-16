from flow.src.transaction import Transaction
from datetime import datetime as dt

class Deposit(Transaction):

	ID : int
	details : str
	total : float
	date : dt

	def __init__(self, ID = "", details = "", total = None, date = dt.now() ):
		self.ID = ID
		self.details = details
		self.total = total
		self.date = date

	@property
	def total(self):
		return self._total

	@total.setter
	def total(self, value = "" ):
		if isinstance(value,(float, int)):
			if value > 0:
				self._total = value
			else:
				raise ValueError("Salary must be positive")
		else:
			raise TypeError("Salary must be a number")

	def __str__(self):
		price = "{:,.2f} $".format(self.total)
		return ("Date: " + self.date_str() +
				"\nTime: " + self.time_str() +
				"\nDetails: "+ self.details +
				"\nTotal Income: "+ price)


if __name__ == "__main__":

	# test
	first = Deposit(ID = 1, details = "Income from ASC", total = 3)
	print(first)
