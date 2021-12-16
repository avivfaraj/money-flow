
class Person(object):

	ID : int
	name : str
	accounts : list

	def __init__(self, id_ = None, name = "", accounts = []):
		self.ID = id_
		self.name = name
		self.accounts = accounts

	@property
	def ID(self):
		return self._ID
	
	@ID.setter
	def ID(self, id_ = ""):
		if id_:
			self._ID = id_
		else:
			raise ValueError("ID must be positive")

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, name = ""):
		if isinstance(name, str):
			if name:
				self._name = name
			else:
				raise ValueError("Name was empty")
		else:
			raise TypeError("Name must be a string")

	@property
	def accounts(self):
		return self._accounts
	
	@accounts.setter
	def accounts(self, accounts = []):
		self._accounts = accounts

	def new_account(self):
		# To Do
		pass


	def __str__(self):
		return ("ID: " + str(self.ID) +
				"\nName: " + self.name)


if __name__ == "__main__":

	a = Person(id_ = 1, name = "Aviv")
	print(a)
