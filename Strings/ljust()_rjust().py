'https://www.programiz.com/python-programming/methods/string/ljust'

'''
The string ljust() method returns a left-justified string of a given minimum width.

The syntax of ljust() method is:

string.ljust(width[, fillchar])

ljust() method takes two parameters:

width - width of the given string. If width is less than or equal to the length of the string, the original string is returned.
fillchar (Optional) - character to fill the remaining space of the width
'''

string = 'cat'
width = 15
fillchar = '*'

# print left justified string
print(string.ljust(width, fillchar))

