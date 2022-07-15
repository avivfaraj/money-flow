
class Person(object):

	ID : int
	name : str
	accounts : list

	def __init__(self, 
				 id_ = None, 
				 first_name = "",
				 middle_name = "",
				 last_name = "", 
				 accounts = []):

		self.ID = id_
		self.first_name = first_name
		self.middle_name = middle_name
		self.last_name = last_name
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
	def first_name(self):
		return self._first_name
	
	@first_name.setter
	def first_name(self, fn = ""):
		if isinstance(fn, str):
			if fn:
				self._first_name = fn
			else:
				raise ValueError("Name was empty")
		else:
			raise TypeError("Name must be a string")


	@property
	def middle_name(self):
		return self._middle_name
	
	@middle_name.setter
	def middle_name(self, mn = ""):
		if isinstance(mn, str) and mn:
				self._middle_name = mn
		else:
			self._middle_name = ""

	@property
	def last_name(self):
		return self._last_name
	
	@last_name.setter
	def last_name(self, ln = ""):
		if isinstance(ln, str):
			if ln:
				self._last_name = ln
			else:
				raise ValueError("Last name was empty")
		else:
			raise TypeError("Last name must be a string")

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
		name = self.first_name +" "+ self.last_name
		if self.middle_name:
			name = self.first_name +" " + self.middle_name +" "+ self.last_name
		return ("ID: " + str(self.ID) +
				"\nName: "+ name)


if __name__ == "__main__":

	a = Person(id_ = 1, first_name = "Aviv", last_name = "Farag")
	print(a)
