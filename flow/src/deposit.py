from flow.src.transaction import Transaction
from flow.src.wire_transfer import Wire
from flow.src.cheque import Cheque
from flow.src.payment import Payment
from datetime import datetime as dt
from typing import Union


class Deposit(Transaction):

	# Attributes
	ID: int
	details: str
	total: float
	date: dt
	payment: Union[Cheque,Wire]

	# Note: Card is not part of payment
	# because an income is usually either
	# a wire transfer or a cheque.

	def __init__(self, 
				 ID = "", 
				 details = "", 
				 total = None, 
				 date = dt.now(),
				 payment: Payment = None):
		self.ID = ID
		self.details = details
		self.total = total
		self.date = date
		self.payment = payment

	@property
	def total(self):
		return self._total

	@total.setter
	def total(self, value = "" ):
		if isinstance(value,(float, int)):
			if value > 0:
				self._total = value
			else:
				raise ValueError("Deposit must be positive")
		else:
			raise TypeError("Deposit must be a number")

	def __str__(self):
		price = "{:,.2f} $".format(self.total)
		return ("Date: " + self.date_str() +
				"\nTime: " + self.time_str() +
				"\nDetails: "+ self.details +
				"\nTotal Income: "+ price+
				"\nPayment " + str(self.payment))


if __name__ == "__main__":

	# test
	w = Wire(4010, 
			 "Bank of America", 
			 4111,
			 "Myself",
			 "Work",
			 "Domestic",
			 "Salary")

	first = Deposit(ID = 1, details = "Income from ASC", total = 3, payment = w)
	print(first)
