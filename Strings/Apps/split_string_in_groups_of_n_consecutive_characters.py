'https://www.geeksforgeeks.org/python-split-string-in-groups-of-n-consecutive-characters/'

# String initialization
string = "Geeksforgeeks"
  
# Defining splitting point
n = 3
  
# Using list comprehension
out = [(string[i:i+n]) for i in range(0, len(string), n)]
  
# Printing output
print(out)