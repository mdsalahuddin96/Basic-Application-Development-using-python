class Animal:
	def __init__(self, name):
		self.name = name
		print(self.name + " was adopted.")

def run(self):
	print("running!")

class Turtle(Animal):
	def run(self):
		print("running slowly!")

tim = Turtle("tim")
tim.run()
