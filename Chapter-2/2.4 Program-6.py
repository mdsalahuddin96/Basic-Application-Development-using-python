with open("app.log","w") as f:
    #first line
    f.write("Wow! I'm now a python programmer.\n")
    #second line
    f.write("I'm trained by this book.\n")
    #third line
    f.write("This book is published from Haque Publications.")
f.close()
with open("app.log","r") as f:
    print(f.readline())
    print(f.readline())
f.close()
