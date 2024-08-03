class Calculator:
    """Super class to define addition, subtraction, multiplication, and division."""
    def addition(self, x, y):
        return x + y
    def subtraction(self, x, y):
        return x - y
    def multiplication(self, x, y):
        return x * y
    def division(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'
class SubCalculator(Calculator):
    """Child class to define methods for calculating square and cube."""
    def square(self, x):
        return x * x

    def cube(self, x):
        return x * x * x
my_calculator = SubCalculator()
temp = my_calculator.addition(60, 30)
print("X + Y =", temp)
temp = my_calculator.subtraction(60, 30)
print("X - Y =", temp)
temp = my_calculator.multiplication(60, 30)
print("X * Y =", temp)
temp = my_calculator.division(60, 30)
print("X / Y =", temp)
temp = my_calculator.square(9)
print("Square of 9 =", temp)
temp = my_calculator.cube(5)
print("Cube of 5 =", temp)
