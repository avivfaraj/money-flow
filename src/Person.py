
class Person(object):
	# def setID(self, id_ = ""):
	# 	if id_:
	# 		self.id = id_
	# 	else:
	# 		self.id = 12222

	def __init__(self, id_ = None, name = "", accounts = []):
		self.setID(id_)

	def setID(self, id_ = ""):
		if id_:
			self.id = id_
		else:
			self.id = 12222


a = Person()
print(a.id)