from abc import ABC, abstractmethod

class Payment(ABC):

	ID : int
	company : str
	account_num : int

	@abstractmethod
	def __init__(self):
		pass
		
	@property
	def ID(self):
		return self._ID

	@ID.setter
	def ID(self, value = -1):
		if value:
			if isinstance(value, int) and value > 0 and len(str(value)) == 4:
				self._ID = value
			else:
				raise ValueError("ID is not valid")
		else:
			raise NotImplementedError("ID is required")

	@property
	def company(self):
		return self._company

	@company.setter
	def company(self, value = "" ):
		if value:
			self._company = value
		else:
			raise ValueError("Card Company is missing!")

	@property
	def account_num(self):
		return self._account_num

	@account_num.setter
	def account_num(self, value = None):
		if value:
			if not isinstance(value,int):
				raise TypeError("Account Number must be an integer")
			else:
				self._account_num = value
		else:
			raise ValueError("Account Number is None. It must be an integer")

