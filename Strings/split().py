'https://www.w3schools.com/python/ref_string_split.asp'

'''
The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.

string.split(separator, maxsplit)
Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

'''
# Example 1
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

# Example 2
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

# Example 3
txt = 'A B C D E F G'
x = txt.split()
print(x)

# Example 4: using maxsplit
txt = "abc#def#ghi#jkl"
x = txt.split("#", maxsplit=2)
print(x)