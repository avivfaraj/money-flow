
# if __name__ == "__main__" or __name__ == "Income":
# 	from Transaction import Transaction
# else:
# 	from .Transaction import Transaction

from transaction import Transaction

class Income(Transaction):

	def __init__(self, ID = "", details = "", salary = "", date = "" ):
		self.ID = ID
		self.details = details
		self.total = salary
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
	first = Income(ID = 1, details = "Income from USAA", salary = 4.5)
	print(first)
# # datetime.date(2021, 12, 3)