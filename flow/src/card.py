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

