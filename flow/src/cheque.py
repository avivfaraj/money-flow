from flow.src.payment import Payment

class Cheque(Payment):

	ID : int
	company : str
	account_num : int
	pay_to : str
	memo : str

	def __init__(self,
				 id_ = None,
				 company = "",
				 account_num = "",
				 pt = "",
				 memo = ""):
		self.ID = id_
		self.company = company
		self.account_num = account_num
		self.pay_to = pt
		self.memo = memo
		
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
	def pay_to(self):
		return self._pay_to

	@pay_to.setter
	def pay_to(self, value = None):
		if value:
			if not isinstance(value,str):
				raise TypeError("Pay To must be a string")
			else:
				self._pay_to = value
		else:
			raise ValueError("Pay To is missing!")

	@property
	def memo(self):
		return self._memo

	@memo.setter
	def memo(self, value = None):
		if value:
			if not isinstance(value,str):
				raise TypeError("Memo must be a string")
			else:
				self._memo = value
		else:
			raise ValueError("Memo is missing!")


	def __str__(self):

		return ("ID: " + str(self.ID) +
				"\nBank: " + self.company +
				"\nAccount: "+ str(self.account_num) +
				"\nPay To: " + self.pay_to +
				"\nMemo: "+ self.memo)


if __name__ == "__main__":
	
	#test
	ch1 = Cheque(4010, "Bank of America", 4111, "School", "Tuition")
	print(ch1)
