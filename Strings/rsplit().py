'https://www.w3schools.com/python/ref_string_rsplit.asp'

'''
The rsplit() method splits a string into a list, starting from the right.

If no "max" is specified, this method will return the same as the split() method.

Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

Syntax
string.rsplit(separator, maxsplit)

separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
'''

txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)

print(x)