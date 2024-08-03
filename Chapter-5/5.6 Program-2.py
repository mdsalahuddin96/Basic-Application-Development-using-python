 # Creating a base class
class Base:
	def __init__(self):
		# Protected member
		self._a = 2
# Creating a derived class
class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)
obj1 = Derived()
obj2 = Base()
# Calling protected member
print("Accessing protected member of obj1: ", obj1._a)
# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)
