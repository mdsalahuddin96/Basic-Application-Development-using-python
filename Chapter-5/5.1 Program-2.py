class Animal:
    def __init__(self,name):
        self.name =name
        print(self.name+"was adopted.")
    def run(self):
        print("running!")
class Dog(Animal):
    def bark(self):
        print("woof!")
spot=Dog("spot")
spot.run()
