from flow.src.payment import Payment

class Card(Payment):

	ID : int
	company : str
	account_num : int
	benefits : list
	c_type : str

	def __init__(self,ID = None, company = "", account_num = None, benefits_ls = [], type_ = "Credit"):
		self.ID = ID
		self.company = company
		self.account_num = account_num
		self.benefits = benefits_ls
		self.c_type = type_

	@property
	def benefits(self):
		if self._benefits:
			return self._benefits
		return None

	@benefits.setter
	def benefits(self, benefits_ls):
		if benefits_ls:
			self._benefits = benefits_ls
		else:
			self._benefits = []


	@property
	def c_type(self):
		return self._c_type

	@c_type.setter
	def c_type(self, type_ = "Credit"):
		if type_:
			self._c_type = type_

	def __str__(self):
		temp = "" 
		if self.benefits:
			for benefit in self.benefits:
				temp += benefit + ", "

			temp = temp[:-2]

		return ("ID: " + str(self.ID) +
				"\nBank: " + self.company +
				"\nAccount: "+ str(self.account_num) +
				"\nBenefits: " + temp +
				"\nCard Type: "+ self.c_type)

if __name__ == "__main__":
	try:
		a = Card(ID = 1756, company = "VISA", benefits_ls = ["2% cash back", "Premium traveler"], account_num = 12)
		# print(isinstance(a, Card))
		# print(a.c_type)
	except Exception as err:
		print(type(err).__name__,": ",str(err))
	print(a)

