from flow.src.payment import Payment

class Wire(Payment):

	ID : int
	company : str
	account_num : int
	recipient : str
	sender : str
	w_type : str
	details : str

	def __init__(self,
				 id_ = None,
				 company = "",
				 account_num = "",
				 recipient = "",
				 sender = "",
				 w_type = "",
				 details = ""):
		self.ID = id_
		self.company = company
		self.account_num = account_num
		self.recipient = recipient
		self.sender = sender
		self.w_type = w_type
		self.details = details
		
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
	def recipient(self):
		return self._recipient

	@recipient.setter
	def recipient(self, value = None):
		if value:
			if not isinstance(value,str):
				raise TypeError("Recipient must be a string")
			else:
				self._recipient = value
		else:
			raise ValueError("Recipient is missing!")

	@property
	def sender(self):
		return self._sender

	@sender.setter
	def sender(self, value = None):
		if value:
			if not isinstance(value,str):
				raise TypeError("Sender must be a string")
			else:
				self._sender = value
		else:
			raise ValueError("Sender is missing!")


	@property
	def w_type(self):
		return self._w_type

	@w_type.setter
	def w_type(self, value = 'Domestic'):
		if value:
			if not isinstance(value,str):
				raise TypeError("Type must be a string")
			else:
				self._w_type = value
		else:
			raise ValueError("Type is missing!")

	@property
	def details(self):
		return self._details

	@details.setter
	def details(self, value = ""):
		if value:
			if not isinstance(value,str):
				raise TypeError("details must be a string")
			else:
				self._details = value
		else:
			raise ValueError("details is missing!")



	def __str__(self):

		return ("ID: " + str(self.ID) +
				"\nBank: " + self.company +
				"\nAccount: "+ str(self.account_num) +
				"\nRecipient: " + self.recipient +
				"\nSender: "+ self.sender +
				"\nType: " + self.w_type +
				"\nDetails: "+ self.details)


if __name__ == "__main__":
	
	#test
	w = Wire(4010, 
			   "Bank of America", 
			   4111,
			   "Roth",
			   "Michael",
			   "International",
			   "Birthday Present")
	print(w)
