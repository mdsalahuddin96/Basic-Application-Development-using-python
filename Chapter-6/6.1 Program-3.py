def my_decorator(func):
    def decorate():
        print("--------------")
        func()
        print("--------------")
    return decorate

def print_raw():
    print("Bangladesh")

decorated_function = my_decorator(print_raw)
decorated_function()
