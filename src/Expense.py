from transaction import Transaction
from datetime import datetime

class Expense(Transaction):

	def __init__(self, ID = "",
	 			 details = "",
	 			 date = "",
	 			 unit_price = "",
	 			 amount = "" ):
		self.ID = ID
		self.details = details
		self.date = date
		self.amount = amount
		self.unit_price = unit_price
		self.total = (self.unit_price , self.amount)

	@property
	def total(self):
		return self._total

	@total.setter
	def total(self, value):
		a,b = value
		self._total = a * b


	@property
	def unit_price(self):
		return self._unit_price

	@unit_price.setter
	def unit_price(self, value = "" ):
		if isinstance(value, (float, int)):
			if value > 0:
				self._unit_price = value
			else:
				raise ValueError("Price Must be Positive")
		else:
			raise TypeError("Price must be either an iteger or float")


	@property
	def amount(self):
		return self._amount

	@amount.setter
	def amount(self, value = "" ):
		if isinstance(value, (int)):
			if value > 0:
				self._amount = value
			else:
				raise ValueError("Amount Must be Positive")
		else:
			raise TypeError("Price must be either an iteger or float")



	def __str__(self):
		price = "{:,.2f} $".format(self.total)

		return ("Date: " + self.date_str() +
				"\nTime: " + self.time_str() +
				"\nDetails: "+ self.details +
				"\nTotal Income: "+price)


# test
# first = Expense(ID = 1,
# 			 	details = "Bike shoes",
# 			 	date = datetime(2021, 2,4,5,6),
# 			 	unit_price = 4,
# 			 	amount = 5)
# print(first)
# datetime.date(2021, 12, 3)