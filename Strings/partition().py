'https://www.w3schools.com/python/ref_string_partition.asp'

'''
The partition() method searches for a specified string, and splits the string into a tuple containing three elements:

The first element contains the part before the specified string.

The second element contains the specified string.

The third element contains the part after the string.

Note: This method searches for the first occurrence of the specified string.

Syntax:

string.partition(value)

'''

# Example
# Search for the word "bananas", and return a tuple with three elements:

# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)