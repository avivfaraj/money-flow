from flow.src.payment import Payment

class Card(Payment):

	ID : int
	company : str
	account_num : int
	benefits : list
	c_type : str

	def __init__(self,ID = None, company = "", account_num = None, beneifts_ls = [], type_ = "Credit"):
		self.ID = ID
		self.company = company
		self.account_num = account_num
		self.beneifts = beneifts_ls
		self.c_type = type_
		
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
	
	@property
	def benefits(self):
		return self._benefits

	@benefits.setter
	def benefits(self, benefits_ls):
		if benefits_ls:
			self._benefits = benefits_ls


	@property
	def c_type(self):
		return self._c_type

	@c_type.setter
	def c_type(self, type_ = "Credit"):
		if type_:
			self._c_type = type_


if __name__ == "__main__":
	try:
		a = Card(ID = 1756, company = "VISA", account_num = 12)
		print(isinstance(a, Card))
		print(a.c_type)
	except Exception as err:
		print(type(err).__name__,": ",str(err))
	print(a)

