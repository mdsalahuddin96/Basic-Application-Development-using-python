class Animal:
    def __init__(self, name):
        self.name = name
        print(self.name + " was adopted.")

    def run(self):
        print("running!")

class Turtle(Animal):
    def run(self):
        print("running slowly!")

# Create an instance of Turtle
tim = Turtle("tim")
tim.run()
