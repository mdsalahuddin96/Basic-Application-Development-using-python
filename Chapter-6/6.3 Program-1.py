# creating a function
def generatorExample():
   yield "P"
   yield "Y"
   yield "T"
   yield "H"
   yield "O"
   yield "N"
# calling the generatorExample() function which is created above
result = generatorExample()
# Traversing in the above result(generator object)
for k in result:
   # Printing the corresponding value
   print(k)
