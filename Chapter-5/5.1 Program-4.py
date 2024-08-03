class Fish:
	def __init__(self):
		self.__size = "big" #private attribute
	def get_size(self):
		print("I'm a " + self.__size + " fish")
	def set_size(self, new_size):
		self.__size = new_size
oscar = Fish()
oscar.get_size()
bert = Fish()
bert.__size = "small" #Attempt to set private attribute directly(Will not work)
bert.get_size()
fin = Fish()
fin.set_size("tiny") #correct way to set private attribute
fin.get_size()
