def str_rev(str):
    str1 = ''
    index = len(str)
    while index > 0:
        str1 += str[index-1]
        index = index -1
    return str1
str1 = input("Enter an String:- ")
print("The reverse string is:- ",str_rev(str1))
