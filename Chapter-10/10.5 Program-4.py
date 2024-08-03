import re

   	#Input string
input_string = "hello 23, hi 77, lovely 18 and sweet 16"

       #Define the regular expression pattern to match numbers
pattern = r'\d+'

       #Use the re.findall() function to find all matches of the
       #pattern in the string
matches = re.findall(pattern, input_string)

       #Convert the matched strings to integers
numbers = [int(match) for match in matches]

       #Print the extracted numbers
print(numbers)
