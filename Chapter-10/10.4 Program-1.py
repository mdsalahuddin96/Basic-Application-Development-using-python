import re
my_string = "purple alice@google.com, blah monkey bob@abc.com blah dishwasher"
temp = my_string.split(',')
for phrase in temp:
    result = re.match("([\w\.-]+)@([\w\.-]+)", phrase)
    print(result)
