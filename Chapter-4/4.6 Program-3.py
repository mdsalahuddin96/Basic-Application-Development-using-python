class triangleArea:
    def __init__(self, a, b, c):
        import math
        if (a + b) > c and (b + c) > a and (a + c) > b:
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print("Triangle Area = ", area)
        else:
            print("Triangle is not possible")

a = float(input("Enter First Arm = "))
b = float(input("Enter Second Arm = "))
c = float(input("Enter Third Arm = "))
tarea = triangleArea(a, b, c)
