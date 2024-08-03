
def my_decorator(func):
    def decorate():
        print("--------------------------------------------------------")
        func()
        print("--------------------------------------------------------")
    return decorate

def print_text():
    print("Diploma in Engineering! using Decorator Funtion Example")

decorated_function = my_decorator(print_text)
decorated_function()

@my_decorator
def print_text():
    print("Hello World!")
print_text()

