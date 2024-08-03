def add_numbers():
    numbers = []  #Create an empty list to store the numbers

#Use a loop to input five numbers from the user and add them
#to the  list
    for i in range(5):
        num = float(input(f"Enter number {i + 1}: "))  # Assuming
    #floating-point numbers
        numbers.append(num)

#Calculate the sum of the numbers in the list
    total = sum(numbers)

#Print the sum
    print(f"The sum of the numbers is: {total}")

#Call the function to add numbers
add_numbers()

