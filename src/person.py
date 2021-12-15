
class Person(object):

	ID : int
	name : str
	accounts : list

	def __init__(self, id_ = None, name = "", accounts = []):
		self.set_ID(id_)
		self.set_name(name)
		self.set_accounts(accounts)

	def set_ID(self, id_ = ""):
		if id_:
			self.ID = id_
		else:
			raise ValueError("ID must be positive")

	def set_name(self, name = ""):
		if isinstance(name, str):
			if name:
				self.name = name
			else:
				raise ValueError("Name was empty")
		else:
			raise TypeError("Name must be a string")

	def set_accounts(self, accounts = []):
		self.accounts = accounts


	def get_ID(self):
		return self.ID

	def get_name(self):
		return self.name

	def get_accounts(self):
		return self.accounts

	def new_account(self):
		# To Do
		pass


	def __str__(self):
		return ("ID: " + str(self.get_ID()) +
				"\nName: " + self.get_name())



a = Person(id_ = 1, name = "Aviv")
print(a)
