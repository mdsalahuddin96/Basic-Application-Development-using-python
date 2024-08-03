
# creating a function that accepts a number as an argument
def oddNumbers(num):
   for i in range(num):    # traversing till that number passed
      if (i%2!=0):   # checking whether the iterator index value is an odd number
         yield i     # getting the iterator index value if the condition is true using the yield keyword
result = oddNumbers(100)    # calling the above function to get the odd numbers below 8
for i in result:    # calling the next items in the result list
    print(i,end=" ")
