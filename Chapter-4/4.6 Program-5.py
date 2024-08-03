import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print(f"The area of the circle is: {circle.area()}")
