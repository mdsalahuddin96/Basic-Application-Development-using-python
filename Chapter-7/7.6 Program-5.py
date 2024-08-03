def square(x):
    assert x>=0, 'Only positive numbers are allowed'
    return x*x

try:
    square(-2)
except AssertionError as msg:
    print(msg)
