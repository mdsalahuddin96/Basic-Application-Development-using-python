import csv
fh=open("inventoryforFruitsitem.csv","w+",newline="")
w=csv.writer(fh)
# fruits name, unit price, quantity and total price
header=["Fruits Name","Unit Price","quantity","total price"]
w.writerow(header)
data=[]
#Take item data from the user
while True:
    try:
        n=int(input("How many insert Fruits Record:?"))
    except ValueError:
        print("Fruits Record are Number Please again Entered!")
        continue
    else:
        break
for i in range(n):
    print("Enter Fruit record {0}:",i+1)
    fruitsname=input("Enter Fruits Name: ")
    while True:
        try:
            unitprice=float(input("Enter Unit Price: "))
        except ValueError:
            print("Invalid Unit price Please Entered Again")
            continue
        else:
            break
    while True:
        try:
            quantity=int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity Please Entered Again")
            continue
        else:
            break
    totalprice = unitprice*quantity
    # Store items data into CSV(comma-separated values) file
    rec=[fruitsname,unitprice,quantity,totalprice]
    data.append(rec)
w.writerows(data)
fh.close()

#Print fruits items summary data from stored CSV file
print("Print fruits items summary data from stored CSV file")
fh=open("inventoryforFruitsitem.csv","r")
r=csv.reader(fh)
for i in r:
    print(i)
fh.close()
