
# creating a function that accepts a number as an argument
def evenNumbers(num):
   for i in range(1,num+1):   # traversing till that number passed
      if (i%2!=1):  # checking whether the iterator index value is an even number
         yield i     # getting the iterator index value if the condition is true using the yield keyword
result = evenNumbers(100)   # calling the above function to get the odd numbers below 100
for i in result:    # calling the next items in the result list
    print(i,end=" ")
