import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) #Output: ['ai', 'ai']
x = re.findall("Portugal", txt)
print(x) #: Output []
x = re.search("\s", txt) # Output The first white-space character is located in position: 3
print("The first white-space character is located in position:", x.start())
x = re.search("Portugal", txt)
print(x) #Output: None
x = re.split("\s", txt)
print(x) # Output: ['The', 'rain', 'in', 'Spain']
x = re.split("\s", txt, 1)
print(x) #Output:['The', 'rain in Spain']
x = re.sub("\s", "9", txt)
print(x) # Output: The9rain9in9Spain
x = re.search("ai", txt)
print(x) # Output: Output: this will print an object
