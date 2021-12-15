from abc import ABC, abstractmethod
from datetime import datetime as dt

class Transaction(ABC):
	@abstractmethod
	def __init__(self):
		pass
		
	@property
	def ID(self):
		return self._ID

	@ID.setter
	def ID(self, value = ""):
		if value:
			self._ID = value
		else:
			raise NotImplementedError("ID is required")

	@property
	def details(self):
		return self._details

	@property
	@abstractmethod
	def total(self):
		pass

	@property
	def date(self):
		return self._date

	@details.setter
	def details(self, value = "" ):
		if value:
			self._details = value


	@total.setter
	@abstractmethod
	def total(self, salary):
		pass

	@date.setter
	def date(self, value = None ):
		if value:
			if not isinstance(value,dt):
				raise Exception("Date must be datetime")
			else:
				self._date = value
		else:
			self._date = dt.now()

	def date_str(self):
		return self.date.strftime("%d/%m/%Y")

	def time_str(self):
		return self.date.strftime("%-I:%M %p")
