'https://www.programiz.com/python-programming/methods/string/lstrip'

'''
The lstrip() method returns a copy of the string with leading characters removed (based on the string argument passed).

The lstrip() removes characters from the left based on the argument (a string specifying the set of characters to be removed).

The syntax of lstrip() is:

string.lstrip([chars])

lstrip() Parameters
chars (optional) - a string specifying the set of characters to be removed.
If chars argument is not provided, all leading whitespaces are removed from the string.

Return Value from lstrip() 
lstrip() returns a copy of the string with leading characters stripped.

All combinations of characters in the chars argument are removed from the left of the string until the first mismatch.
'''

my_string = '   this is good '

# Leading whitespace are removed
print(my_string.lstrip())


# Argument doesn't contain space
# No characters are removed.
print(my_string.lstrip('sti'))

print(my_string.lstrip('s ti'))


website = 'https://www.programiz.com/'

print(website.lstrip('htps:/.'))

print(my_string.rstrip('good '))


txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)


# https://www.geeksforgeeks.org/python-string-methods-set-3-strip-lstrip-rstrip-min-max-maketrans-translate-relplace/
# Python code to demonstrate working of strip(), lstrip() and rstrip()
str = "---geeksforgeeks---"
 
# using strip() to delete all '-'
print (" String after stripping all '-' is : ", end="")
print (str.strip('-'))
 
# using lstrip() to delete all trailing '-'
print (" String after stripping all leading '-' is : ", end="")
print (str.lstrip('-'))
 
# using rstrip() to delete all leading '-'
print (" String after stripping all trailing '-' is : ", end="")
print (str.rstrip('-'))