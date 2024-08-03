def summation():
    n=1
    sum = 0;
    for n in range(100):
        if n%2 == 0:
            continue
        sum += n
    return sum
add = summation()
print("The summation is: ",add)
