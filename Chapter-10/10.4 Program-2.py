import re

# Matching the pattern with named group 'int'
m = re.match(r"(?P<int>\d+)\.(\d*)", '3.14')

# Check if there is a match
if m:
    # Print the matched groups
    print(m.group(1))  # This will print '3'
    print(m.group(2))  # This will print '14'
