from flow.src.card import Card 

class Debit(Card):

	_ID : int
	_company : str
	_account_num : int
	_benefits : list

	def __init__(self, ID = None, company = "", account_num = None, beneifts_ls = []):
		self.ID = ID
		self.company = company
		self.account_num = account_num
		self.beneifts = beneifts_ls

	def __str__(self):
		benefits = ",".join(self.beneifts)
		return ("ID:" + str(self.ID) +
			  "\nCompany: " + self.company + 
			  "\nAccount Number: "+ str(self.account_num) + 
			  "\nBenefits: " + benefits )
		


if __name__ == "__main__":
	try:
		a = Debit(ID = 1756, company = "VISA", account_num = 12)
	except Exception as err:
		print(type(err).__name__,": ",str(err))
	print(a)