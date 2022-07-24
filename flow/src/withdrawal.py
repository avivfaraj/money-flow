from flow.src.transaction import Transaction
from datetime import datetime as dt
from typing import Optional
from flow.src.card import Card
from flow.src.payment import Payment
from flow.src.cheque import Cheque
from flow.src.wire_transfer import Wire
from typing import Union


class Withdrawal(Transaction):

	ID: int
	details: str
	date: dt
	unit_price: float
	amount: int
	discount: float
	sector: str
	payment: Payment

	def __init__(self,
				 ID = "",
	 			 details = "",
	 			 date = dt.now(),
	 			 unit_price = "",
	 			 amount = "",
	 			 sector = "", 
	 			 discount = 0,
	 			 payment: Payment = None):

		self.ID = ID
		self.details = details
		self.date = date
		self.amount = amount
		self.unit_price = unit_price
		self.discount = discount
		self.sector = sector
		self.payment = payment
		self.total = (self.unit_price , self.amount, self.discount)

	@property
	def total(self):
		return self._total

	@total.setter
	def total(self, value):
		price, amount, discount = value
		self._total = price * amount - discount 


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
			raise TypeError("Amount must be either an iteger or float")


	@property
	def sector(self):
		return self._sector

	@sector.setter
	def sector(self, value = "" ):
		if isinstance(value, (str)):
			self._sector = value
		else:
			raise TypeError("Sector must be a string")


	@property
	def discount(self):
		return self._discount

	@discount.setter
	def discount(self, value = 0 ):
		if isinstance(value, (int, float)):
			self._discount = value
		else:
			raise TypeError("Discount must be a number")

	@property
	def payment(self):
		return self._payment

	@payment.setter
	def payment(self, value = None):
		if isinstance(value, (Card, Cheque, Wire)):
			self._payment = value

		elif value is None:
			raise ValueError("Payment is missing!")
		
		else:
			raise TypeError("Valid payments type: Card, Cheque and Wire")


	def __str__(self):
		price = "{:,.2f} $".format(self.total)

		return ("Date: " + self.date_str() +
				"\nTime: " + self.time_str() +
				"\nDetails: "+ self.details +
				"\nSector: " + self.sector +
				"\nUnits: "+ str(self.amount) +
				"\nPrice: " + str(self.unit_price) +
				"\nDiscount: "+ str(self.discount) +
				"\nTotal: "+ price +
				"\nPayment Method: "+ str(self.payment))

if __name__ == "__main__":

	# test
	a = Card(ID = 1756, company = "VISA", account_num = 12)
	first = Withdrawal(ID = 1,
				 	details = "Bike shoes",
				 	date = dt(2021, 2,4,5,6),
				 	unit_price = 2,
				 	amount = 5,
				 	sector = "Fashion",
				 	payment = a,
				 	discount = 2)

	print(first)

