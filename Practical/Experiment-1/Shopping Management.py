# This loop will go on until the budget is an integer or float
while True:
    try:
        bg = float(input("Enter your budget: "))
        # If the budget is an integer or float, it will be stored temporarily in the variable 's'
        s = bg
        break  # Exit the loop if input is valid
    except ValueError:
        print("PRINT NUMBER AS AN AMOUNT")
        exit(1)  # Exiting the program on error instead of using continue

# Dictionary to store product("name"), quantity("quant"), price("price") with empty lists as their values
a = {"name": [], "quant": [], "price": []}

# Converting dictionary to lists for further updating
b = list(a.values())

# Variables to access values from the dictionary 'a'
na = b[0]  # Product names
qu = b[1]  # Quantities
pr = b[2]  # Prices

# This loop terminates when the user selects 2.EXIT option when asked.
# In the try block, it will ask the user for an option as an integer (1 or 2).
# If correct, then proceed, else exit the program.
while True:
    try:
        ch = int(input("1.ADD\n2.EXIT\nEnter your choice: "))
    except ValueError:
        print("\nERROR: Choose only digits from the given options")
        exit(1)  # Exiting the program on error instead of using continue
    else:
        # Check if the budget is greater than zero and the option selected
        # by the user is 1 (to add an item)
        if ch == 1 and s > 0:
            # Input product name
            pn = input("Enter product name: ")
            # Input quantity of the product
            q = input("Enter quantity: ")
            # Input price of the product
            try:
                p = float(input("Enter price of the product: "))
            except ValueError:
                print("Please enter a valid price.")
                continue

            if p > s:
                # Check if the price is greater than the budget
                print("\nCAN'T BUY THE PRODUCT")
                continue
            else:
                # Check if the product name is already in the list
                if pn in na:
                    # Find the index of that product
                    ind = na.index(pn)
                    # Update quantity and price for the existing product
                    qu[ind] = q
                    pr[ind] = p
                else:
                    # Append new product details to the lists
                    na.append(pn)
                    qu.append(q)
                    pr.append(p)

                # Subtract the price from the budget and assign it to 's'
                s = bg - sum(pr)

                print("\nAmount left:", s)

                # If the budget goes zero, print "NO BUDGET"
                if s <= 0:
                    print("\nNO BUDGET")
                    break
        elif ch == 2:
            break
        else:
            print("Invalid choice. Please enter 1 to add items or 2 to exit.")

# Print the amount left in variable 's'
print("\nAmount left: Rs.", s)

# If the amount left equals any amount in the price list
if s in pr:
    # Print the name of the product that can be bought with the remaining budget
    print("\nAmount left can buy you a", na[pr.index(s)])

print("\n\n\nGROCERY LIST")

# Print the final grocery list
for i in range(len(na)):
    print(na[i], qu[i], pr[i])
