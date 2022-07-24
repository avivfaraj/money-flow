from flow.src.payment import Payment

class Cheque(Payment):

	ID: int
	company: str
	account_num: int
	pay_to: str
	memo: str

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
