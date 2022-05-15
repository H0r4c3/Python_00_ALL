'https://www.programiz.com/python-programming/methods/string/center'

'''
The center() method returns a string which is padded with the specified character.

The syntax of center() method is:

string.center(width[, fillchar])
center() Parameters
The center() method takes two arguments:

width - length of the string with padded characters
fillchar (optional) - padding character
The fillchar argument is optional. If it's not provided, space is taken as default argument.

Return Value from center()
The center() method returns a string padded with specified fillchar. It doesn't modify the original string.
'''

my_string = "Python"
new_string = my_string.center(24, '*')
print("Centered String: ", new_string)