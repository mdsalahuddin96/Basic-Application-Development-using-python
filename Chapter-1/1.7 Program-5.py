def Test_Prime(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        for x in range(2,n):
            if(n%x == 0):
                return 0
    return 1
n = int(input("Enter a number to check prime or not: "))
if(Test_Prime(n)==1):
    print("This is a prime number.")
else:
    print("This is not a prime number.")
