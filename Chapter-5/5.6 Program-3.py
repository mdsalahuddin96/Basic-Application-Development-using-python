 # Creating a Base class
class Base:
	def __init__(self):
		self.a = "CST"
		self.__c = "CSE"
# Creating a derived class
class Derived(Base):
	def __init__(self):
		# Calling constructor of Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c) #Attempt to access private member
# Driver code
obj1 = Base()
print(obj1.a)


