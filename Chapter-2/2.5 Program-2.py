def program4():
    with open("info.txt","r") as f1:
       data=f1.read()
    count_capital =0
    count_small=0
    count_digits=0
    for ch in data:
        if ch.islower():
            count_small+=1
        if ch.isupper():
            count_capital+=1
        if ch.isdigit():
            count_digits+=1
    print("Total Number of Capital letters are:",count_capital)
    print("Total Number of Small letters are:",count_small)
    print("Total Number of  digits are:",count_digits)
program4()
