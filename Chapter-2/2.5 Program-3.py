def program9():
    f = open("info.txt","r")
    print(f.tell())     #(i)
    f.seek(4,0)         #(ii)
    print(f.read(5))    #(iii)
    f.seek(10,0)        #iv
    print(f.tell())     #v
    print(f.read(10))   #vi
program9()
