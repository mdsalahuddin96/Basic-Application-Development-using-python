def	multiply(numbers):
    result = 1;
    for x in numbers:
        result = result*x
    return result
print("The result of multiplication is",multiply((8,2,3,12,5)))
