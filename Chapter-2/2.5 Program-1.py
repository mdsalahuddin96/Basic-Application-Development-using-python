def program2():
    f = open("MyFile.txt","w")
    line1=input("Enter the line1 text:")
    line2=input("Enter the line2 text:")
    line3=input("Enter the line3 text:")
    new_line="\n"
    f.write(line1)
    f.write(new_line)
    f.write(line2)
    f.write(new_line)
    f.write(line3)
    f.write(new_line)
    f.close()
program2()
