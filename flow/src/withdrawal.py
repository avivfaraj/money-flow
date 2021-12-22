from flow.src.transaction import Transaction
from datetime import datetime as dt
from typing import Union
from flow.src.credit import Credit
from flow.src.debit import Debit

class Withdrawal(Transaction):

	ID : int
	details : str
	date : dt
	unit_price : float
	amount : int
	pay_method : str
	card : Union[Credit,Debit, None]

	def __init__(self, ID = "",
	 			 details = "",
	 			 date = dt.now(),
	 			 unit_price = "",
	 			 amount = "",
	 			 pay_method = "Credit",
	 			 card = None):

		self.ID = ID
		self.details = details
		self.date = date
		self.amount = amount
		self.unit_price = unit_price
		self.pay_method = pay_method
		self.card = card
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


	@property
	def card(self):
		return self._card

	@card.setter
	def card(self, value = None):
		if isinstance(value, (Credit,Debit)):
			self._card = value

		elif value is None:
			if self.pay_method in ["Credit", "Debit"]:
				raise ValueError("Card is missing!")
			
			self._card = None

		else:
			raise TypeError("Card's instance accept Credit, Debit or None!")


	def __str__(self):
		price = "{:,.2f} $".format(self.total)

		card_str = ""
		if self.card:
			card_str = ("\nID: "+ str(self.card.ID)+
						"\nCompany: " +str(self.card.company))
		return ("Date: " + self.date_str() +
				"\nTime: " + self.time_str() +
				"\nDetails: "+ self.details +
				"\nTotal Income: "+price +
				"\nPayment Method: "+ self.pay_method+
				"\nCard: " + card_str)

if __name__ == "__main__":

	# test
	a = Credit(ID = 1756, company = "VISA", account_num = 12)
	first = Withdrawal(ID = 1,
				 	details = "Bike shoes",
				 	date = dt(2021, 2,4,5,6),
				 	unit_price = 2,
				 	amount = 5,
				 	pay_method = "Credit",
				 	card = a)

	print(first)

